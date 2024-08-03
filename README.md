# Docker Questions

This document provides detailed instructions and scripts for various Docker operations.

## 1. What is the relation between an image and a container in Docker?

In Docker:
- **Image:** A Docker image is a blueprint for creating customers. It includes the application code, runtime environment, libraries and other dependencies required to run an application.
- **Container:** A Docker container is a running instance of a Docker image. It is an isolated environment where the application defined in the image runs. Containers share the host system Kernal but have their own file system, network and process space.

### Differences Between an Image and a Container

| Feature          | Image                                     | Container                                |
|------------------|-------------------------------------------|------------------------------------------|
| **Definition**   | Blueprint for creating containers         | Running instance of an image              |
| **Resource**     | No isolated resources                     | Has isolated resources                    |
| **Execution**    | Not executable on its own                 | Runs applications and processes           |
| **Persistence**  | Does not maintain state                   | Maintains state during runtime            |
| **Lifecycle**    | Created once, can be reused               | Started, stopped, and deleted             |


## 2. List all the images and the containers in the system.

- **List Docker images:**

  ```bash
  docker images
  ```

- **List Docker Containers:**

  ```bash
  docker ps -a
  ```

## 3. Pull the latest image of `nginx` and run it

- **Pull the latest `nginx` image:**

  ```bash
  docker pull nginx:latest
  ```

- **Run the `nginx` container:**

  ```bash
  docker run -d --name super-nginx -p 7001:80 -e NGINX_HOST=vunet.local nginx
  ```

## 4. Get the list of all running containers and stop and remove the `nginx` container

- **List all running containers:**

  ```bash
  docker ps
  ```

- **Stop the `nginx` container:**

  ```bash
  docker stop super-nginx
  ```

- **Remove the `nginx` container:**

  ```bash
  docker rm super-nginx
  ```

## 5. Create a Docker volume named `vunet` and run `nginx` again, attaching the volume to `/etc/` in the container

- **Create a Docker volume:**

  ```bash
  docker volume create vunet
  ```

- **Run the `nginx` container with the volume attached to /etc/:**

  ```bash
  docker run -d --name super-nginx -p 7001:80 -v vunet:/etc/ nginx
  ```

## 6. Stop and remove the `nginx` container and remove the volume `vunet`

- **Stop the `nginx` container:**

  ```bash
  docker stop super-nginx
  ```

- **Remove the `nginx` container:**

  ```bash
  docker rm super-nginx
  ```

- **Remove the volume `vunet`:**

  ```bash
  docker volume rm vunet
  ```

## 7. Create a Dockerfile

- **Create a `Dockerfile`:**

  ```Dockerfile
  FROM ubuntu:latest

  RUN apt-get update && \
      apt-get install -y python3.10 python3-pip

  COPY server.py /usr/src/app/app.py

  WORKDIR /usr/src/app

  ENTRYPOINT ["python3", "app.py"]
  ```

- **Python script (`app.py`):**

  ```python
  import http.server
  import socketserver
  from http import HTTPStatus

  class Handler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(HTTPStatus.OK)
          self.end_headers()
          self.wfile.write(b'Hello world')

  httpd = socketserver.TCPServer(('', 8000), Handler)
  print("Serving Http Requests on 8000...")
  httpd.serve_forever()
  ```

## 8. Run a container using the image created

- **Build the Docker image:**

  ```bash
  docker build -t abhishek_container .
  ```

- **Run the container using the image:**

  ```bash
  docker run -d --name abhishek_container -p 8000:8000 python-server
  ```

## 9. Check if the container is running and has the Python process running

- **Check the running container:**

  ```bash
  docker ps
  ```

  Yes the python process is running as `app.py` is listed.

- **Check the Python process inside the container:**

  ```bash
  docker exec -it abhishek_container ps aux
  ```

## 10. Why are Docker networks used? Create a Docker network named `vunet`

- **Purpose of Docker networks:**

  Docker networks are used to manage communication between containers, isolate network traffic, and configure network settings. They enable containers to communicate with each other and with external systems securely and efficiently. Conceptually, a network is a virtual switch. It can be a local (to a single Engine) or global (across multiple hosts).

- **Create a Docker network named `vunet`:**

  ```bash
  docker network create vunet
  ```

## 11. Create an Nginx cluster by attaching the created network, `vunet`, to it

- **Run Nginx containers in the `vunet` network:**

  ```bash
  docker run -d --name abhishek_nginx --network vunet nginx
  ```
