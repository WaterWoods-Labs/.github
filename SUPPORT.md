# Support

## Choose the correct product

| Scope | Branch and releases | Support route |
| --- | --- | --- |
| XCoin integration | `xcoin`; tags prefixed `xcoin-` | [XCoin issue forms](https://github.com/WaterWoods-Labs/freqtrade/issues/new/choose) |
| Binance Portfolio Margin/PAPI | `binance-portfolio-margin`; tags prefixed `binance-portfolio-margin-` | [Portfolio Margin bug form](https://github.com/WaterWoods-Labs/freqtrade/issues/new?template=binance_portfolio_margin_bug.yml) |
| Behavior that reproduces on official Freqtrade | Official upstream branches and releases | [Freqtrade issue tracker](https://github.com/freqtrade/freqtrade/issues) |

Use the repository's [issue form chooser](https://github.com/WaterWoods-Labs/freqtrade/issues/new/choose)
for feature proposals or when the correct product form is not obvious.

For a WaterWoods product issue, include the product name, exact release tag or commit, dry-run or
live mode, operating system, and a minimal reproduction. Use an immutable image digest when a
container is involved:

- XCoin: `ghcr.io/waterwoods-labs/freqtrade-xcoin@sha256:<digest>`;
- Binance Portfolio Margin:
  `ghcr.io/waterwoods-labs/freqtrade-binance-portfolio-margin@sha256:<digest>`.

Do not attach credentials, signatures, account identifiers, private orders, databases, or
unredacted logs. Report suspected vulnerabilities through the private route in
[`SECURITY.md`](SECURITY.md), not through a support issue.

General strategy design, profitability, and financial advice are outside the support scope.
