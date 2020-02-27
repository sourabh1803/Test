pipeline {
    agent any
    stages {
	  stage('Helm Repo Update'){
          steps{
             sh 'python /home/ubuntu/connect.py'
                }
	}	      
	 stage('Helm Chart Execution'){
         steps{
             sh 'python /home/ubuntu/connect2.py'
                }	
	           }
         }
}

