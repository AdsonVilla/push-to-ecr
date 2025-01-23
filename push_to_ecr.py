import boto3
import os
import subprocess

AWS_REGION = "us-east-1"
ECR_REPOSITORY = "nginx-demo"

def get_aws_login():
    """Obtém credenciais de login para o Amazon ECR."""
    client = boto3.client("ecr", region_name=AWS_REGION)
    response = client.get_authorization_token()
    auth_data = response["authorizationData"][0]
    ecr_url = auth_data["proxyEndpoint"]
    token = auth_data["authorizationToken"]
    return ecr_url, token

def docker_login(ecr_url, token):
    """Realiza o login no Docker com o ECR."""
    username, password = token.split(":")
    subprocess.run(["docker", "login", "-u", username, "-p", password, ecr_url], check=True)

def push_image_to_ecr(image_name, ecr_url):
    """Tag e envia a imagem Docker para o ECR."""
    image_tag = f"{ecr_url}/{ECR_REPOSITORY}:latest"
    subprocess.run(["docker", "tag", image_name, image_tag], check=True)
    subprocess.run(["docker", "push", image_tag], check=True)

if __name__ == "__main__":
    ecr_url, token = get_aws_login()
    docker_login(ecr_url, token)
    push_image_to_ecr("nginx", ecr_url)
