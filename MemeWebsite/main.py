from flask import Flask, requests, json, render_template

app = Flask(__name__)

def getMeme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route('/', methods=["GET"])
def index():
    meme_large, subreddit = getMeme()
    return render_template("index.html", meme_large = meme_large, subreddit = subreddit)

app.run(host ='0.0.0.0', port = 5000, debug = True)