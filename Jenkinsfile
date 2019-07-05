pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7:latest'
		}
	}
	stages {
        stage('test') {
            steps {
                sh 'python tests/regression_test.py stage'
                }
			}
	}
}
