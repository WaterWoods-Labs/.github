# WaterWoods-Labs organization metadata

This public repository contains the WaterWoods Labs organization profile and default community
health files. Product source code, runtime configuration, credentials, logs, and account data do
not belong here.

## Product routes

WaterWoods maintains two isolated Freqtrade products in
[`WaterWoods-Labs/freqtrade`](https://github.com/WaterWoods-Labs/freqtrade). Changes, releases, and
container images must stay within the matching product boundary.

| Product | Source branch | Release prefix | Container image | Support |
| --- | --- | --- | --- | --- |
| UMX | [`umx`](https://github.com/WaterWoods-Labs/freqtrade/tree/umx) | [`umx-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=umx-) | `ghcr.io/waterwoods-labs/freqtrade-umx` | [UMX issue forms](https://github.com/WaterWoods-Labs/freqtrade/issues/new/choose) |
| Binance Portfolio Margin | [`binance-portfolio-margin`](https://github.com/WaterWoods-Labs/freqtrade/tree/binance-portfolio-margin) | [`binance-portfolio-margin-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=binance-portfolio-margin-) | `ghcr.io/waterwoods-labs/freqtrade-binance-portfolio-margin` | [Portfolio Margin bug form](https://github.com/WaterWoods-Labs/freqtrade/issues/new?template=binance_portfolio_margin_bug.yml) |

Deploy published images by immutable digest, for example `IMAGE@sha256:<digest>`. Never substitute
one product image for the other.

UMX is the current name of the former XCoin integration. When citing historical XCoin releases,
keep their original `xcoin-*` tags and `freqtrade-xcoin` image identifiers; route new changes to UMX.

## Repository contents

- [`profile/README.md`](profile/README.md) is rendered on the organization profile.
- [`SECURITY.md`](SECURITY.md) defines the private vulnerability-reporting route.
- [`SUPPORT.md`](SUPPORT.md) routes product and upstream support requests.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) defines contribution boundaries.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) is the organization
  fallback pull-request checklist.

## Validation

Pull requests and `main` updates run [community validation](.github/workflows/validate.yml): local
Markdown link targets, YAML syntax, read-only workflow permissions, pinned action revisions, and
high-confidence sensitive-file patterns. External URLs are reviewed separately; the check does
not claim to verify their availability or to detect every possible secret.

Run `python scripts/validate_repository.py` with `requirements-validation.txt` installed in the
managed validation environment. Docker-only workstations run this in an ephemeral validation
container. Product and research repositories retain their own checks and approval policies.
