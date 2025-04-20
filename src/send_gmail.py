#!/usr/bin/env python
# coding: utf-8

# In[1]:


import base64
import logging
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

import os

import config


# In[4]:


# Configure logging using the path from config.py
logging.basicConfig(
    level=logging.INFO,
    filename=config.SEND_GMAIL_LOG,
    filemode="a",  # Append mode
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Path to OAuth credentials JSON file
CREDENTIALS_FILE = config.CREDENTIALS_FILE

# Gmail API Scope
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
TOKEN_PATH = "token.pickle"

def authenticate_gmail():
    creds = None

    # Check if token.pickle exists
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token:
            creds = pickle.load(token)

    # If credentials are invalid or expired, refresh or re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the new token for future use
        with open(TOKEN_PATH, "wb") as token:
            pickle.dump(creds, token)

    return creds

def send_gmail(job_title, recruiter_email):
    """Sends a follow-up email using Gmail API and logs the process."""
    logging.info(f"Preparing to send email for job: {job_title} to {recruiter_email}")

    if recruiter_email == "N/A":
        logging.warning("No recruiter email found. Skipping email sending.")
        return

    try:
        creds = authenticate_gmail()
        service = build("gmail", "v1", credentials=creds)
        logging.info("Gmail API service built successfully.")

        email_subject = f"Follow-up on my application for {job_title}"
        email_body = f"""
        Dear Hiring Manager,

        I hope you’re doing well. I recently applied for the {job_title} position and wanted to follow up to express my continued interest. 
        I am very excited about the opportunity to bring my skills in {job_title.split()[0]} development and contribute to your team.

        Please let me know if you need any further information from me. I look forward to hearing about the next steps.

        Best regards,  
        Anugya
        fnu.anugya@gmail.com
        """

        message = MIMEText(email_body)
        message["to"] = recruiter_email
        message["subject"] = email_subject
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        logging.info("Attempting to send email via Gmail API...")
        send_message = (
            service.users().messages().send(userId="me", body={"raw": encoded_message}).execute()
        )
        logging.info(f"Email sent successfully to {recruiter_email} (Message ID: {send_message['id']})")

    except Exception as e:
        logging.error(f"Error sending email: {e}")

# Example Usage
if __name__ == "__main__":
    send_gmail("Python Developer", "xyz@gmal.com")
