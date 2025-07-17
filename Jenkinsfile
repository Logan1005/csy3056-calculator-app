

// Jenkinsfile for CI/CD Pipeline
// This file defines the stages for building, testing, and deploying the calculator application.

pipeline {
    agent any

    environment {
        IMAGE_NAME = 'calculator-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests inside Docker container...'
                bat "docker run --rm %IMAGE_NAME%"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Deployment steps need to go here
            }
        }
    }
}
