pipeline {

	agent any

	stages {
	
	
		

		stage('Python Download'){


			steps{
				powershell 'choco install python2 --version=2.7.16'
				powershell 'python --version'
	}
      }
		stage('Flask Download'){
			
			steps{
				powershell 'pip install Flask'
				powershell 'pip install Werkzeug'
				powershell 'flask --version'
			}
		}

		stage('Jinja2 Download'){
		
			steps{
				powershell 'pip install Jinja2'
				powershell 'pip freeze'
			}
		
		}

		stage('Git Download'){
			steps{
				powershell 'choco install git.install'
			}
		}
		
		stage('Pulling files from repository '){
			
			steps{
				
			}
		
		}
   }



}