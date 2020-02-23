pipeline {
    agent any
    stages {
         stage('Helm Chart Execution'){
          steps{
        	  sh  'python3 /home/ubuntu/First.py'
                }
	}	
	stage('Test'){
          steps{
        	  sh 'python3 /home/ubuntu/Third.py'
                }	
	           }
         }
}
