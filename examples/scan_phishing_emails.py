

"""Simple phishing-email scanner (style fixed, no hard-coded secrets)."""

import imaplib
import email
import re
from email.header import decode_header
from typing import List


# CONFIGURATION (use env vars or secrets in CI instead of hard-coding)
EMAIL_ACCOUNT_ENV = "EMAIL_ACCOUNT"
EMAIL_PASSWORD_ENV = "EMAIL_PASSWORD"
IMAP_SERVER = "imap.gmail.com"
FOLDER = "INBOX"

PHISHING_DOMAINS = [
    "ssaib.uk.com", "daydarylmann.com", "tinyurl.com"
]

PHISHING_KEYWORDS = [
    "icloud locked",
    "payment issue",
    "apple support",
    "account suspended",
    "update payment",
]


def clean_subject(subject: bytes | str) -> str:
    """Decode email subject safely."""
    if subject is None:
        return ""
    if isinstance(subject, bytes):
        try:
            decoded, _ = decode_header(subject)[0]
            return decoded.decode() if isinstance(decoded, bytes) else str(decoded)
        except Exception:
            return subject.decode("utf-8", errors="ignore")
    return str(subject)


def extract_urls(text: str) -> List[str]:
    """Return list of http(s) URLs in text."""
    if not text:
        return []
    return re.findall(r"https?://[^\s<>\"']+", text)


def check_if_phishing(subject: str, sender: str, urls: List[str]) -> bool:
    """Return True if subject/sender/urls indicate likely phishing."""
    subj = (subject or "").lower()
    snd = (sender or "").lower()

    if any(keyword in subj for keyword in PHISHING_KEYWORDS):
        return True

    for domain in PHISHING_DOMAINS:
        if domain in snd or any(domain in (url or "").lower() for url in urls):
            return True

    return False


