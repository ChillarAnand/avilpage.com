<!--
.. title: Migrating from Nginx to Caddy
.. slug: migrating-from-nginx-to-caddy
.. date: 2025-05-30 21:21:21 UTC+05:30
.. tags: devops, automation
.. category: programming
.. link: 
.. description: How to migrate from Nginx to Caddy for web server management?
.. type: text
-->

When deploying web apps in production, a web server is essential for serving static files, handling reverse proxying, 
and managing SSL/TLS certificates. 

I have been using Nginx for a long time, but I have recently switched to Caddy as it provides automatic HTTPS by default.
In addition, Caddy has a simpler configuration syntax and is easier to set up for basic use cases.


### Nginx vs Caddy

To illustrate the differences, here are some examples of how to configure a simple web server in both Nginx and Caddy.

#### Nginx Configuration

```nginx
server {
    listen 80;
    server_name avilpage.com;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }

    location /api {
        proxy_pass http://localhost:3000;
    }
}
```

With Nginx, you need to manually handle SSL/TLS certificates, which can be cumbersome. 
You typically use tools like Certbot to obtain and renew certificates.

#### Caddy Configuration

```caddyfile
avilpage.com {
    root * /var/www/html
    file_server

    reverse_proxy /api localhost:3000
}
```

Caddy automatically manages SSL/TLS certificates for you, so you don't need to worry about obtaining or renewing them.
It also provides default redirection from HTTP to HTTPS, making it easier to secure your site.


### Conclusion

Caddy's automatic HTTPS and simpler configuration syntax make it a compelling choice for web servers, 
especially for those who want to get started quickly without dealing with the complexities of SSL/TLS management.