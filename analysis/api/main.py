'''from flask import Flask,jsonify,request
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
        action = request.json.get('action')
        if action == 'analyze':
            if os.getenv('API_TOKEN') is None:
                raise Exception("Api Token for the bert model not found")
        
        
            api_token = os.getenv('API_TOKEN')
        
            result = model(api_token=api_token)
            print(result)

        
            return jsonify({
                "result":result,
            })
        if action=='generate':
            if os.getenv('ANYSCALE_AUTH_KEY') is None:
                raise Exception("Anyscale Auth key not found")

            anyscale_auth_token = os.getenv('ANYSCALE_AUTH_KEY')
            response = prompt(anyscale_auth_key=anyscale_auth_token)
            return({
                "response":response
            })
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})
 
if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import os
from sentiment_analyser import model
from review_generator import prompt

app = Flask(__name__)
load_dotenv()
CORS(app)

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"

@app.route('/', methods=["POST"])
def analyse_review():
    try:
        action = request.json.get('action')  # Assuming the front-end sends an 'action' parameter

        if action == 'analyze':
            api_token = os.getenv('API_TOKEN')
            if api_token is None:
                raise Exception("API Token for the bert model not found")

            result = model(api_token=api_token)
            return jsonify({"result": result})

        elif action == 'generate':
            anyscale_auth_token = os.getenv('ANYSCALE_AUTH_KEY')
            if anyscale_auth_token is None:
                raise Exception("Anyscale Auth key not found")

            response = prompt(anyscale_auth_key=anyscale_auth_token)
            return jsonify({"response": response})

        else:
            raise Exception("Invalid action")

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

