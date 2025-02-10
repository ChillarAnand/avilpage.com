<!--
.. title: Free DockerHub Alternative - ECR Public Gallery
.. slug: free-dockerhub-alternative-ecr-gallery
.. date: 2025-02-09 21:38:34 UTC+05:30
.. tags: docker, devops
.. category: DevOps
.. link: 
.. description: Free Docker alternative without rate limits & without auth - AWS ECR Public Gallery
.. type: text
-->

![docker-rate-limits](/images/docker-rate-limits.png)

DockerHub started rate limiting[^rate] anonymous docker pulls. When testing out a new CI/CD setup, I hit the rate limit and had to wait for an hour to pull the image. This was a good time to look for alternatives.

[AWS ECR Public Gallery](https://gallery.ecr.aws/)[^ecr] is a good alternative to DockerHub as of today(2025 Feb). It is free and does not have rate limits even for anonymous users. 

![public-ecr-gallery](/images/public-ecr-gallery.png)

Once we find the required image from the gallery, we can simply change the image name in the `docker pull` command to pull the image from ECR Gallery.

```bash
docker pull public.ecr.aws/ubuntu/ubuntu
```

In `Dockerfile`, we can use the image from ECR Gallery as follows:

```Dockerfile
FROM public.ecr.aws/ubuntu/ubuntu
```

That is a quick way to avoid DockerHub rate limits.

[^rate]: [DockerHub Limits](https://docs.docker.com/docker-hub/usage/)
[^ecr]: [AWS ECR Public Gallery](https://gallery.ecr.aws)
