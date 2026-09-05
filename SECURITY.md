# Security policy

## Supported scope

WaterWoods accepts vulnerability reports for the currently maintained UMX and Binance Portfolio
Margin product branches and their published releases:

- `umx` with release tags prefixed `umx-`;
- `binance-portfolio-margin` with release tags prefixed `binance-portfolio-margin-`.

A problem that reproduces unchanged on official Freqtrade should follow the
[upstream Freqtrade security policy](https://github.com/freqtrade/freqtrade/security/policy).

## Report privately

Use [private vulnerability reporting](https://github.com/WaterWoods-Labs/freqtrade/security/advisories/new)
for WaterWoods product vulnerabilities. Do not open a public issue for a suspected vulnerability.

Describe the affected product, branch or immutable release tag, impact, and minimal reproduction.
Redact all exchange credentials and private trading data. Never submit real API keys, API secrets,
tokens, request signatures, account identifiers, private orders, database contents, or unredacted
live logs.

Public issues containing sensitive material may expose it permanently even after editing. If the
private reporting form is unavailable, do not publish the report; wait until a private GitHub
reporting route is available.
