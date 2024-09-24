pipeline {
    agent any
    environment {
        IMAGE_NAME = 'ghcr.io/thanatat64/test-api'
    }

    stages {
        stage('Run Unit Test') {
            agent {
                    label 'test'
            }
            steps {
                sh 'echo pass here'
                sh 'pip install --no-cache-dir --upgrade -r requirements.txt '
                sh 'python3 unit_test.py'
            // Assumes unit_test.py exists in the root directory and contains your unit tests
            }
        }
        stage('Create Images of Simple API') {
            agent {
                    label 'test'
            }
            steps {
                sh 'docker stop simple-api-container'
                sh 'docker rm simple-api-container'
                sh 'docker build -t simple-api .'
            // Build Docker image using provided Dockerfile
            }
        }
        stage('Create Container of Simple API') {
            agent {
                    label 'test'
            }
            steps {
                sh 'docker run -d -p 8000:8000 --name simple-api-container simple-api'
            // Create Docker container from the built image
            }
        }
        stage('Clone/Setup Robot') {
            agent { label 'test' }
            steps {
                dir('./robot-test/') {
                    git branch: 'main', credentialsId: 'tnt', url: 'https://github.com/thanatat64/SDPX-Robot-Assignment.git'
                }
                echo 'clone done!'
            }
        }

        stage('Run Robot') {
            agent { label 'test' }
            steps {
                // sh "pwd"
                // sh "ls"
                sh 'cd ./robot-test && python3 -m robot test_plus.robot'
            }
        }
        stage('Push image') {
            agent {
                    label 'test'
            }
            steps {
                withCredentials(
                [usernamePassword(
                    credentialsId: 'tnt',
                    passwordVariable: 'githubPassword',
                    usernameVariable: 'githubUser'
                )]
            ) {
                    sh "docker login ghcr.io -u ${githubUser} -p ${githubPassword}"
                    sh "docker pull ${IMAGE_NAME}"
                    sh "docker tag ${IMAGE_NAME} ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker rmi ${IMAGE_NAME}:${env.BUILD_NUMBER}"
            }
            }
        }
        stage('Pull image && runcontainer') {
            agent {
                    label 'pre-prod'
            }
            steps {
                withCredentials(
                [usernamePassword(
                    credentialsId: 'tnt',
                    passwordVariable: 'githubPassword',
                    usernameVariable: 'githubUser'
                )]
            ) {
                    sh "docker login ghcr.io -u ${githubUser} -p ${githubPassword}"
                    sh "docker pull ${IMAGE_NAME}"
            }
            }
        }
        stage('runcontainer') {
            agent {
                    label 'pre-prod'
            }
            steps {
                    sh 'docker stop simple-api-container02'
                    sh 'docker rm simple-api-container02'
                    sh "docker run -d -p 8000:8000 --name simple-api-container02 ${IMAGE_NAME}"
            }
        }
    }
}
