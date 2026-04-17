pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SherineSelvakumar/Joanna-Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Build successful!'
            }
        }
    }
}
