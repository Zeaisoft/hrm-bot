from flask import Flask
from app.routes import whatsapp_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(whatsapp_bp)  # Register the WhatsApp routes
    return app
