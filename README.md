# Browserless

**Author:** browserless
**Type:** tool
**Repository:** https://github.com/browserless/dify-plugin

Headless browser automation for AI agents, powered by [Browserless](https://browserless.io). This plugin proxies the official Browserless MCP server (`https://mcp.browserless.io/mcp`) and exposes its tools as native Dify tools.

## What you can do

- **Scrape** any web page and get markdown, HTML, screenshots, PDFs, or links
- **Search** the web and optionally scrape every result
- **Map** every URL on a website (sitemap + link discovery)
- **Crawl** a site and scrape every page
- **Export** a URL in its native content type
- **Run custom Puppeteer code** server-side and get the result back
- **Download files** triggered by Puppeteer code
- **Audit performance** with Lighthouse
- **Drive a stateful agent** (goto, click, type, snapshot, etc.) — full ReAct browser loop

## Setup

1. Get a Browserless API token by signing up at [browserless.io/signup/email](https://www.browserless.io/signup/email).
2. In Dify: **Tools → Browserless → Authorize**, paste the token, save.
3. Add any Browserless tool to an Agent or Workflow node.

## Tools

| Tool | Use case |
|---|---|
| `browserless_smartscraper` | Extract page content as markdown / HTML / screenshot / PDF / links |
| `browserless_search` | SearXNG-backed web/news/image search, optional inline scrape |
| `browserless_map` | Discover every URL on a site |
| `browserless_crawl` | Crawl + scrape a site up to a depth |
| `browserless_export` | Fetch a URL in its native content type (HTML, PDF, image…) |
| `browserless_function` | Run arbitrary Puppeteer JS, return a typed payload |
| `browserless_download` | Run Puppeteer JS, return a file Chrome downloads |
| `browserless_performance` | Run a Lighthouse audit |
| `browserless_agent` | Persistent multi-turn agent session (goto, click, type, snapshot, …) |

## Privacy

See [PRIVACY.md](./PRIVACY.md). Browserless privacy policy: https://www.browserless.io/privacy.

## Support

- Issues: https://github.com/browserless/dify-plugin/issues
- Email: support@browserless.io
