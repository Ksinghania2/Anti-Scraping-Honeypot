# Automated Anti-Scraping Honey-Pot Security Engine

An automated web-security mechanism built from scratch in Python to identify, log, and dynamically block unauthorized automated data scrapers and malicious web crawlers.

By deploying hidden directory traps within standard HTML architectures, this lightweight engine differentiates between human traffic and automated scripts, executing instant perimeter defense actions at the network level.

## ⚡ Core Operational Features
* **Behavioral Analysis (Honey-Pot Trap):** Injects specific directory access points hidden from human interaction via hidden CSS parameters (`display:none`) but fully visible to structural web scrapers.
* **Dynamic IP Blacklisting:** Utilizes an active `set` collection to record flagged IP coordinates, enforcing a zero-tolerance access rule upon violation.
* **Low-Overhead Filtering:** Bypasses heavy enterprise web-application firewalls by managing security rules directly inside native network socket request pathways.

## 🛠️ Setup & Execution

### 1. Launch the Security Engine
Run the native Python server script:
```bash
python3 honeypot.py

Live Verification Metrics
Human Validation: Navigate to http://localhost:8080/ via any standard browser. The interface renders cleanly with zero security interference.

Intrusion Detection: Accessing the hidden path http://localhost:8080/hidden-admin-login-trap fires an instant alert to the server console and blocks the source device permanently with an HTTP 403 Forbidden status.