# **DevOps Project: Deploy de imagem NGINX para o Amazon ECR via GitHub Actions**

## **Descrição do Projeto**
Este projeto demonstra um fluxo de trabalho DevOps para criar, configurar e enviar uma imagem Docker do NGINX para o Amazon Elastic Container Registry (ECR). O objetivo é automatizar o envio da imagem utilizando uma pipeline configurada no GitHub Actions, enquanto também foi disponibilizado scripts manuais para execução local.

---

## **Tecnologias Utilizadas**
- **Docker**: Para construir e gerenciar a imagem do NGINX.
- **NGINX**: Servidor web configurado para servir conteúdo estático.
- **Amazon ECR**: Serviço de registro de imagens Docker na AWS.
- **GitHub Actions**: Para automatizar o processo de construção e envio da imagem para o ECR.
- **Python**: Para gerenciar a autenticação e o push da imagem no Amazon ECR via `boto3`.
- **AWS SDK for Python (`boto3`)**: Biblioteca usada para comunicação com os serviços da AWS.

