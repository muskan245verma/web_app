pipeline {
    agent any 
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '965279af-cab6-4cf7-9829-4faa69c04d9c', url: 'https://github.com/muskan245verma/web_app.git']]])
            }
        }
        stage('Building the app') { 
            steps {
                git branch: 'main', url: 'https://github.com/muskan245verma/web_app.git'
                bat 'python Lgame.py'
                echo "---------------------Build Successfully----------------------"
            }
        }
        stage('Testing Stage') { 
            steps {
                echo "Tesing Under process........"
                bat 'python test_Lgame.py'
                echo "---------------------Tested Successfully---------------------"
            }
        }
        stage('Docker Image'){
            steps{
                bat 'docker image build -t web_app .'
                echo "-------------------Image Built Successfully------------------"
            }
        }
        stage('Stop previous containers') {
            steps {
                 echo "Running"
                 bat 'docker stop Web_app'
                 echo "---------------Previous Containers Stopped-------------------"
                   }
             }
        stage('Running Docker Image'){
              steps{
                   echo "Image Getting Ready to run"
                   bat 'docker run -p 5000:5000 --name Web_app -d web_app'
                   echo "------------Image Running---------------"
              }
        }
    }
}
