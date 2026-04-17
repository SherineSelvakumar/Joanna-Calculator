pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO = "625073910615.dkr.ecr.us-east-1.amazonaws.com/myapp"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SherineSelvakumar/Joanna-Calculator.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin 625073910615.dkr.ecr.us-east-1.amazonaws.com
                '''
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag myapp:latest $ECR_REPO:latest'
            }
        }

        stage('Push to ECR') {
            steps {
                sh 'docker push $ECR_REPO:latest'
            }
        }
    }
}
