<!--
.. title: How To Deploy Django Channels To Production
.. slug: deploying-scaling-django-channels
.. date: 2018-05-18 21:21:21 UTC+05:30
.. tags: python, django, devops
.. category:
.. link:
.. description:
.. type: text
-->

In this article, we will see how to deploy [django channels](https://pypi.org/project/channels/) to production and how we can scale it to handle more load. We will be using nginx as proxy server, [daphne](https://pypi.org/project/daphne/) as ASGI server, gunicorn as WSGI server and redis for channel back-end.

Daphne can serve HTTP requests as well as WebSocket requests. For stability and performance, we will use uwsgi/gunicorn to serve HTTP requests and daphne to serve websocket requests.

We will be using systemd to create and manage processes instead of depending on third party process managers like supervisor or circus. We will be using ansible for managing deployments. If you don't want to use ansible, you can just replace template variables in the following files with actual values.


### Nginx Setup

Nginx will be routing requests to WSGI server and ASGI server based on URL. Here is nginx configuration for server.

```conf
server {
    listen {{ server_name }}:80;
    server_name {{ server_name }} www.{{ server_name }};

    return 301 https://avilpage.com$request_uri;
}


server {
    listen {{ server_name }}:443 ssl;
    server_name {{ server_name }} www.{{ server_name }};

    ssl_certificate     /root/certs/avilpage.com.chain.crt;
    ssl_certificate_key /root/certs/avilpage.com.key;

    access_log /var/log/nginx/avilpage.com.access.log;
    error_log /var/log/nginx/avilpage.com.error.log;

    location / {
            proxy_pass http://0.0.0.0:8000;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_redirect off;
    }

    location /ws/ {
            proxy_pass http://0.0.0.0:9000;
            proxy_http_version 1.1;

            proxy_read_timeout 86400;
            proxy_redirect     off;

            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $server_name;
    }

    location /static {
        alias {{ project_root }}/static;
    }

    location  /favicon.ico {
        alias {{ project_root }}//static/img/favicon.ico;
    }

    location  /robots.txt {
        alias {{ project_root }}/static/txt/robots.txt;
    }

}
```

### WSGI Server Setup

We will use gunicorn for wsgi server. We can run gunicorn with

```sh
$ gunicorn avilpage.wsgi --bind 0.0.0.0:8000 --log-level error --log-file=- --settings avilpage.production_settings
```

We can create a systemd unit file to make it as a service.

```conf
[Unit]
Description=gunicorn
After=network.target


[Service]
PIDFile=/run/gunicorn/pid
User=root
Group=root
WorkingDirectory={{ project_root }}
Environment="DJANGO_SETTINGS_MODULE={{ project_name }}.production_settings"
ExecStart={{ venv_bin }}/gunicorn {{ project_name}}.wsgi --bind 0.0.0.0:8000 --log-level error --log-file=- --workers 5 --preload


ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
Restart=on-abort
PrivateTmp=true


[Install]
WantedBy=multi-user.target
```

Whenever server restarts, systemd will automatically start gunicorn service. We can also restart gunicorn manually with

```sh
$ sudo service gunicorn restart
```


### ASGI Server Setup

We will use daphne for ASGI server and it can be started with

```sh
$ daphne avilpage.asgi:application --bind 0.0.0.0 --port 9000 --verbosity 1
```

We can create a systemd unit file like the previous one to create a service.

```
[Unit]
Description=daphne daemon
After=network.target


[Service]
PIDFile=/run/daphne/pid
User=root
Group=root
WorkingDirectory={{ project_root }}
Environment="DJANGO_SETTINGS_MODULE={{ project_name }}.production_settings"
ExecStart={{ venv_bin }}/daphne --bind 0.0.0.0 --port 9000 --verbosity 0 {{project_name}}.asgi:application
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
Restart=on-abort
PrivateTmp=true


[Install]
WantedBy=multi-user.target
```

### Deployment

Here is [an ansible playbook](https://github.com/ChillarAnand/eddie/blob/master/ubuntu/config/playbooks/django_setup.yml) which is used to deploy these config files to our server. To run the playbook on server `avilpage.com`, execute

```sh
$ ansible-playbook -i avilpage.com, django_setup.yml
```


### Scaling

Now that we have deployed channels to production, we can do performance test to see how our server performs under load.

For WebSockets, we can use [Thor](https://www.npmjs.com/package/thor) to run performance test.

```sh
thor -C 100 -A 1000 wss://avilpage.com/ws/books/
```

Our server is able to handle `100 requests per second` with a `latency of 800ms`. This is good enough for low traffic website.

To improve performance, we can use unix sockets instead of rip/port for gunicorn and daphne. Also, daphne has support for multiprocessing using [shared file descriptors](). Unfortunately, it doesn't work as expected. As [mentioned here](https://github.com/django/daphne/issues/182#issuecomment-387507887), we can use systemd templates and spawn multiple daphne process.

An alternate way is to use [uvicorn](https://pypi.org/project/uvicorn/) to start multiple workers. Install uvicorn using pip

```sh
$ pip install uvicorn
```

Start uvicorn ASGI server with

```
$ uvicorn avilpage.asgi --log-level critical --workers 4
```
This will spin up 4 workers which should be able to handle more load. If this performance is not sufficient, we have to setup a load balancer and spin up multiple servers(just like scaling any other web application).
