pipeline {
    agent any
    stages {
        stage('Acquire Pipeline'){
          steps{
        	   sh 'python3 /home/ubuntu/First.py'
                }
        }
        stage('Onbaord'){
          steps{
        	  sh 'python3 /home/ubuntu/Second.py'
                }
	stage('Test'){
          steps{
        	  sh 'python3 /home/ubuntu/Third.py'
                }	
	           }
           }
		   }
     }
