pipeline {
    agent any

    environment {
        // This ensures the Allure tool we configured in Step 2 is used
        ALLURE_HOME = tool 'allure'
    }

    stages {
        stage('Cleanup') {
            steps {
                echo 'Cleaning up any old containers...'
                // Using 'bat' because you are on Windows
                bat 'docker-compose down --remove-orphans'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Starting Docker Compose and running tests...'
                // --exit-code-from ensures Jenkins marks the build as failed if a test fails
                bat 'docker-compose up --build --exit-code-from orangehrm-tests'
            }
        }
    }

    post {
        always {
            echo 'Generating Allure Report...'
            // This 'allure' command matches the plugin and tool name
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            
            echo 'Shutting down containers...'
            bat 'docker-compose down'
        }
    }
}