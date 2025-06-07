# Simple Python Docker Example

This is a simple Flask web application containerized with Docker.

## Files

- `app.py` - Simple Flask web application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker container configuration
- `README.md` - This file

## How to Build and Run

### 1. Build the Docker Image

```bash
docker build -t python-docker-example .
```

### 2. Run the Container

```bash
docker run -p 5000:5000 python-docker-example
```

### 3. Access the Application

Open your browser and go to:
- Main page: http://localhost:5000
- Health check: http://localhost:5000/health

### 4. Stop the Container

Press `Ctrl+C` in the terminal where the container is running.

### 5. Publish the Image to Docker Hub
- Log in to Docker Hub from your terminal
```bash
docker login 
```

- Build your Docker image
```bash
docker build -t <your-dockerhub-username>/<image-name>:<tag> .
```

- Test the image
```bash
docker run -p 5000:5000 <your-dockerhub-username>/flask-docker-app:latest
```

- publish the image to Docker Hub
```bash
docker push <your-dockerhub-username>/flask-docker-app:latest
```

## Docker Commands Explained

- `docker build -t python-docker-example .` - Builds an image with tag "python-docker-example"
- `docker run -p 5000:5000 python-docker-example` - Runs the container and maps port 5000
- `docker ps` - Lists running containers
- `docker images` - Lists available images
- `docker stop <container_id>` - Stops a running container

## What the App Does

The Flask application:
- Serves a welcome message at the root URL
- Shows current timestamp
- Provides a health check endpoint
- Runs on port 5000 inside the container 