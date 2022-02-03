from flask import Flask,render_template,request,jsonify
import json,requests 

app = Flask(__name__) 

@app.route("/") 
def index():
    return render_template("index.html") 

@app.route("/temperature", methods=["GET"]) 
def temperature():
    city = request.args.get('city') 
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=1ac4e0d72fc2d8cd8044a7eb187a3acd"
    r = requests.get(api) 
    data =json.loads(r.text) 
    kelvin = 273.15 
    result = (data["main"]["temp"]) - kelvin 
    result = round(result,2) 
    return jsonify(tempereature = result)
    
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
    