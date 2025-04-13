#  Jenkins Pipeline Explained – Automated Docker Deployment on Git Commit

This pipeline automates the deployment of an application using Docker. It:
- Triggers on every Git push
- Loads configuration from a `.env` file in the repo
- Builds and pushes a Docker image
- Deploys the updated container

---

##  Prerequisites

- Jenkins is configured with:
  - Docker installed on the agent
  - GitHub or GitLab credentials setup
  - Docker Hub credentials stored securely (e.g., `docker-hub-credentials`)
- Git repository includes a `.env` file and a `Dockerfile`

---

##  Jenkinsfile Breakdown
# 🧱 Jenkins Pipeline Structure and Explanation

Below is a breakdown of each major section in the `Jenkinsfile` for Docker-based deployment automation:

---

## 1️⃣ `agent any`
Runs the pipeline on any available Jenkins agent.  
This provides flexibility to use any node configured in your Jenkins setup.

---

## 2️⃣ `environment`
Defines global credentials for the Docker registry.  
For example, a credential ID like `docker-hub-credentials` is securely used to log in during image push.

---

## 3️⃣ `triggers`
Triggers the pipeline on every push via GitHub webhook.  
This ensures your deployment process starts automatically with every code change.

---

## 4️⃣ `Checkout`
Pulls the code from the specified branch and repository URL as defined in the `.env` file.  
It ensures the pipeline works dynamically across different environments or branches.

---

## 5️⃣ `Load Environment Variables`
Dynamically loads configuration values such as:
- App name
- Git repo and branch
- Docker image name
- Port mapping  
All values are sourced from a `.env` file committed to the repo.

---

## 6️⃣ `Build Docker Image`
Builds a Docker image using the application's `Dockerfile`.  
The image is tagged using the Jenkins build number to uniquely identify each version.

---

## 7️⃣ `Push to Docker Hub`
Pushes the built Docker image to Docker Hub (or any Docker registry).  
Authentication is handled securely using Jenkins credentials.

---

## 8️⃣ `Deploy Container`
Stops and removes any existing container with the same app name (if running).  
Then it runs a new container from the freshly pushed image, exposing the correct port.

---

## 9️⃣ `Post`
Handles actions after the main stages:

- ✅ `always`: Cleans up Docker images from the Jenkins agent to save space.
- ✅ `success`: Logs a "Deployment successful" message.
- ✅ `failure`: Logs an error message for debugging failed deployments.

---
