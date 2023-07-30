# Docker Commands

- Download docker images
```
docker pull <image-name>
```
- Docker images list
```
docker images -a 
docker images list
```
- Docker container from an image
```
docker run -it <image-name>
```
- Giving a name to container when run
```
docker run --name <container_name> -it <image_name>
```
- Show running docker containers
```
docker ps -a
```
- Run another shell of existing container
```
docker exec -it (container_id/ name) bash
```
- Running container with  GUI enabled in windows
```
docker run --name <container_name> -e DISPLAY=host.docker.internal:0.0 -it <image_name>
```
- Stop a docker container
```
docker stop <container_name>
```
- Remove a single container
```
docker rm <container_name>
```
- Building image from a docker file
```
docker build -t <image_name> .
```
The above command by default looks for the file named 'dockerfile'
```
docker build -f <dockerfile_name> -t <image_name> .
```
