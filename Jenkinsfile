pipeline {
	agent {
		docker {
			image 'cerrbeer/python3.7:latest'
		}
	}
	stages {
		stage('build') {
			steps {
				sh 'python -m pip install --user selenium'
				}
			}
        stage('test') {
            steps {
                sh 'python tests/regression_test.py stage'
                }
			}
	}
}
