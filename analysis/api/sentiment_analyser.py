import requests
from dotenv import load_dotenv
from flask import jsonify,request

load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"

def model(api_token=None):
    try:
        data = request.json.get('data')
        if api_token is None:
            return jsonify({"error":"Missing api token"})
        
        payload = {
            "inputs": data
        }
        print(payload)
        
        headers = {"Authorization": f"Bearer {api_token}"}
        
        bertweet_response = requests.post(API_URL, headers=headers, json=payload)
        
        print(bertweet_response)
        
        return bertweet_response.json()
	
    except Exception as e:
        raise e