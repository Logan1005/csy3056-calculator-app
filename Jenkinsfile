
// Author: Logan
// Purpose: Jenkinsfile for CI/CD Pipeline
// Dependencies: Docker, Jenkins
// Description: This file defines the stages for building, testing, and deploying the calculator application.

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
                bat """
                REM Stop & remove any existing container
                docker stop calculator-app || exit 0
                docker rm calculator-app || exit 0

                REM Run the new container
                docker run -d -p 5000:5000 --name calculator-app %IMAGE_NAME% python app.py
                """
            }  
        }
    }
}
