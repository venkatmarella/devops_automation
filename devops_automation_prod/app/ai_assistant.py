import openai

class AIAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, task):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a DevOps AI assistant.'},
                {'role': 'user', 'content': f'Provide steps to {task}'}
            ]
        )
        return response.choices[0].message.content
