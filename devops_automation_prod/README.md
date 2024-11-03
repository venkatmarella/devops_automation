# DevOps Automation System

This project is a modular DevOps automation system that integrates with Slack and uses AI to assist with various DevOps tasks.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```
   export SLACK_BOT_TOKEN=your_slack_bot_token
   export SLACK_SIGNING_SECRET=your_slack_signing_secret
   export OPENAI_API_KEY=your_openai_api_key
   ```

3. Run the Flask app:
   ```
   python run.py
   ```

## Deploying to Production

To deploy the Flask app to production, you can use Gunicorn as the WSGI server:

1. Install Gunicorn:
   ```
   pip install gunicorn
   ```

2. Run the app with Gunicorn:
   ```
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

This will start the app with 4 worker processes, binding to all network interfaces on port 8000.
