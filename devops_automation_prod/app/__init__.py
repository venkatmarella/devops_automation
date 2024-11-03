from flask import Flask
from config import Config
from app.tool_manager import ToolManager
from app.ai_assistant import AIAssistant

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.tool_manager = ToolManager()
    app.ai_assistant = AIAssistant(app.config['OPENAI_API_KEY'])

    from app import routes
    app.register_blueprint(routes.bp)

    return app
