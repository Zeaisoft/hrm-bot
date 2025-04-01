from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from app.hrm_logic import HRM

whatsapp_bp = Blueprint("whatsapp", __name__)

@whatsapp_bp.route("/", methods=["GET"])
def home():
    return "HRM Chatbot is running!"

@whatsapp_bp.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get("Body", "").strip()
    response = MessagingResponse()
    
    # Process the incoming message
    reply = HRM.process_command(incoming_msg)
    response.message(reply)

    return str(response)
