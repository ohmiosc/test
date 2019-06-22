pipeline {
  agent any
  stages {
    stage('Repository') {
      steps {
          git url: "https://github.com/mario21ic/python-testing.git", branch: "master"
      }
    }
    stage('Run test') {
      steps {
          sh "cd 4-fake-delegation/ && python3 -m unittest -v test/CostoEnvioService.py"
      }
    }
  }
}
