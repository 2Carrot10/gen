#!/bin/bash
import requests
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("question")
args = parser.parse_args()

url = "http://localhost:11434/api/generate" #https://127.0.0.1/
"""

curl http://localhost:11434/api/generate -d '{
"model": "phi3:mini",
"prompt": "why is the sky blu?",
"stream":"false"}'

    """
# Create the data payload
data = dict(
    model="qwen2.5-coder:1.5b",#"codellama:7b",
    prompt=args.question,
    stream=False
)

# Send the POST request
response = requests.post(url=url, json=data)
text = json.loads(response.text).get("response")
print(text)
