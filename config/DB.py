# importing module
from env import db_url, db_name
import firebase_admin
from firebase_admin import credentials

# Fetch the service account key JSON file contents
cred = credentials.Certificate(".db-CAIF.json")

# Initialize the app with a service account, granting admin privileges
db = firebase_admin.initialize_app(cred, {
    'databaseURL': db_url
})

print("DB Connected")
