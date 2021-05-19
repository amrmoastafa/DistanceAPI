from flask import Flask,request
from flask_restful import Resource, Api
import requests
import json

#Importing API Key
api_key = 'AkKr73zALFQ7JyYWE84K4syg-1rCNyQsToIbW6BUK3ZPF-noh2emBttpjFdCl97l'
base_url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&"
#Home Address Input

app = Flask(__name__)
api = Api(app)

@app.route('/',methods=['GET','POST'])
def home():
    
    if request.method == 'GET':
        x = 0
        home = request.args.get('home')
        destination = request.args.get('destination')
        result = base_url + "wp.0=" + home + "&wp.1=" + destination + "&avoid=minimizeTolls&key="+ api_key
        r = requests.get(url = result)
        data = r.json()
        distance = data['resourceSets'][0]['resources'][0]
        for key, value in distance.items():
            if key == 'travelDistance':
                print(value)
                x = value
        ret = {
            "distance" : x
        }
        return ret
    return "Distance"

if __name__=='__main__':
    app.run(debug=True)