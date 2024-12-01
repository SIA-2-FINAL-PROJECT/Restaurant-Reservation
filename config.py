import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Base configuration class."""
    API_TITLE = "Travel Booking API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    # SSL settings for database (if applicable)
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'ssl': {
                'ca': os.path.join(os.getcwd(), 'app/certs/ca.pem')
            }
        }
    }
