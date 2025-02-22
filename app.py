server {
    listen 80;
    server 3.109.158.27;

    location / {
        proxy_pass http://127.0.0.1:5000;
       

