pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                pip install -U seleniumbase
            }
        }
        stage('Test') {
            steps {
                pytest --dashboard --html=report.html -s --headless
            }
        }
    }
}