import os

class Config:
    SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
    SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
