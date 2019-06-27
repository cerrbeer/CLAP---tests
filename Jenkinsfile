pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7'
		}
	}
	stages {
		stage('build') {
			steps {
			sh 'docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-radium'
			}
		}
		stage('test') {
			steps {
				sh 'python tests/regression_test.py'
				}
			}
	}
}
