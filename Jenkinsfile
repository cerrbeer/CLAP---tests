pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python tests/regression_test.py stage'
            }
        }
    }
}
