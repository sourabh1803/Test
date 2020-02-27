pipeline {
    agent any
    stages {
	  stage('Helm Repo Update'){
          steps{
             sh 'sh /home/ubuntu/repoupdate.sh'
                }
	}	
	  stage('Cleaning Repo with same Name'){
          steps{
        	  sh 'sh /home/ubuntu/try.sh'
                }
	    }	    
	stage('Helm Chart Execution'){
          steps{
        	  sh 'sh /home/ubuntu/chartadd.sh.sh'
                }	
	           }
         }
}
