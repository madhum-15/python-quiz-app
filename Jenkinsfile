pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Stating the application'
        sh '''pip3.7 install -r requirements.txt
python3.7 manage.py runserver 0.0.0.0:8001'''
      }
    }

  }
}