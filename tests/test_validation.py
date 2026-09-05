"""Exercise review-blocking mistakes using disposable community-repository fixtures."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "community_validation", Path(__file__).resolve().parents[1] / "scripts/validate_repository.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CommunityValidationTest(unittest.TestCase):
    def check(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return MODULE.validate(root)

    def test_local_document_link_and_external_link_are_accepted(self):
        self.assertEqual([], self.check({
            "README.md": "[Guide](docs/guide.md) [Site](https://example.com)",
            "docs/guide.md": "# Guide\n",
        }))

    def test_missing_and_escaping_document_targets_are_rejected(self):
        for target in ("missing.md", "../outside.md"):
            with self.subTest(target=target):
                self.assertTrue(self.check({"README.md": f"[Guide]({target})"}))

    def test_invalid_yaml_is_rejected(self):
        self.assertTrue(self.check({"invalid.yml": "key: [unfinished"}))

    def test_credentials_are_redacted_in_diagnostics(self):
        value = "gh" + "p_" + "A" * 36
        problems = self.check({"README.md": value})
        self.assertTrue(problems)
        self.assertNotIn(value, "\n".join(problems))

    def test_runtime_files_are_rejected(self):
        self.assertTrue(self.check({"example.local.json": "{}"}))

    def test_workflow_write_permissions_and_mutable_actions_are_rejected(self):
        for content in (
            "permissions: {contents: write}\njobs: {}",
            "permissions: {contents: read}\njobs:\n  check:\n    steps:\n      - uses: actions/checkout@v7",
        ):
            with self.subTest(content=content):
                self.assertTrue(self.check({".github/workflows/check.yml": content}))


if __name__ == "__main__":
    unittest.main()
