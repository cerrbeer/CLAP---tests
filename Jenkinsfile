pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7'
		}
	}
	stages {
		stage('build') {
			steps {
				sh 'pip3 install selenium'
				}
			}		stage('test') {
			steps {
				sh 'python tests/regression_test.py stage'
				}
			}
	}
}
