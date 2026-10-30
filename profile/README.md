# WaterWoods Labs

WaterWoods Labs maintains product-specific Freqtrade integrations. UMX and Binance Portfolio
Margin are independent products with separate source branches, release prefixes, and container
images.

UMX was formerly named XCoin. Historical releases retain their original names and identifiers.

## Choose a product

| Entry | UMX | Binance Portfolio Margin (PAPI) |
| --- | --- | --- |
| Markets | Spot and USDT perpetual futures | Standard Portfolio Margin accounts trading USD-M perpetuals |
| Source | [`umx`](https://github.com/WaterWoods-Labs/freqtrade/tree/umx) | [`binance-portfolio-margin`](https://github.com/WaterWoods-Labs/freqtrade/tree/binance-portfolio-margin) |
| Adapter and configuration | [UMX guide](https://github.com/WaterWoods-Labs/freqtrade/blob/umx/docs/umx-adapter.md) | [PAPI guide](https://github.com/WaterWoods-Labs/freqtrade/blob/binance-portfolio-margin/docs/binance-portfolio-margin-adapter.md) |
| Maintenance and contribution routing | [UMX maintenance](https://github.com/WaterWoods-Labs/freqtrade/blob/umx/docs/umx-maintenance.md) | [PAPI maintenance](https://github.com/WaterWoods-Labs/freqtrade/blob/binance-portfolio-margin/docs/binance-portfolio-margin-maintenance.md) |
| Releases | [`umx-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=umx-&expanded=true) | [`binance-portfolio-margin-*`](https://github.com/WaterWoods-Labs/freqtrade/releases?q=binance-portfolio-margin-&expanded=true) |
| Image | `ghcr.io/waterwoods-labs/freqtrade-umx` | `ghcr.io/waterwoods-labs/freqtrade-binance-portfolio-margin` |

The repository's default branch is `umx`. For PAPI, use the `binance-portfolio-margin` source
link above and select that branch when cloning or opening a pull request. The `develop` and
`stable` branches remain official Freqtrade mirrors.

Use the published immutable `@sha256:<digest>` for deployment. Product images are not
interchangeable.

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
