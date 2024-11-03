import importlib
import os

class ToolManager:
    def __init__(self):
        self.tools = {}
        self.load_tools()

    def load_tools(self):
        tools_dir = os.path.join(os.path.dirname(__file__), 'tools')
        for filename in os.listdir(tools_dir):
            if filename.endswith('_tool.py'):
                tool_name = filename[:-8]
                module_name = f'app.tools.{filename[:-3]}'
                try:
                    module = importlib.import_module(module_name)
                    tool_class = getattr(module, f'{tool_name.capitalize()}Tool')
                    self.tools[tool_name] = tool_class()
                except (ImportError, AttributeError) as e:
                    print(f'Error loading tool {tool_name}: {e}')

    def has_tool(self, tool_name):
        return tool_name in self.tools

    def get_available_tools(self):
        return list(self.tools.keys())

    def execute_task(self, tool_name, task_name, *args, **kwargs):
        if tool_name in self.tools:
            tool = self.tools[tool_name]
            if hasattr(tool, task_name):
                return getattr(tool, task_name)(*args, **kwargs)
            else:
                return f'Task \'{task_name}\' not found in {tool_name} tool'
        else:
            return f'Tool \'{tool_name}\' not found'
