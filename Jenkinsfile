pipeline {
    agent any
    options { skipDefaultCheckout(true) }
    parameters { booleanParam(name: 'DEPLOY_LOCAL', defaultValue: false, description: 'Deploy Compose on this dedicated lab agent') }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Validate') {
            steps { sh 'docker compose config --quiet' }
        }
        stage('Build image') { steps { sh 'docker compose build flask-app' } }
        stage('Deploy with docker compose') {
            when { expression { params.DEPLOY_LOCAL } }
            steps { sh 'docker compose up -d' }
        }
    }
}
