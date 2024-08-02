# Docker Operations Guide

This document provides detailed instructions and scripts for various Docker operations.

## 1. What is the relation between an image and a container in Docker?

In Docker:
- **Image:** A Docker image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software: the code, runtime, libraries, and dependencies. Images serve as the blueprint for creating containers.
- **Container:** A Docker container is a running instance of a Docker image. It represents a running process in the Docker environment and provides an isolated execution environment. Containers use the image as a template but have their own writable filesystem and isolated resources.

### Differences Between an Image and a Container

| Feature          | Image                                     | Container                                |
|------------------|-------------------------------------------|------------------------------------------|
| **Definition**   | Blueprint for creating containers         | Running instance of an image              |
| **State**        | Static (unchangeable)                     | Dynamic (can change during execution)    |
| **Filesystem**   | Read-only filesystem                      | Writable filesystem                       |
| **Resource**     | No isolated resources                     | Has isolated resources                    |
| **Execution**    | Not executable on its own                 | Runs applications and processes           |
| **Persistence**  | Does not maintain state                   | Maintains state during runtime            |
| **Lifecycle**    | Created once, can be reused               | Started, stopped, and deleted             |


## 2. List all the images and the containers in the system.

- **List Docker images:**

  ```bash
  docker images
  ```

- **Run the `nginx` container:**

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

  - `-d` runs the container in detached mode.
  - `--name super-nginx` names the container `super-nginx`.
  - `-p 7001:80` exposes port 80 of the container to port 7001 on the host.
  - `-e NGINX_HOST=vunet.local` sets the environment variable `NGINX_HOST`.

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

- **Create the Docker volume:**

  ```bash
  docker volume create vunet
  ```

- **Run the `nginx` container with the volume attached:**

  ```bash
  docker run -d --name super-nginx -p 7001:80 -v vunet:/etc/ nginx
  ```

  - `-v vunet:/etc/` attaches the `vunet` volume to `/etc/` in the container.

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
  # Use the latest Ubuntu image
  FROM ubuntu:latest

  # Install Python 3.10
  RUN apt-get update && \
      apt-get install -y python3.10 python3-pip

  # Copy the Python script into the image
  COPY server.py /usr/src/app/server.py

  # Set the working directory
  WORKDIR /usr/src/app

  # Run the Python script as the entrypoint
  ENTRYPOINT ["python3", "server.py"]
  ```

- **Python script (`server.py`):**

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

## 8. Build and run the container

- **Build the Docker image:**

  ```bash
  docker build -t python-server .
  ```

- **Run the container using the image:**

  ```bash
  docker run -d --name python-server -p 8000:8000 python-server
  ```

## 9. Check if the container is running and has the Python process running

- **Check the running container:**

  ```bash
  docker ps
  ```

  Ensure `python-server` is listed.

- **Check the Python process inside the container:**

  ```bash
  docker exec -it python-server ps aux
  ```

## 10. Why are Docker networks used? Create a Docker network named `vunet`

- **Purpose of Docker networks:**

  Docker networks are used to manage communication between containers, isolate network traffic, and configure network settings. They enable containers to communicate with each other and with external systems securely and efficiently.

- **Create a Docker network named `vunet`:**

  ```bash
  docker network create vunet
  ```

## 11. Create an Nginx cluster by attaching the created network, `vunet`, to it

- **Run Nginx containers in the `vunet` network:**

  ```bash
  docker run -d --name nginx1 --network vunet nginx
  docker run -d --name nginx2 --network vunet nginx
  ```

  These commands run two Nginx containers connected to the `vunet` network.
