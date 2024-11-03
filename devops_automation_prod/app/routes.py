from flask import Blueprint, current_app, request, jsonify
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

bp = Blueprint('main', __name__)

slack_app = App(token=current_app.config['SLACK_BOT_TOKEN'])
handler = SlackRequestHandler(slack_app)

@slack_app.command('/devops')
def handle_devops_command(ack, say, command):
    ack()
    parts = command['text'].lower().split()
    if len(parts) < 2:
        say('Invalid command. Use format: /devops <tool> <task> [args]')
        return

    tool, task = parts[:2]
    args = parts[2:]

    if current_app.tool_manager.has_tool(tool):
        ai_response = current_app.ai_assistant.get_response(f'{task} using {tool}')
        result = current_app.tool_manager.execute_task(tool, task, *args)
        say(f'AI Response for {task} using {tool}:

{ai_response}

Execution result:
{result}')
    else:
        say(f'Tool \'{tool}\' not supported. Available tools: {', '.join(current_app.tool_manager.get_available_tools())}')

@bp.route('/slack/events', methods=['POST'])
def slack_events():
    return handler.handle(request)

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200
