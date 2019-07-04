pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7'
		}
	}
	stages {
		stage('test') {
			steps {
				sh 'python regression_test.py stage'
				}
			}
	}
}
