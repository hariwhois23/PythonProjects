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

### 🖥️ `agent any`
Specifies that the pipeline can run on any available Jenkins agent.

---

###  `environment` Block
```groovy
environment {
    REGISTRY_CREDENTIALS = 'docker-hub-credentials'
}
