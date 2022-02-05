pipeline {
    agent any//Pipeline'nın herhangi bir ortamda yürütülmesini sağlar.
	stages{
		stage('Clean Workspace'){//Bu başlangıç adımında daha önce yaptığımız işlemler varsa o dosyaları yeni yürütme için temizlememizi sağlar.
			steps{
                cleanWs()//Bu komut ile Jenkins'in workspace'ini temizleriz.
			}
		}
		stage('Git Clone'){//Bu kısımda Github üzerindeki dosyalarımızın klonunu oluşturduk, yani sistemimize çektik.
			steps{
                powershell 'D:/Programlar/Git/bin/git.exe clone https://github.com/AhmetFatihSarac/CaseStudy.git'//Burada dosya dizininin adresini verdik ve github url'mizi ekledik.
                powershell 'pwd'//Burada ise hangi dizinde olduğumuzu kontrol ettik.
			}
		}
		stage('Docker Image Build'){//Bu kısımda github üzerinden sistemimize çektiğimiz dosyaları docker kullanarak image'ni oluşturduk.
			steps{
                powershell 'docker image build -t ahmetfatih024/casestudy:0.0.2 ./CaseStudy'//Bu komutta image'mizi tagledik. Bulunduğumuz klasörün içindeki 'CaseStudy' dizininden image almasını söyledik.
                powershell 'docker image ls -a'//Burada ise oluşturulmuş image'mizi görmeyi sağladık.
			}
		}
		stage('Dockerhub Login'){//Bu kısımda Dockerhub hesabımıza girişimizi gerçekleştirdik.
			steps{
                powershell 'docker login -u ahmetfatih024 -p 407d005e-4481-427c-bbb4-bc6e8df8eb4e'//Bu komutta kullamıcı adımızı ve şifremizi girdik. Şifreyi Dockerhub'dan aldığım access token ile girdim.
			}
		}
		stage('Docker Image Push'){//Bu kısımda ise oluşturmuş olduğumuz image'i bilgilerini girmiş olduğumuz Dockerhub hesabına pushladık.
			steps{
                powershell 'docker image push ahmetfatih024/casestudy:0.0.2'//Bu komutla belirli tag'deki image'i Dockerhub Repository'mize pushladık.
			}
		}
		stage('Docker Image Deployment'){//Bu kısımda ise oluştumuş olduğumuz image'i deploy ettik.
			steps{
                powershell 'docker container run -d -p 5000:5000 ahmetfatih024/casestudy:0.0.2'//Bu komutta image'imizden bir container ayağa kaldırdık. 5000:5000 portu üzerinden çalıştırdık.
			}
		}
		stage('Docker Check'){//Bu kısımda oluşturduğumuz container'i kontrol ettik.
			steps{
                powershell 'docker ps'//Bu komutta container'ı kontrol ettik.
			}
		}
		stage('Docker API Test'){//Bu kısımda ise çalışan container'ımızın port üzerinde çalışıp çalışmadığını test ettik.
			steps{
                powershell 'curl -v http://localhost:5000'//Bu komutlar ile port'umuza giden adresden API'mizin verilerini gördük.
                powershell 'curl -v http://localhost:5000/temperature?city=istanbul'
			}
		}
		stage('Docker Stop and Remove'){//Bu son kısımda ise çalışmakta olan container'ımızı durdurup sildik ve işlemi sonlandırdık.
			steps{
                powershell 'docker rm $(docker stop $(docker ps -a -q --filter ancestor="ahmetfatih024/casestudy:0.0.2"))'
			}//Bu komutta ise önce kontrol ettiğimiz container'ın tag'İni girerek belirledik. Sonra container'ı durdurup sildik.
		}
	}
}