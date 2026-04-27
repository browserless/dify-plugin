# Privacy

This plugin connects Dify to the Browserless MCP server (`https://mcp.browserless.io/mcp`).

## Data sent to Browserless

When you invoke a tool, the following is transmitted to `mcp.browserless.io` over HTTPS:

- The Browserless API token you configured in plugin credentials, sent as a `Bearer` token.
- The arguments you (or the LLM) pass to the tool (URLs, search queries, JavaScript code, selectors, etc.).
- Standard HTTP metadata (User-Agent, IP address).

Browserless then opens a real Chromium browser to perform the requested action and returns the result.

## Data Browserless processes

Browserless processes the request to deliver the requested output (rendered page content, screenshots, search results, etc.). It also records usage metrics tied to your token for billing.

## Data retention

Browserless does not persistently store the page content, screenshots, or other output it returns to you. Usage metrics (request counts, byte counts, time consumed) are retained for billing and analytics.

## Third parties

Some Browserless tools may invoke third-party services on your behalf (e.g. residential proxy vendors for `browserless_smartscraper`, 2Captcha for captcha-solving features). See the Browserless privacy policy for details.

## Full policy

See [https://www.browserless.io/privacy](https://www.browserless.io/privacy).

## Contact

support@browserless.io
