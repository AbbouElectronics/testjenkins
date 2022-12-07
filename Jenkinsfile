pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('sql') {
      steps {
        sh 'python sql.py'
      }
    }
  }
}
