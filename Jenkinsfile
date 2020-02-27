pipeline {
    agent any
    stages {
	  stage('MD5 File Check Sum'){
          steps{
             sh 'python /home/ubuntu/checksum.py'
                }
	   }	
	  stage('VirusCheck'){
          steps{
             sh 'python /home/ubuntu/scn.py'
                }
	   }	
	  stage('Helm Repo Update'){
          steps{
             sh 'python /home/ubuntu/connect.py'
                }
	}	
	  stage('Cleaning Repo with same Name'){
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

