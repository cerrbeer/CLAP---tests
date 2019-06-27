pipeline {
	agent {
		docker {
		    image 'selenium/standalone-chrome:3.141.59-neon'

			
		}
	}
	stages {
		stage('test') {
			steps {
				sh 'python tests/regression_test.py'
				}
			}
	}
}
