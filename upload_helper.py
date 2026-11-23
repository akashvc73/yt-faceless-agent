#!/usr/bin/env python3
"""
Simple YouTube upload helper using the official Google API.
Requires:
- client_secrets.json
- authorized credentials (token.json after first run)
- google-api-python-client, google-auth-oauthlib, google-auth-httplib2

Install once:
pip install --upgrade google-api-python-client google-auth-oauthlib google-auth-httplib2
"""

import os
import argparse
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

def upload_video(file_path, title, description, tags, category_id="27", privacy="private"):
    youtube = get_authenticated_service()
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id  # 27 = Education
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False
        }
    }
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")
    print("Upload complete. Video ID:", response.get("id"))
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", default="")
    parser.add_argument("--tags", default="")
    parser.add_argument("--privacy", default="private")
    args = parser.parse_args()
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    upload_video(args.file, args.title, args.description, tags, privacy=args.privacy)
