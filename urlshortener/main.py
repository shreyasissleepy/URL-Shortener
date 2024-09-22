from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    url = requests.get('https://api.waifu.pics/sfw/waifu').json()['url']
    return render_template('index.html',url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
