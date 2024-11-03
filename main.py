import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from tool_manager import ToolManager
from ai_assistant import AIAssistant

app = App(token=os.environ['SLACK_BOT_TOKEN'])
tool_manager = ToolManager()
ai_assistant = AIAssistant(os.environ['OPENAI_API_KEY'])

@app.command('/devops')
def handle_devops_command(ack, say, command):
    ack()
    parts = command['text'].lower().split()
    if len(parts) < 2:
        say('Invalid command. Use format: /devops <tool> <task> [args]')
        return
    tool, task = parts[:2]
    args = parts[2:]
    if tool_manager.has_tool(tool):
        ai_response = ai_assistant.get_response(f'{task} using {tool}')
        result = tool_manager.execute_task(tool, task, *args)
        say(f'AI Response for {task} using {tool}:

{ai_response}

Execution result:
{result}')
    else:
        say(f'Tool \'{tool}\' not supported. Available tools: {', '.join(tool_manager.get_available_tools())}')

@app.event('app_mention')
def handle_mention(event, say):
    say('I\'m here to help with DevOps tasks. Use /devops command with a specific tool and task.')

if __name__ == '__main__':
    handler = SocketModeHandler(app, os.environ['SLACK_APP_TOKEN'])
    handler.start()
