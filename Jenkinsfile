pipeline {
	agent {
		docker {
		    image 'selenium/standalone-chrome:3.141.59-neon'
		 }
		docker {
		    image 'cerrbeer/python3.7'
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
