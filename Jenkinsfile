pipeline {
    agent any
    stages {
         stage('Helm Chart Execution'){
          steps{
        	  sh  'sh /home/ubuntu/chart1.sh'
                }
	}	
	stage('Test'){
          steps{
        	  sh 'python3 /home/ubuntu/Third.py'
                }	
	           }
         }
}
