import requests
import jwt
import datetime
import logging

AUTH_API_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"
SECRET_KEY = "your_secret_key"  # Replace with a secure secret key

logger = logging.getLogger(__name__)

def authenticate_user(email, password):
    """
    Authenticates the user against the given authentication API.
    """
    try:
        # Send the POST request
        response = requests.post(AUTH_API_URL, json={"email": email, "password": password}, timeout=10)
        logger.debug(f"Raw response: {response.text}")

        # Ensure the response is valid JSON
        try:
            user_details = response.json()
        except ValueError:
            logger.error("Response is not valid JSON.")
            return None

        # Handle specific response format
        if isinstance(user_details, list) and len(user_details) == 2:
            if user_details[0] == "Verified" and user_details[1] == "True":
                # Assign roles based on email
                role = "admin" if email == "grace@plymouth.ac.uk" else "user"
                user_id = 1 if role == "admin" else 2  # Example UserID for admin and non-admin
                logger.info(f"Authentication successful. Role: {role}")
                return generate_jwt(email, role, user_id)
            else:
                logger.info("Authentication failed: Invalid credentials.")
                return None

        # Handle unexpected cases
        logger.warning("Unexpected response format from the API.")
        return None
    except requests.RequestException as e:
        logger.error(f"Error connecting to Authenticator API: {e}")
        return None

def generate_jwt(email, role, user_id):
    logger.debug(f"Generating JWT for email: {email}, role: {role}, user_id: {user_id}")
    payload = {
        "user_id": user_id,
        "email": email,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None