# WaterWoods Labs

WaterWoods Labs maintains product-specific Freqtrade integrations. UMX and Binance Portfolio
Margin are independent products with separate source branches, release prefixes, and container
images.

UMX was formerly named XCoin. Historical releases retain their original names and identifiers.

## Products

| Product | Source | Releases | Image |
| --- | --- | --- | --- |
| UMX spot and USDT perpetual futures | [`umx` branch](https://github.com/WaterWoods-Labs/freqtrade/tree/umx) | [`umx-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=umx-) | `ghcr.io/waterwoods-labs/freqtrade-umx` |
| Binance standard Portfolio Margin through PAPI | [`binance-portfolio-margin` branch](https://github.com/WaterWoods-Labs/freqtrade/tree/binance-portfolio-margin) | [`binance-portfolio-margin-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=binance-portfolio-margin-) | `ghcr.io/waterwoods-labs/freqtrade-binance-portfolio-margin` |

Use the published immutable `@sha256:<digest>` for deployment. Product images are not
interchangeable.

Product maintenance: [UMX](https://github.com/WaterWoods-Labs/freqtrade/blob/umx/docs/umx-maintenance.md)
and [Portfolio Margin](https://github.com/WaterWoods-Labs/freqtrade/blob/binance-portfolio-margin/docs/binance-portfolio-margin-maintenance.md).
For contribution boundaries, see the
[organization guide](https://github.com/WaterWoods-Labs/.github/blob/main/CONTRIBUTING.md).

## Support and security

- Report reproducible UMX problems with the repository's
  [UMX issue forms](https://github.com/WaterWoods-Labs/freqtrade/issues/new/choose).
- Report Portfolio Margin problems through a
  [Portfolio Margin bug form](https://github.com/WaterWoods-Labs/freqtrade/issues/new?template=binance_portfolio_margin_bug.yml)
  and include the affected branch or release tag.
- Problems that also reproduce on official Freqtrade belong in the
  [upstream project](https://github.com/freqtrade/freqtrade/issues).

Security vulnerabilities must be sent through
[private vulnerability reporting](https://github.com/WaterWoods-Labs/freqtrade/security/advisories/new),
never through a public issue. Do not post API keys, API secrets, tokens, signatures, account data,
private orders, or unredacted live logs.

Trading software carries financial risk. Start with dry-run, review the release notes, and never
place credentials in source control.
