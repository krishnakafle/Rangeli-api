# Reference from 
# https://www.alibabacloud.com/blog/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04_594319

# activate virtual env
gunicorn --bind 0.0.0.0:8010 municipalProfile.wsgi

# create service file
nano /etc/systemd/system/rangeli.service

# Add following content
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/home/user1/administrator/Rangeli/Rangeli-api
ExecStart=/home/user1/administrator/tansen/env/bin/gunicorn --workers 3 --bind localhost:9001 municipalProfile.wsgi:application

[Install]
WantedBy=multi-user.target


# Start the service

systemctl start rangeli
systemctl enable rangeli

# Check the service
systemctl status rangeli


# nginx setup

nano /etc/nginx/sites-available/rangeli_api

# copy following

server {
    listen 80;
    server_name rangeli-api.kaflekrishna.com.np;

    access_log /home/user1/administrator/Rangeli/Rangeli-api/rangeli_access.log;
    error_log /home/user1/administrator/Rangeli/Rangeli-api/rangeli_error.log;

    gzip on;
    gzip_types application/json;

    location = /favicon.ico { access_log off; log_not_found off; }
    #location /static/ {
    #    root /home/user1/administrator/Rangeli/Rangeli-api/s;
    #}

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8010;
    }
}


# link the site
ln -s /etc/nginx/sites-available/rangeli_api /etc/nginx/sites-enabled/

# restart server
systemctl restart nginx