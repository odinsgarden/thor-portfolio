# thor-portfolio
### thor-portfolio

Curated OSINT, recon and automation toolkit showcase — sanitized examples and demos.

---

### Overview
Thor Whittaker’s curated technical showcase: a sanitized selection of OSINT and reconnaissance automation, device-sync tooling, and example scripts that demonstrate data-processing pipelines and Portable PowerShell packaging (private). This repository contains non-sensitive examples, screenshots, and architecture notes intended for public demonstration only — sensitive code, raw data, and runtime artifacts remain private.

---

### Key capabilities
- **Recon automation:** Shodan, Wigle, WHOIS, httpx integrations (sanitized)  
- **OSINT pipelines:** host list generation, graph export, CSV outputs  
- **Device and radio tooling:** UV5R sync scripts (private implementations)  
- **Packaging:** Portable PowerShell runtime snapshots (private)  
- **Demonstrations:** screenshots, sanitized example scripts, and minimal runbooks

---

### Public examples
- **examples/scan_phishing_emails.py** — sanitized phishing detection example showing parsing and heuristic scoring  
- **assets/page_capture.png** — UI / results screenshot for demo purposes  
- **docs/overview.md** — architecture notes and data flow diagrams (sanitized)

---

### How to run the examples (minimal, safe)
1. Create and activate a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Run the sanitized scanner example:
```bash
python examples/scan_phishing_emails.py --input examples/sample_emails.json --output results.csv
```
3. View demo screenshot:
```bash
# open assets/page_capture.png with your image viewer
xdg-open assets/page_capture.png
```

Notes:
- All example inputs are sanitized; do not run on sensitive or production datasets without review.
- Examples intentionally avoid keys, credentials, or payloads.

---

### How it was built
- Languages: **Python**, minimal PowerShell snippets for illustration.  
- Tooling: virtualenv/venv, standard pip workflow, basic Makefile for convenience.  
- Design: modular examples that demonstrate patterns (ingest → transform → export) without shipping production runtime artifacts.

---

### Privacy & licensing
- Public repo contains only sanitized examples, screenshots, and documentation. Full toolkits, runtime artifacts, and raw data are private.  
- Default license: **MIT** for public examples (change as needed). Add a LICENSE file if you want another license.

---

### Contact
- **GitHub:** github.com/odinsgarden  
- **Email:** thor.whittaker@outlook.com

---


