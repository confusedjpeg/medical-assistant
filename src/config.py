import os

class Config:
    """Configuration settings for the medical assistant application."""
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/medical_assistant')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API keys
    NIH_API_KEY = os.getenv('NIH_API_KEY', 'your_nih_api_key')
    DRUGBANK_API_KEY = os.getenv('DRUGBANK_API_KEY', 'your_drugbank_api_key')
    OPENFDA_API_KEY = os.getenv('OPENFDA_API_KEY', 'your_openfda_api_key')

    # Other configurations
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')