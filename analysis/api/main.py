from flask import Flask,jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from sentiment_analyser import model
from review_generator import prompt

app = Flask(__name__)
CORS(app)
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
@app.route('/', methods=["POST","GET"])

def analyse_review():
    try:
        if os.getenv('API_TOKEN') is None:
            raise Exception("Api Token for the bert model not found")
        
        if os.getenv('ANYSCALE_AUTH_KEY') is None:
            raise Exception("Anyscale Auth key not found")

        api_token = os.getenv('API_TOKEN')

        anyscale_auth_token = os.getenv('ANYSCALE_AUTH_KEY')
        
        result = model(api_token=api_token)
        
        response = prompt(anyscale_auth_key=anyscale_auth_token)
        
        return jsonify({
            "result":result,
            "response":response
        })
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})
 
if __name__ == '__main__':
    app.run(debug=True)
