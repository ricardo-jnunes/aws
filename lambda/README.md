#Create a Lambda function from an ECR

Dockerfile de uma imagem Python de imagem base da AWS, subir em um repositório do ECR e criar uma Lambda utilizando o imagem de contêiner armazenada no ECR.

```
docker build --platform linux/amd64 -t meu-app:latest .
```
