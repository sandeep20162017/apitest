from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_TOKEN = 'xyz'  # Replace with your GitHub personal access token
REPO_OWNER = 'sandeep20162017'  # Replace with your GitHub username
REPO_NAME = 'gcp-api'  # Replace with your repository name
FILE_PATH = 'test/test.txt'  # Replace with the path to your file in the repository

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
        return jsonify({'error': 'Failed to fetch file from GitHub'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)