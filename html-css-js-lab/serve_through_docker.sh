RELPATH=$1

docker stop docker-nginx 
docker rm docker-nginx
docker run --restart unless-stopped --name docker-nginx -p 80:80 -d -v $RELPATH:/usr/share/nginx/html nginx
