from google.oauth2 import credentials
import os.path

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
GCP_PROJECT = "dotmodus-training"
AUTH_TOKEN = os.getenv("AUTH_JSON")

print(AUTH_TOKEN)

credentials.Credentials.from_authorized_user_file(AUTH_TOKEN, scopes= SCOPES)

