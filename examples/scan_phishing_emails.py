import imaplib
import email
import re
import os
from email.header import decode_header
from urllib.parse import urlparse

# CONFIGURATION
EMAIL_ACCOUNT = "lumberjackattack904@gmail.com"
EMAIL_PASSWORD = "qpil jfnm pevb kquk"  # Use App Password if 2FA is enabled
IMAP_SERVER = "imap.gmail.com"
FOLDER = "INBOX"
PHISHING_DOMAINS = [
    "ssaib.uk.com", "daydarylmann.com", "tinyurl.com"
]
PHISHING_KEYWORDS = [
    "icloud locked", "payment issue", "apple support", "account suspended", "update payment"
]

def clean_subject(subject):
    if isinstance(subject, bytes):
        try:
            return decode_header(subject)[0][0].decode()
        except:
            return subject.decode('utf-8', errors='ignore')
    return subject

def extract_urls(text):
    return re.findall(r'https?://[^\s<>"]+', text)

def check_if_phishing(subject, sender, urls):
    subject = subject.lower()
    if any(keyword in subject for keyword in PHISHING_KEYWORDS):
        return True
    for domain in PHISHING_DOMAINS:
        if domain in sender or any(domain in url for url in urls):
            return True
    return False

def scan_emails():
    print("[*] Connecting to email server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select(FOLDER)

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    phishing_hits = []

    for i in email_ids[::-1][:500]:  # Limit to latest 500 emails
        res, msg_data = mail.fetch(i, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = clean_subject(msg["subject"])
                sender = msg.get("from", "")
                urls = []

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode(errors='ignore')
                            urls += extract_urls(body)
                else:
                    body = msg.get_payload(decode=True).decode(errors='ignore')
                    urls += extract_urls(body)

                if check_if_phishing(subject, sender, urls):
                    phishing_hits.append({
                        "Subject": subject,
                        "From": sender,
                        "URLs": urls
                    })

    print(f"\n[*] Scan complete. Found {len(phishing_hits)} suspicious emails.\n")
    for i, hit in enumerate(phishing_hits, 1):
        print(f"--- Suspicious Email #{i} ---")
        print(f"From: {hit['From']}")
        print(f"Subject: {hit['Subject']}")
        for url in hit["URLs"]:
            print(f"→ URL: {url}")
        print()

if __name__ == "__main__":
    scan_emails()
