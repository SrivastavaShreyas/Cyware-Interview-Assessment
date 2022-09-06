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
                git([url: 'https://github.com/SrivastavaShreyas/Cyware-Interview-Assessment.git', branch: 'main', credentialsId: 'github_personal_id'])
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