# Contributing

Thank you for improving a WaterWoods project. Keep every change within one product or community
documentation scope.

## Route the change

- Target `xcoin` for XCoin adapter behavior, tests, documentation, CI, and releases.
- Target `binance-portfolio-margin` for Binance Portfolio Margin/PAPI behavior, tests,
  documentation, CI, and releases.
- Target this repository's `main` branch only for organization profile and default community
  health files.
- For any other repository-local scope, follow that repository's own contribution and branch
  guidance; repository files take precedence over these organization defaults.
- Propose changes that apply unchanged to official Freqtrade to the
  [upstream project](https://github.com/freqtrade/freqtrade) first.

Do not combine XCoin and Portfolio Margin implementation changes in one pull request. A shared
Freqtrade-core extension point must be justified and tested independently for each affected
product.

## Pull requests

1. Start from the latest intended target branch.
2. Keep the change focused and explain its product boundary.
3. Add or update tests and documentation in the same pull request.
4. Run the repository's focused validation and any required full suite.
5. State release, image, configuration, and migration impact.

Never commit API keys, API secrets, tokens, request signatures, account data, private orders,
databases, runtime logs, downloaded market data, or live configuration. Examples must contain
obvious placeholders only.

Security vulnerabilities belong in
[private vulnerability reporting](https://github.com/WaterWoods-Labs/freqtrade/security/advisories/new),
not in a pull request or public issue.
