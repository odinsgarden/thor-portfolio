# Thor Whitaker - Technical Showcase
[![CI](https://github.com/odinsgarden/thor-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/odinsgarden/thor-portfolio/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Curated OSINT, recon and automation toolkit showcase — sanitized examples and demos.

---

## Portfolio
Live site / portfolio: https://github.com/thorwhitaker/thorwhitaker.github.io/blob/main/index.md

---

## Overview
Thor Whittaker’s curated technical showcase: a sanitized selection of OSINT and reconnaissance automation, device-sync tooling, and example scripts that demonstrate phishing-detection workflows and Portable Personal Playback (private). This repository contains non-sensitive examples, screenshots, and architecture notes intended for public demonstration only — sensitive code, raw data, and full runtime artifacts remain private.

---

## Key capabilities
- **Reconnaissance:** OSINT pipelines, Shodan, WHOIS, Wigle, httpx integrations (sanitized)  
- **Threat data:** MISP integration patterns and sanitized graph exports  
- **Tooling:** Python automation, small PowerShell examples for packaging/portability  
- **Playback:** Portable Personal Playback (PPP) concepts and sanitized sync notes (private components)  
- **Outputs:** CSV/graph exports, demo screenshots, minimal runbooks

---

## Public examples
- **examples/osint_phishing_emails.py** — sanitized phishing detection example showing parsing and heuristic scoring  
- **examples/sync_ppp.py** — sanitized PPP sync script (illustrative only)  
- **examples/ppp_notes.md** — PPP notes and screenshots (sanitized)  
- **examples/architecture.md** — architecture notes and data flow diagrams (sanitized)  
- **assets/page_capture.png** — demo screenshot

---

## How to run the examples (minimal, safe)
1. Create and activate a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Run the sanitized scanner example:
```bash
python examples/osint_phishing_emails.py --input examples/sample_emails.json --output results.csv
```
3. View demo screenshot:
```bash
xdg-open assets/page_capture.png
```

Notes:
- Example inputs are sanitized; do not run on sensitive or production datasets without review.  
- Examples do not include credentials, private keys, or raw sensitive datasets.

---

## How it was built
- Languages: **Python** with minimal PowerShell snippets for packaging examples.  
- Tooling: venv, pip, optional Makefile for convenience.  
- CI: Lightweight GitHub Actions workflow to run tests and linting on pushes/PRs.

---

## Continuous Integration
A simple CI workflow runs on pushes and pull requests to `main`. It installs dependencies, runs `pytest`, and runs `flake8`. See `.github/workflows/ci.yml` for details.

Run checks locally:
```bash
pip install pytest flake8
pytest -q
flake8
```

---

## Contributing
Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the preferred workflow, pull request guidelines, and testing expectations.

Preferred workflow:
1. Fork the repo  
2. Create a descriptive branch (e.g., `feature/scan-parser`)  
3. Open a pull request with a short summary, motivation, and tests/examples

---

## Code of Conduct
This project follows a Contributor Covenant style code of conduct. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

---

## License
This repository is published under the MIT License. See the full text in the [LICENSE](LICENSE) file.

---

## Contact
- **GitHub:** github.com/odinsgarden  
- **Email:** thor.whittaker@outlook.com

--- 

