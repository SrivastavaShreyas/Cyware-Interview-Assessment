pipeline {
    environment {
        registry = "2003103/cywarey"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning our Git') {
            steps {
                git 'https://github.com/SrivastavaShreyas/Cyware-Interview-Assessment.git'
            }
        }
        stage('Building our image') {
            steps{
                script {
                    dockerImage = docker.build cyware_assessment + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy our image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps{
                sh "docker rmi $cyware_assessment:$BUILD_NUMBER"
            }
        }
    }
}