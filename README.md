# Case Study

## Uygulamanın Build Edilmesi

** Öncelikle uygulamamızı docker üzerinden Dockerfile kullanarak containerize ettim ve Docker Hub'a kendi repository'me push'ladım. ** <br/>
** Uygulamamızı build etmek için öncelikle shell'imize girerek container'ımızı repository'den pull işlemi ile alıyoruz.**

`docker pull ahmetfatih024/casestudy:latest`

** Sonra ise repository'den aldığımız container'ımızı container run komutu ile ayağa kaldırıyoruz.**

`docker container run -p 5000:5000 ahmetfatih024/casestudy`

** Son olarak web tarayıcımızdan localhost'a erişerek uygulamamızı görebiliriz. **

` http://localhost:5000/ `


** AHMET FATİH SARAÇ **