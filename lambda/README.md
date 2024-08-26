#Create a Lambda function from an ECR

Dockerfile de uma imagem Python de imagem base da AWS, subir em um repositório do ECR e criar uma Lambda utilizando o imagem de contêiner armazenada no ECR.

```
docker build --platform linux/amd64 -t meu-app:latest .
```

Após acessar sua conta AWS, navegue até o serviço "ECR" clicando em "Serviços" na seção "Contêineres"  e selecionando "Elastic Container Registry"
- Criar repositório
- Para realizar o upload da imagem Docker no Amazon ECR
- Importante: É necessário ter configurado o AWS-CLI com suas credenciais de acesso. Segue link da documentação de configuração do AWS-CLI.
- Execute o Docker Push

Crie uma função Lambda a partir de uma imagem do ECR
- Navegue até o serviço do Lambda clicando em "Serviços" na seção "Compute" (Computação) e selecionando "Lambda"
- Crie uma lambda
- Selecione:
   - Imagem de contêiner
   - Nome da função:
   - URI da imagem de contêiner, sele a URI do seu container
   - Arquitetura certifique que esteja em x86_64
