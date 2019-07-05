pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7:latest'
		}
	}
	stages {
        stage('build') {
            steps {
                sh 'pip show selenium'
                }
			}
        stage('test') {
            steps {
                sh 'python tests/regression_test.py stage'
                }
			}
	}
}
