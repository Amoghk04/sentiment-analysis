import requests
from flask import request,jsonify

s = requests.Session()
api_base = "https://api.endpoints.anyscale.com/v1"

def prompt(anyscale_auth_key=None):
    try:
        prompt = request.json.get('prompt')
        if anyscale_auth_key is None:
            return jsonify({'error': "Missing anyscale_api_token"})
        
        if prompt is None:
            return jsonify({'error': "No prompt provided"})
        print(prompt)
        url = f"{api_base}/chat/completions"
        body = {
            "model": "mistralai/Mistral-7B-Instruct-v0.1",
            "messages": [{"role": "system", "content": "You are a helpful assistant that generates reviews for products or responses to other topics based on user specification."},
                        {"role": "user", "content": f"""
                        You will be provided with exactly 2 phrases separated by an hyphen, 1 of them consists of a sentiment
                        which can be either 'positive','negative' or 'neutral'. The other phrase will
                        be of a product or a topic. Using these 2 words you have to generate a review 
                        or sentence.
                        Example Input 1: Positive - SmartPhone
                        Example output: The above mentioned SmartPhone is a marvelous product which makes our life way simpler 
                        by helping us carry out our day-to-day tasks very easily and efficiently
                        Example Input 2: Negative - World War 2
                        Example Output: The World War 2 was a devastating war for the humankind and one must refrain from 
                        causing any such events of mass destruction which will eventually lead to our extinction.
                         
                        Print the review with a max character cap of 50 *only* should not exceed it at any cost. Do not print anything else whatsover *ONLY THE REVIEW*.
                        *Do NOT even enter the starting phrase of 'Sure, I'd be happy to help! Here's my response to the input.*

                        Input: {prompt}
                        Output: <Review/Response
                        """} 
                        ],
            "temperature": 0.6
        }

        with s.post(url, headers={"Authorization": f"Bearer {anyscale_auth_key}"}, json=body) as resp:
            out = resp.json()['choices'][0]['message']['content']
    
        return out
    
    except Exception as e:
        raise e