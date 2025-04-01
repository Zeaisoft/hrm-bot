import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Load Firebase credentials from an environment variable
firebase_credentials = os.environ.get("FIREBASE_CREDENTIALS")

if firebase_credentials:
    cred_dict = json.loads(firebase_credentials)  # Convert string to dict
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("FIREBASE_CREDENTIALS environment variable not set")

db = firestore.client()
