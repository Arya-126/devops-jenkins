pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m unittest discover -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p deployment
                    cp app.py requirements.txt deployment/
                    ls -l deployment/
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline SUCCESS: app deployed to workspace/deployment/' }
        failure { echo 'Pipeline FAILED — check Stage View and Console Output' }
    }
}
