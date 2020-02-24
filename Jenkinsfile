pipeline {
    agent any
    stages {
	  stage('Acquire Packages'){
          steps{
        	  sh  'sh /home/ubuntu/ftp.sh'
                }
	}	
         stage('Helm Repo Update'){
          steps{
        	  sh  'sh /home/ubuntu/chart.sh'
                }
	}	
	    stage('Cleaning Repo with same Name'){
          steps{
        	  sh 'sh /home/ubuntu/chart2.sh'
                }
	    }	    
	stage('Helm Chart Execution'){
          steps{
        	  sh 'sh /home/ubuntu/chart1.sh'
                }	
	           }
         }
}
