# Usar a imagem base do NGINX
FROM nginx:1.27.3-alpine

# Copiar o arquivo de configuração para o diretório padrão do NGINX
COPY nginx.conf /etc/nginx/nginx.conf

# Expor a porta padrão do NGINX
EXPOSE 80
