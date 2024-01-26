from flask import Flask,jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os
from model import model

app = Flask(__name__)
CORS(app)
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
@app.route('/', methods=["POST","GET"])

def analyse_review():
    try:
        if os.getenv('API_TOKEN') is None:
            raise Exception("Api_Token for the bert model not found")
        
        api_token = os.getenv('API_TOKEN')
        result = model(api_token=api_token)
        return jsonify({"result":result})
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})
 
if __name__ == '__main__':
    app.run(debug=True)
