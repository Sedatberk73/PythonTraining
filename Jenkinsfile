pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                // Install dependencies, including Selenium
                sh 'pip install -U seleniumbase'
            }
        }
        stage('Run Tests') {
            steps {
                // Run the Python tests with pytest
                sh 'pytest --dashboard --html=report.html -s --headless'
            }
        }
    }
    post {
        always {
            // Archive the test reports
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
        success {
            echo 'The tests have passed!'
        }
        failure {
            echo 'The tests have failed!'
        }
    }
}
