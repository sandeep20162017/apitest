from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Read environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')
FILE_PATH = os.getenv('FILE_PATH')

@app.route('/get-file', methods=['GET'])
def get_file():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.raw'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_content = response.text
        return jsonify({'file_content': file_content})
    else:
        return jsonify({'error': 'Failed to fetch file from GitHub', 'status_code': response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
