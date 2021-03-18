pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python3.7 manage.py runserver 0.0.0.0:8001'
        echo 'application started'
      }
    }

  }
}