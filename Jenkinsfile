pipeline {
    agent any

    environment {
        REGISTRY_CREDENTIALS = 'docker-hub-credentials'
    }

    triggers {
     
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                git url: "${env.GIT_REPO}", branch: "${env.GIT_BRANCH}"
            }
        }

        stage('Load Environment Variables') {
            steps {
                script {
                    def props = readProperties file: '.env'
                    env.APP_NAME      = props['APP_NAME']
                    env.DOCKER_IMAGE  = props['DOCKER_IMAGE']
                    env.GIT_REPO      = props['GIT_REPO']
                    env.GIT_BRANCH    = props['GIT_BRANCH']
                    env.APP_PORT      = props['APP_PORT']
                    env.IMAGE_TAG     = "${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', REGISTRY_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh "docker rm -f ${APP_NAME} || true"
                    sh "docker run -d --name ${APP_NAME} -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}:${IMAGE_TAG}"
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh "docker rmi ${DOCKER_IMAGE}:${IMAGE_TAG} || true"
        }
        success {
            echo "Deployment successful! 🚀"
        }
        failure {
            echo "Deployment failed! ❌"
        }
    }
}
