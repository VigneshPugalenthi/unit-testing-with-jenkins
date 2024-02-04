pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python MathUtils.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -v -s'
            }
        }
    }
}