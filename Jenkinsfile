pipeline {
    agent {
      label 'web2'
    }

    tools {
      allure 'allure'
      git 'Default'
    }

    stages {
        stage("Clean"){
            steps {
                sh "rm -rf allure junit.xml "
            }
        }
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://gitlab.stuq.ceshiren.com/seveniruby/geektime_0.git'

            }
        }
        stage('Tests') {
            parallel {
                stage('Test2') {
                    steps {
                        sh "echo test2"
                    }
                }
                stage('Test3') {
                    steps {
                        sh "echo test3"
                    }
                }
                stage('Test1') {
                    steps {

                        // Run Maven on a Unix agent.
                        sh "pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ "
                        sh "pytest  --alluredir=allure --junitxml=junit.xml geektime_0/service/petclinic/ "

                        // To run Maven on a Windows agent, use
                        // bat "mvn -Dmaven.test.failure.ignore=true clean package"
                    }

                    post {
                        // If Maven was able to run the tests, even if some of the test
                        // failed, record the test results and archive the jar file.
                        success {
                            junit 'junit.xml'
                            archiveArtifacts 'junit.xml'
                            allure includeProperties: false, jdk: '', results: [[path: 'allure']]
                        }
                    }
                }
            }
        }
    }
}
