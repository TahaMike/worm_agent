import requests
from config import OLLAMA_URL, MODEL

def query_ollama(prompt):
    res = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"]