pipeline {
    agent any
	stages{
		stage('Clean Workspace'){
			steps{
                cleanWs()
			}
		}
		stage('Git Clone'){
			steps{
                powershell 'D:/Programlar/Git/bin/git.exe clone https://github.com/AhmetFatihSarac/CaseStudy.git'
                powershell 'pwd'
			}
		}
		stage('Docker Image Build'){
			steps{
                powershell 'docker image build -t ahmetfatih024/casestudy:0.0.2 ./CaseStudy'
                powershell 'docker image ls -a'
			}
		}
		stage('Dockerhub Login'){
			steps{
                powershell 'docker login -u ahmetfatih024 -p 407d005e-4481-427c-bbb4-bc6e8df8eb4e'
			}
		}
		stage('Docker Image Push'){
			steps{
                powershell 'docker image push ahmetfatih024/casestudy:0.0.2'
			}
		}
		stage('Docker Image Deployment'){
			steps{
                powershell 'docker container run -d -p 5000:5000 ahmetfatih024/casestudy:0.0.2'
			}
		}
		stage('Docker Check'){
			steps{
                powershell 'docker ps'
			}
		}
		stage('Docker API Test'){
			steps{
                powershell 'curl -v http://localhost:5000'
                powershell 'curl -v http://localhost:5000/temperature?city=istanbul'
			}
		}
		stage('Docker Stop and Remove'){
			steps{
                powershell 'docker rm $(docker stop $(docker ps -a -q --filter ancestor="ahmetfatih024/casestudy:0.0.2"))'
			}
		}
	}
}