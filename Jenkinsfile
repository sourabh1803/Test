pipeline {
    agent any
    stages {
	  stage('Helm Repo Update'){
          steps{
             sh 'python /home/ubuntu/connect.py'
                }
	}	
	stage('Helm Repo Cleane'){
          steps{
             sh 'python /home/ubuntu/connect1.py'
                }
	}        
	 stage('Helm Chart Execution'){
         steps{
             sh 'python /home/ubuntu/connect2.py'
                }	
	           }
         }
}

