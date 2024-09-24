pipeline {
    agent {
        label 'test'
    }
    stages {
        stage('Clone simple-api repository') {
            steps {
                git url: 'https://github.com/nichaOrg/simple-api.git', branch: 'dev'
            }
        }

        stage('Build and Test API') {
            steps {
                script {
                    // Build and test API
                    sh 'pip install -r requirements.txt ' // Install dependencies
                    sh 'python3 app.py &'
                    sh 'sleep 5' // Wait for API to start

                    // Run unit tests
                    sh 'python3 test_unit.py'
                }
            }
        }

        stage('Build and Test Robot Framework') {
            steps {
                script {
                    dir('./robot3/') {
                        git url: 'https://github.com/nichaOrg/simple-api-robot.git', branch: 'main'
                    }
                    sh 'cd ./robot3 && robot test_robot.robot'
                }
            }
        }

        // #build image
        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh 'docker login'
                    sh 'docker build -t horiii/cicd:lastest .'
                    sh 'docker push horiii/cicd:lastest'
                }
            }
        }

        stage('Clean Workspace') {
            steps {
                sh 'docker compose down'
                sh 'docker system prune -a -f'
            }
        }
        stage('compose up') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
        stage('Running Preprod') {
            agent {
                label 'preprod'
            }
            steps {
                sh 'docker compose down && docker system prune -a -f && docker compose up -d --build'
            }
        }
    }
}
