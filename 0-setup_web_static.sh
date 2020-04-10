#!/usr/bin/env bash
# Bash script that setup the web servers for the deployment of web_static
# Install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
# Create folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
# Create html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create Symbolic link between test and current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Set user:group ubuntu ownership of the /data/ directory
sudo chown -R ubuntu:ubuntu /data/
# Nginx Configuration
echo "server {
	listen 80;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	add_header X-Served-By $HOSTNAME;

	error_page 404 /404.html;

	location = /404.html {
		 internal;
	}

	location /redirect_me {
		 return 301 https://cathedraldigilab.com;
	}

	location /hbnb_static {
		alias /data/web_static/current;
	}
}" > /etc/nginx/sites-enabled/default
# Reload Nginx service
sudo service nginx restart
