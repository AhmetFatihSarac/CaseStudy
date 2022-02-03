# Case Study

## Görev(1): API'nin Oluşturulması

**API'yi oluşturmak için Flask Framework kullanmayı tercih ettim.**

**API'mizdeki hava durumu bilgilerinin kaynağı için openweathermap isimli siteyi kullandım.**<br/>
[Openweahermap.org](https://openweathermap.org/)

### Uygulamamızın oluşturulması:
**1.adım:**<br/>
![(Görüntü yüklenmiyorsa lütfen linki kopyalayınız, tıklamayınız !)https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/1/1.PNG](https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/1/1.PNG)<br/>
**2.adım:**<br/>
![(Görüntü yüklenmiyorsa lütfen linki kopyalayınız, tıklamayınız !)https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/2/2.PNG](https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/2/2.PNG)<br/>
**3.adım:**<br/>
![(Görüntü yüklenmiyorsa lütfen linki kopyalayınız, tıklamayınız !)https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/3/3.PNG](https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/3/3.PNG)<br/>
**4.adım:**<br/>
![(Görüntü yüklenmiyorsa lütfen linki kopyalayınız, tıklamayınız !)https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/4/4.PNG](https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/4/4.PNG)<br/>
**5.adım:**<br/>
![(Görüntü yüklenmiyorsa lütfen linki kopyalayınız, tıklamayınız !)https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/5/5.PNG](https://github.com/AhmetFatihSarac/CaseStudy/blob/main/images/5/5.PNG)<br/>



## Görev(2): Uygulamanın Docker Üzerinden Containerize ve Build Edilmesi

### Docker ile Containerize işlemi:
**1.adım:**<br/>
**Öncelikle Dockerfile'ımızı  oluşturarak içerisine gerekli komutları yazıyoruz ve uygulamamızın olduğu klasöre ekliyoruz.**<br/>
![]()<br/>
**2.adım:**<br/>
**Kullandığımız sistem üzerinden shell'imize giriyoruz.(Docker'ın kurulu olması gerekir.)**<br/>
![]()<br/>
**3.adım:**<br/>
**cd komtu ile bulunduğumuz klasörden uygulamamızın klasörüne geçiş yapıyoruz.**<br/>
![]()<br/>
**4.adım:**<br/>
**` docker image build -t ahmetfatih024/casestudy .` komutu ile uygulamamızın image'ini oluşturduk.**<br/>
![]()<br/>
**5.adım:**<br/>
**`docker image push ahmetfatih024/casestudy` komutu ile oluşturduğumuz image'i DockerHub ortamına repository'me ekledim.**<br/>
![]()<br/>
**Daha sonra image'e ulaşmak istersek `docker pull ahmetfatih024/casestudy:latest` komutu ile DockerHub ortamından kendi sistemimize çekebiliriz.**<br/>
**6.adım:**<br/>
**Son olarak `docker container run  -p 5000:5000 ahmetfatih024/casestudy` komutu ile oluşturduğumuz image'den bir container ayağa kaldırarak uygulamamızı çalıştırdık.**<br/>
![]()<br/>
![]()<br/>


**AHMET FATİH SARAÇ**
