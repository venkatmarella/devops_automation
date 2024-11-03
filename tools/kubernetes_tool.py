from kubernetes import client, config
from .base_tool import BaseTool

class KubernetesTool(BaseTool):
    def __init__(self):
        config.load_kube_config()
        self.apps_v1 = client.AppsV1Api()

    def get_available_tasks(self):
        return ['create_deployment', 'scale_deployment']

    def create_deployment(self, name, image, replicas=1):
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1DeploymentSpec(
                replicas=int(replicas),
                selector=client.V1LabelSelector(
                    match_labels={'app': name}
                ),
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={'app': name}
                    ),
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name=name,
                                image=image
                            )
                        ]
                    )
                )
            )
        )
        
        try:
            self.apps_v1.create_namespaced_deployment(namespace='default', body=deployment)
            return f'Deployment {name} created successfully'
        except Exception as e:
            return f'Error creating deployment: {str(e)}'

    def scale_deployment(self, name, replicas):
        try:
            self.apps_v1.patch_namespaced_deployment_scale(
                name=name,
                namespace='default',
                body={'spec': {'replicas': int(replicas)}}
            )
            return f'Deployment {name} scaled to {replicas} replicas'
        except Exception as e:
            return f'Error scaling deployment: {str(e)}'
