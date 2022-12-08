pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'ls'
      }
    }
    stage('hello') {
      steps {
         sh 'python checkversion.py'
      }
    }
  }
}
