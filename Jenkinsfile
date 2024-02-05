pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile MathUtils.py tests_data.py'
            }
        }
        stage('Test') {
            steps {
                sh 'py.test --junit-xml test-reports/results.xml test_math_utils.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

    }
}