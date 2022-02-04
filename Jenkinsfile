pipeline {

	agent any

	stages {
	
	
		stage('Chocolatey Download'){
		
			steps{
				powershell 'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))'
			}
		
		}

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