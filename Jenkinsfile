pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7'
		}
	}
	stages {
		stage('build') {
			steps {
				sh 'sudo su jenkins'
				sh 'sudo -H pip install selenium'
				}
		}
		stage('test') {
			steps {
				sh 'python tests/regression_test.py stage'
				}
			}
	}
}
