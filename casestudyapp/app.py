from flask import Flask,render_template,request,jsonify
import json,requests # Flask Framework ve uygulama için gerekli kütüphaneleri ekliyoruz.


app = Flask(__name__) # Flask'ın şablonlar ve statik dosyalar gibi kaynakları nerede arayacağını bilmesi için burası gereklidir.


@app.route("/") # Burada ise başlangıç sayfamızı oluşturduk.
def index():
    return render_template("index.html") # Burası ise başlangıç sayfamızın içeriğinin index.html dosyası üzerinden çalışmasını sağladık.

@app.route("/temperature", methods=["GET"]) # Burada ise 'temperature' isimli endpoint'i oluşturduk ve sadece GET isteği alınmasını sağladık.
def temperature():
    city = request.args.get('city') # Burada GET metodu üzerinden 'city' isimli parametrenin alınmasını sağladık.

    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=1ac4e0d72fc2d8cd8044a7eb187a3acd"
    # Burada ise havadurumu bilglilerinin kaynağı olan siteye 'city' parametresi ile ekleme yaparak gerekli şehrin bilgilerinin alınmasını sağladık. 

    r = requests.get(api) # Almış olduğumuz bilgileri 'r' isimli değişkene atadık.
    data =json.loads(r.text) # Burada 'r' değişkenimizin json formatındaki verilerini 'data' isimli değişkenine text olarak çevirdik.
    kelvin = 273.15 # Derece (Celsius) sıcaklık biriminin hesaplanması için Kelvin değerini 'kelvin' isimli değişkene atadık.

    result = (data["main"]["temp"]) - kelvin 
    """ Burada ise 'data' değişkeninin içerisinde bulunan Kelvin değerindeki sıcaklık bilgisini çektik ve oluşturduğumuz 'kelvin' değerinden çıkardık.
        Böylece kelvin değerini celsius'a çevirdik ve bu değeri 'result' değişkenine atadık.
    """

    result = round(result,2) # Oluşturduğumuz 'result' değişkenindeki sayının virgülden sonraki son hanesinin 2 olarak kalmasını sağladık.
    return jsonify(tempereature = result)# Burada ise son olarak sayfamızın belirli parametreler girilerek 'result' değerini döndürmesini sağladık.
    
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
    # Son olarak uygulamamızın hızlı ve hatasız çalışması için değerler girdik ve host değerini belirledik.