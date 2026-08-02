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
| XCoin | [`xcoin`](https://github.com/WaterWoods-Labs/freqtrade/tree/xcoin) | [`xcoin-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=xcoin-) | `ghcr.io/waterwoods-labs/freqtrade-xcoin` | [XCoin issue forms](https://github.com/WaterWoods-Labs/freqtrade/issues/new/choose) |
| Binance Portfolio Margin | [`binance-portfolio-margin`](https://github.com/WaterWoods-Labs/freqtrade/tree/binance-portfolio-margin) | [`binance-portfolio-margin-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=binance-portfolio-margin-) | `ghcr.io/waterwoods-labs/freqtrade-binance-portfolio-margin` | [Portfolio Margin bug form](https://github.com/WaterWoods-Labs/freqtrade/issues/new?template=binance_portfolio_margin_bug.yml) |

Deploy published images by immutable digest, for example `IMAGE@sha256:<digest>`. Never substitute
one product image for the other.

## Repository contents

- [`profile/README.md`](profile/README.md) is rendered on the organization profile.
- [`SECURITY.md`](SECURITY.md) defines the private vulnerability-reporting route.
- [`SUPPORT.md`](SUPPORT.md) routes product and upstream support requests.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) defines contribution boundaries.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) is the organization
  fallback pull-request checklist.
