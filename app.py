from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get("search_gif")
    payload = {
        "q" : query,
        "key" : "3OGJ9M5CUDUK"
    }
    data = None

    r = requests.get( "https://api.tenor.com/v1/search", params = payload)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        data = r.json()
        data = data["results"]
    else:
        data = None
    return render_template("index.html", data = data)



    # set the apikey and limit  

    # get the top 10 GIFs for the search term


if __name__ == '__main__':
    app.run(debug=True)
