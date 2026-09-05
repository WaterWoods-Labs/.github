"""Validate this small community repository without network access or write operations."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".venv", "__pycache__", ".pytest_cache"}
FORBIDDEN = {"user_data", "secrets", "credentials", "logs", "data", "backups"}
SECRET = re.compile(
    r"gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|"
    r"AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def validate(root: Path) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in IGNORED for part in relative.parts):
            continue
        label = relative.as_posix()
        if path.is_symlink():
            errors.append(f"{label}: symbolic links are not allowed")
            continue
        if not path.is_file():
            continue
        if (any(part.lower() in FORBIDDEN for part in relative.parts)
                or path.name.startswith(".env") or path.name.endswith(".local.json")
                or path.suffix.lower() in {".db", ".sqlite", ".sqlite3", ".log", ".zip", ".pem", ".key"}):
            errors.append(f"{label}: runtime or sensitive file is not allowed")
            continue
        if path.stat().st_size > 1024 * 1024:
            errors.append(f"{label}: community files must be smaller than 1 MiB")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"{label}: readable UTF-8 text is required")
            continue
        if SECRET.search(text):
            errors.append(f"{label}: high-confidence credential pattern detected (value redacted)")
        if path.suffix == ".md":
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for target in LINK.findall(prose):
                parts = urlsplit(target.strip("<>"))
                if parts.scheme or parts.netloc:
                    if parts.scheme not in {"https", "http", "mailto"}:
                        errors.append(f"{label}: unsupported link scheme")
                    continue
                destination = (path.parent / unquote(parts.path)).resolve()
                if not destination.is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f"{label}: missing or escaping local link: {target}")
        if path.suffix in {".yml", ".yaml"}:
            try:
                document = yaml.load(text, Loader=yaml.BaseLoader)
            except yaml.YAMLError:
                errors.append(f"{label}: invalid YAML")
                continue
            if relative.parts[:2] == (".github", "workflows"):
                if not isinstance(document, dict) or document.get("permissions") != {"contents": "read"}:
                    errors.append(f"{label}: workflow permissions must be contents: read")
                    continue
                for job in document.get("jobs", {}).values():
                    if job.get("permissions", {"contents": "read"}) != {"contents": "read"}:
                        errors.append(f"{label}: job permissions must be contents: read")
                    for step in job.get("steps", []):
                        action = step.get("uses")
                        if action and not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}", action):
                            errors.append(f"{label}: actions must be pinned to a full commit SHA")
    return errors


if __name__ == "__main__":
    problems = validate(ROOT)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("Community documents, local links, YAML, action pins, and sensitive-file checks passed.")
