from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/ugc/group/<int:group_id>')
def get_group_items(group_id):
    url = f"https://catalog.roblox.com/v1/search/items?CreatorType=Group&CreatorTargetId={group_id}&Limit=50&category=11&Subcategory=21"
    headers = { "User-Agent": "UGCProxy/1.0" }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()