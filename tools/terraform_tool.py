import subprocess
from .base_tool import BaseTool

class TerraformTool(BaseTool):
    def get_available_tasks(self):
        return ['create_cluster', 'deploy_ingress', 'update_cluster']

    def run_terraform_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output.decode(), error.decode()

    def create_cluster(self):
        output, error = self.run_terraform_command('terraform init && terraform apply -auto-approve')
        if error:
            return f'Error creating cluster: {error}'
        return f'Cluster created successfully: {output}'

    def deploy_ingress(self):
        output, error = self.run_terraform_command('terraform apply -target=kubernetes_ingress.example -auto-approve')
        if error:
            return f'Error deploying ingress: {error}'
        return f'Ingress resources deployed successfully: {output}'

    def update_cluster(self):
        output, error = self.run_terraform_command('terraform apply -auto-approve')
        if error:
            return f'Error updating cluster: {error}'
        return f'Cluster updated successfully: {output}'
