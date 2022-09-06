pipeline {
    environment {
        registry = "2003103/cyware"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Initialize') {
            steps{
                script{
                    def dockerHome = tool 'Docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                } 
            }
        }
        stage('Cloning our Git') {
            steps {
                git([url: 'https://github.com/SrivastavaShreyas/Cyware-Interview-Assessment.git', branch: 'main', credentialsId: 'github_personal_id'])
            }
        }
        stage('Building our image') {
            steps{
                script {
                    echo env.BUILD_ID
                    echo registry:{env.BUILD_ID}
                    // dockerImage = docker.build(registry:{env.BUILD_ID})
                }
            }
        }
        stage('Deploy our image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}