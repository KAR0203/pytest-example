pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'develop2', description: 'The branch to checkout')
        string(name: 'PYTHON_HOME', defaultValue: '/Users/karan.pandhare/PytestSample/pytest-example/venv/bin/python', description: 'Path to the Python executable')
    }

    environment {
        PYTHON_HOME = "${params.PYTHON_HOME}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out branch: ${params.BRANCH_NAME}"
                git branch: "${params.BRANCH_NAME}", url: 'https://github.com/KAR0203/pytest-example.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies..."
                    sh '${PYTHON_HOME} -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests..."
                    sh './venv/bin/pytest --junitxml=results.xml'
                }
            }
        }
        stage('Fetch Test Status') {
            steps {
                script {
                    echo "Fetching test status from API..."

                    def response = httpRequest url: 'http://localhost:8080/job/TestngProject7/32/testReport/api/json', acceptType: 'APPLICATION_JSON'
                    def jsonResponse = readJSON text: response

                    // Extracting test status from the response
                    def failedTests = jsonResponse.failCount
                    def skippedTests = jsonResponse.skipCount
                    def passedTests = jsonResponse.passCount
                    def regressionTests = jsonResponse.regressionCount // Assuming you have this field in the response
                    def fixedTests = jsonResponse.fixedCount // Assuming you have this field in the response

                    echo "Test Results from API: "
                    echo "Failed Tests: ${failedTests}"
                    echo "Skipped Tests: ${skippedTests}"
                    echo "Passed Tests: ${passedTests}"
                    echo "Regression Tests: ${regressionTests}"
                    echo "Fixed Tests: ${fixedTests}"

                    // You can use these values to set build result or report accordingly
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv'
        }

        success {
            echo 'Build and tests succeeded!'
            junit '**/results.xml'
        }

        failure {
            echo 'Build or tests failed!'
        }

        aborted {
            echo 'Build was aborted, no tests were run.'
        }
    }
}
