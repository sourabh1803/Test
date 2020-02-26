pipeline {
    agent any
    stages {
	  
         stage('Helm Repo Update'){
          steps{
        	     sh  'ssh ubuntu:ubuntu@10.90.73.189'
		     sh  '/home/ubuntu/repoupdate.sh'
                }
	}	
	    stage('Cleaning Repo with same Name'){
          steps{
        	  sh 'sh /home/ubuntu/second.sh'
                }
	    }	    
	stage('Helm Chart Execution'){
          steps{
        	  sh 'sh /home/ubuntu/chartadd.sh.sh'
                }	
	           }
         }
}
