import requests as requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Api!'


def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


@app.route('/Scoring/<string:x>')
def hell(x):
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-xlm-roberta-base-sentiment"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    # x = "I like you. I love you"
    output = query({
        "inputs": x, })
    sorted_response = sorted(output[0], key=lambda x: x['score'], reverse=True)
    highest_label = sorted_response[0]['label']
    if highest_label == 'positive':
        return str(2)
    if highest_label == 'neutral':
        return str(1)
    else:
        return str(0)


if __name__ == '__main__':
    app.run()