def scan_emails(email_account: str, email_password: str, folder: str = FOLDER) -> List[dict]:
    """Connect to IMAP, scan recent emails, return list of suspected phishing hits."""
    hits: List[dict] = []

    print("[*] Connecting to email server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    try:
        mail.login(email_account, email_password)
    except imaplib.IMAP4.error as exc:
        print(f"[!] IMAP login failed: {exc}")
        return hits

    try:
        mail.select(folder)
        status, messages = mail.search(None, "ALL")
        if status != "OK" or not messages or not messages[0]:
            return hits

        email_ids = messages[0].split()
        # Limit to latest 500 emails
        for i in email_ids[::-1][:500]:
            res, msg_data = mail.fetch(i, "(RFC822)")
            if res != "OK":
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = clean_subject(msg.get("subject"))
                    sender = msg.get("from", "")
                    urls: List[str] = []

                    if msg.is_multipart():
                        for part in msg.walk():
                            ctype = part.get_content_type()
                            if ctype == "text/plain" and part.get_payload(decode=True):
                                body = part.get_payload(decode=True).decode(errors="ignore")
                                urls += extract_urls(body)
                    else:
                        payload = msg.get_payload(decode=True)
                        if payload:
                            body = payload.decode(errors="ignore")
                            urls += extract_urls(body)

                    if check_if_phishing(subject, sender, urls):
                        hits.append(
                            {
                                "Subject": subject,
                                "From": sender,
                                "URLs": urls,
                            }
                        )
    finally:
        try:
            mail.logout()
        except Exception:
            pass

    return hits


def main() -> None:
    import os

    email_account = os.getenv(EMAIL_ACCOUNT_ENV)
    email_password = os.getenv(EMAIL_PASSWORD_ENV)

    if not email_account or not email_password:
        print(
            "[!] Missing credentials. Set environment variables "
            f"{EMAIL_ACCOUNT_ENV} and {EMAIL_PASSWORD_ENV}"
        )
        return

    phishing_hits = scan_emails(email_account, email_password)
    print(f"\n[*] Scan complete. Found {len(phishing_hits)} suspicious emails.\n")

    for i, hit in enumerate(phishing_hits, 1):
        print(f"--- Suspicious Email #{i} ---")
        print(f"From: {hit['From']}")
        print(f"Subject: {hit['Subject']}")
        for url in hit["URLs"]:
            print(f"→ URL: {url}")
        print()


if __name__ == "__main__":
    main()"""Simple phishing-email scanner (style fixed, no hard-coded secrets)."""

import imaplib
import email
import re
from email.header import decode_header
from typing import List


# CONFIGURATION (use env vars or secrets in CI instead of hard-coding)
EMAIL_ACCOUNT_ENV = "EMAIL_ACCOUNT"
EMAIL_PASSWORD_ENV = "EMAIL_PASSWORD"
IMAP_SERVER = "imap.gmail.com"
FOLDER = "INBOX"

PHISHING_DOMAINS = [
    "ssaib.uk.com", "daydarylmann.com", "tinyurl.com"
]

PHISHING_KEYWORDS = [
    "icloud locked",
    "payment issue",
    "apple support",
    "account suspended",
    "update payment",
]


def clean_subject(subject: bytes | str) -> str:
    """Decode email subject safely."""
    if subject is None:
        return ""
    if isinstance(subject, bytes):
        try:
            decoded, _ = decode_header(subject)[0]
            return decoded.decode() if isinstance(decoded, bytes) else str(decoded)
        except Exception:
            return subject.decode("utf-8", errors="ignore")
    return str(subject)


def extract_urls(text: str) -> List[str]:
    """Return list of http(s) URLs in text."""
    if not text:
        return []
    return re.findall(r"https?://[^\s<>\"']+", text)


def check_if_phishing(subject: str, sender: str, urls: List[str]) -> bool:
    """Return True if subject/sender/urls indicate likely phishing."""
    subj = (subject or "").lower()
    snd = (sender or "").lower()

    if any(keyword in subj for keyword in PHISHING_KEYWORDS):
        return True

    for domain in PHISHING_DOMAINS:
        if domain in snd or any(domain in (url or "").lower() for url in urls):
            return True

    return False


def scan_emails(email_account: str, email_password: str, folder: str = FOLDER) -> List[dict]:
    """Connect to IMAP, scan recent emails, return list of suspected phishing hits."""
    hits: List[dict] = []

    print("[*] Connecting to email server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    try:
        mail.login(email_account, email_password)
    except imaplib.IMAP4.error as exc:
        print(f"[!] IMAP login failed: {exc}")
        return hits

    try:
        mail.select(folder)
        status, messages = mail.search(None, "ALL")
        if status != "OK" or not messages or not messages[0]:
            return hits

        email_ids = messages[0].split()
        # Limit to latest 500 emails
        for i in email_ids[::-1][:500]:
            res, msg_data = mail.fetch(i, "(RFC822)")
            if res != "OK":
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = clean_subject(msg.get("subject"))
                    sender = msg.get("from", "")
                    urls: List[str] = []

                    if msg.is_multipart():
                        for part in msg.walk():
                            ctype = part.get_content_type()
                            if ctype == "text/plain" and part.get_payload(decode=True):
                                body = part.get_payload(decode=True).decode(errors="ignore")
                                urls += extract_urls(body)
                    else:
                        payload = msg.get_payload(decode=True)
                        if payload:
                            body = payload.decode(errors="ignore")
                            urls += extract_urls(body)

                    if check_if_phishing(subject, sender, urls):
                        hits.append(
                            {
                                "Subject": subject,
                                "From": sender,
                                "URLs": urls,
                            }
                        )
    finally:
        try:
            mail.logout()
        except Exception:
            pass

    return hits


def main() -> None:
    import os

    email_account = os.getenv(EMAIL_ACCOUNT_ENV)
    email_password = os.getenv(EMAIL_PASSWORD_ENV)

    if not email_account or not email_password:
        print(
            "[!] Missing credentials. Set environment variables "
            f"{EMAIL_ACCOUNT_ENV} and {EMAIL_PASSWORD_ENV}"
        )
        return

    phishing_hits = scan_emails(email_account, email_password)
    print(f"\n[*] Scan complete. Found {len(phishing_hits)} suspicious emails.\n")

    for i, hit in enumerate(phishing_hits, 1):
        print(f"--- Suspicious Email #{i} ---")
        print(f"From: {hit['From']}")
        print(f"Subject: {hit['Subject']}")
        for url in hit["URLs"]:
            print(f"→ URL: {url}")
        print()


if __name__ == "__main__":
    main()
