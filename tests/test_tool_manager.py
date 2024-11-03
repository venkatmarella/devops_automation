import unittest
from unittest.mock import patch, MagicMock
from tool_manager import ToolManager

class TestToolManager(unittest.TestCase):
    def setUp(self):
        self.tool_manager = ToolManager()

    @patch('os.listdir')
    @patch('importlib.import_module')
    def test_load_tools(self, mock_import, mock_listdir):
        mock_listdir.return_value = ['terraform_tool.py', 'kubernetes_tool.py']
        mock_import.side_effect = [
            MagicMock(TerraformTool=MagicMock()),
            MagicMock(KubernetesTool=MagicMock())
        ]
        
        self.tool_manager.load_tools()
        
        self.assertEqual(len(self.tool_manager.tools), 2)
        self.assertIn('terraform', self.tool_manager.tools)
        self.assertIn('kubernetes', self.tool_manager.tools)

    def test_has_tool(self):
        self.tool_manager.tools = {'terraform': MagicMock()}
        self.assertTrue(self.tool_manager.has_tool('terraform'))
        self.assertFalse(self.tool_manager.has_tool('nonexistent'))

    def test_get_available_tools(self):
        self.tool_manager.tools = {'terraform': MagicMock(), 'kubernetes': MagicMock()}
        available_tools = self.tool_manager.get_available_tools()
        self.assertEqual(set(available_tools), {'terraform', 'kubernetes'})

    def test_execute_task(self):
        mock_tool = MagicMock()
        mock_tool.test_task.return_value = 'Task executed'
        self.tool_manager.tools = {'test_tool': mock_tool}
        
        result = self.tool_manager.execute_task('test_tool', 'test_task', 'arg1', 'arg2')
        
        self.assertEqual(result, 'Task executed')
        mock_tool.test_task.assert_called_once_with('arg1', 'arg2')

if __name__ == '__main__':
    unittest.main()
