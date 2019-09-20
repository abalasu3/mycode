from flask import Flask,jsonify
import requests

app = Flask(__name__)

@app.route("/planets")
def planets():
    force_dict = {} 
    for i in range(1,11):
        force_json = requests.get(f'https://swapi.co/api/planets/{i}/?format=json').json()
        force_dict[force_json.get("name")] = force_json.get("climate") 
    return jsonify(force_dict)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5006)
