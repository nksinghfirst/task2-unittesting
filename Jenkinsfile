pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nksinghfirst/task2-unittesting.git'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 unit.py'
            }
        }
    }
}
