pipeline {
    agent any 
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '965279af-cab6-4cf7-9829-4faa69c04d9c', url: 'https://github.com/muskan245verma/web_app.git']]])
            }
        }
        stage('Build') { 
            steps {
                git branch: 'main', url: 'https://github.com/muskan245verma/web_app.git'
                bat 'python Lgame.py'
                echo "Build Successfully"
            }
        }
        stage('Test') { 
            steps {
                bat 'python test_Lgame.py'
                echo "Tested Successfully"
            }
        }
        stage('Building Docker Image'){
            steps{
                bat 'docker image build -t web_app .'
                echo "Image Built Successfully"
            }
        }

        stage('Running Docker Image'){
              steps{
                   bat 'docker run -p 5000:5000 -d web_app'
                   echo "Image Running"
              }
        }
    }
}
