pipeline {
    agent any
    stages {
        stage('Build unit-testing-with-jenkins') {
            steps {
                sh 'python3 -m py_compile MathUtils.py tests_data.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}