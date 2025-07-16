# Calculator App CI/CD Pipeline

This project is a simple Python calculator application with a CI/CD pipeline using Jenkins.

# Contents
- 'calculator.py': the calculator implementation
- 'test_calculator.py': unit tests for the calculator
- 'Jenkinsfile': Jenkins pipeline configuration

# Pipeline
The Jenkins pipeline has three stages:
1. Build: currently a placeholder that echoes "Skipping Docker build"
2. Test: runs all Python unit tests using 'pytest'
3. Deploy: currently a placeholder that echoes "Deploying application"

# Running the pipeline
The pipeline is configured to run in Jenkins. To trigger:
- Make sure Jenkins is connected to this GitHub repo.
- Run the pipeline job from the Jenkins UI.
- The pipeline will execute and print the test results.

All stages are designed to pass if all tests succeed.

# Requirements
- Python 3.6+
- pytest
