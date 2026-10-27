# Honeypot HTTP Server Demo

A small Python `http.server` example that serves a page on `localhost:8080` and records requests to a specific hidden path. Requests to `/hidden-admin-login-trap` add the client address to an in-memory set; subsequent requests from that address receive HTTP 403 while the process remains running.

## Run

```bash
python honeypot.py
```

Open `http://localhost:8080/` in a browser to view the page. The hidden link is present in the HTML, but any client can request the trap path directly.

## Scope and limitations

This is a local demonstration, not an anti-scraping or production security system. A request to the trap path does not prove that the client is a bot. The block list is in memory, disappears when the process exits, and uses the address observed by the server; there is no persistence, proxy-aware identity handling, authentication, rate limiting, or robust HTTP-server configuration. The server binds to localhost by default.
