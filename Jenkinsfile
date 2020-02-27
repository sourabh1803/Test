pipeline {
    agent any
    stages {
	  stage('Helm Repo Update'){
          steps{
             sh 'python /home/ubuntu/connect.py'
                }
	}	
	  stage('Cleaning Repo with same Name'){
          steps{
        	  sh 'sh /home/ubuntu/try.sh'
                }
	    }	    
	stage('Helm Chart Execution'){
          steps{
        	  sh 'sh /home/ubuntu/chartadd.sh'
                }	
	           }
         }
}
