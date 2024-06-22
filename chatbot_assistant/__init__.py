#!/usr/bin/env/python3

from flask import Blueprint, request
from flask_socketio import SocketIO
from dotenv import load_dotenv

load_dotenv()
socketio = SocketIO()

# chat_view = Blueprint("chat_view", __name__, url_prefix="/api/v1")
from flask import Flask
from flask_cors import CORS
import os

def create_app():
    """
    manufacture app qith necesarry dependencies initialized
    """
    print("OPENAI_API_KEYyy:", os.getenv("OPENAI_API_KEY"))

    app = Flask(__name__)
    socketio.init_app(app)

    from chatbot_assistant.chat_app import chat_view
    app.register_blueprint(chat_view)

    CORS(
        app,
        resources={r"/api/v1/*": {"origins": "*"}}
    )

    app.config.from_object("config.ConfigClass")
    print(f"DEBUG: {app.config['DEBUG']}")
    print(f"KEY: {app.config['SECRET_KEY']}")

    return app
