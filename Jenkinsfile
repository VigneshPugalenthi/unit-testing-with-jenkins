pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 -m py_compile MathUtils.py tests_data.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml test-reports/results.xml test_math_utils.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    emailext (attachLog: true, body: '$DEFAULT_CONTENT', replyTo: '$DEFAULT_REPLYTO', subject: '$DEFAULT_SUBJECT', to: 'vignesh1998.vk@gmail.com')
                }
            }
        }
    }
}