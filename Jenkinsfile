pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'dir'
      }
    }
    stage('hello') {
      steps {
         bat 'python3 hello.py'
      }
    }
  }
}
