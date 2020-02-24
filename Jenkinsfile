pipeline {
    agent any
    stages {
         stage('Helm Repo Update'){
          steps{
        	  sh  'sh /home/ubuntu/chart.sh'
                }
	}	
	stage('Helm Chart Execution'){
          steps{
        	  sh 'sh /home/ubuntu/chart1.sh'
                }	
	           }
         }
}
