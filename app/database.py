import firebase_admin
from firebase_admin import credentials, firestore

# Firebase credentials directly in the code
firebase_config = {
    "type": "service_account",
    "project_id": "hrmbot-3e3a7",
    "private_key_id": "fe936fd68b33fcad9db4a57a814eea43a52460ef",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDDbbO8fznWfa/n
hiBlM6Ninh/l5me/TEHHRmyrKmSfcdCVVDfyqfBg6/HGV//CydAAVGYCW8OVM0Kc
qlG47J/LRIeGwFu4sIlbzWBsWc6zbK6IVDV7pY6oqHGzKTONGsoknIn2XsdBjJzN
zV5bETTbuz8hNrGSjJ3ew6M//vthwiWTy6i533D3QeKmvzEdtRs3/PjxhjMK+hUk
BNNZM5nJNDVsac25nQUT8M0Kk5YqrlqnQahwI6au/AYviPuMpjIpTRJuBpVEA/7K
Lrl257kVjJTho+sUgrDFHWE7jL8QlS2jH0BIH0fim+C07nBRiYUap61fojDmzroy
LgNR+Ps9AgMBAAECggEAF83Q9XDPFrU7K97xKzfdpYbP09emDhhicBIVQnQTdZMO
GQz9E5hnfdFqIwKtAIjxxliBZGAmXpIJLGlX3Z0qND7QqIqITDgUmGitCgWWYScn
yytBUyJDUip8+ZmsfHoljSK+xeedgE/O+bJo1SbaDWRYDYT1SX3J7PcKIiK+HpX/
ftrUG/z6MGWiQbv4x0r7yElsbIkiKxe6a2OadAOflcd1ufi/YzDT9ioWPKHVU7Ag
bQoGIgu0vPLOXVjd0X0Mi0CimkXhDcM7hC9oUUJZJTBDk/v4GIT4usgaqx/fXeA/
q1WyYw3JXFXkQcaGoU1k1qGKntnNH8J8RObLeFY58QKBgQDoIWluJFfwWvTwo9gJ
dIpcJ+kJoQ1uXFIUGXLIhNyEWA5Zkdqn6YvUIMmEXj079jLG/q7EE6IF1zYqYkra
KIsr9sHSBVEtpLIjZqXZ+Fty7OHk4GQJnPES2LtkiF8wc38vp5FcK6lV4BuGpXAS
JiKIIdC1Big9p0Cj7mIEkSXQYwKBgQDXhiZFT9bsEDoL0MKktm4UQ0PNbcwl0vvO
fD7Q/QXwfud9I4NCgZjO5GvbYPNNPi9rNquBVBv8U6lGT208NgwfHc+FgBUfKCPv
azkcXLmxXw3dUmDjaxd0y/y6tEsx5erXV3FmoZuPbJx36s1qtBphXr6OosuJJ7U1
+BmiVd9H3wKBgQDbnsj2KTJ+OEAn8Iw0HevN1wC3WIWxlW0ekRk1N+a+2+Tvv3wl
g2QFFeQy9UpwEbXm6g0FfCG97ujTXt2828EYnkSwZNFyIrFbpwFhYYV8DTyH4/kh
0zeOgjmBmzicSZnax2pSzwhONFM2qA2JTkU7kOq6apHmCviwYJiiA4XISwKBgDRn
UuDhg9GMNIDw9pLUJLnajR7jBpNf1IglX6SzEQGj6adcviqqljwgADWsQhxS9Xat
KVBd4hwdP3hwEZBlV9ctCWtddEVKHkq1mIJT7Xa6NQXOZO6G+IIWo1HGSs5MKCjK
AzHAM7HQ586kkePS/OMWBWFrJfAoboA73gfBt3OjAoGBAN25mva0yKd61WIUy/98
s8/QkDo4iQqz5gBLGdJ8i7XUubo9rIGtiQaa+3llHoQL//xUWNMAtUg/LBn2Asmu
z6aPXiB3UwkC/DuM/KbzjCOcerXUI2W1UmDl5G/OIBl9dUC47q1SQ4EyHXPKqnxG
aIHHio05zgXTRP6eHUY19SBy
-----END PRIVATE KEY-----""",
    "client_email": "firebase-adminsdk-fbsvc@hrmbot-3e3a7.iam.gserviceaccount.com",
    "client_id": "102620939342126479045",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40hrmbot-3e3a7.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

try:
    # Initialize Firebase
    cred = credentials.Certificate(firebase_config)

    if not firebase_admin._apps:  # Prevent multiple initializations
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    print("Firebase initialized successfully.")

except firebase_admin.exceptions.FirebaseError as fe:
    raise RuntimeError(f"Firebase SDK Initialization Error: {fe}")
except Exception as e:
    raise RuntimeError(f"Unexpected error occurred while initializing Firebase: {e}")
