

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
                // Build with Dockerfile that installs pytest
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest tests inside Docker container...'
                // Run tests with pytest; if tests fail, it will cause this stage to fail
                bat "docker run --rm %IMAGE_NAME% pytest test_calculator.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
            }
        }
    }
}
