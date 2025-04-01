# app/database.py
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with Firestore credentials
cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_firestore_connection():
    # Return the Firestore client
    return db

def add_employee(name, role):
    # Add an employee to Firestore
    doc_ref = db.collection("employees").document(name)
    doc_ref.set({"name": name, "role": role})
    return f"Employee {name} added as {role}."

def remove_employee(name):
    # Remove an employee from Firestore
    db.collection("employees").document(name).delete()
    return f"Employee {name} removed."
