pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'application started'
        sh 'python3.7 manage.py runserver 0.0.0.0:8001'
      }
    }

  }
}