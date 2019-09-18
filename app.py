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

    r = requests.get( "https://api.tenor.com/v1/search?", params = payload)
    data = r.json()
    return render_template("index.html", data = data)


@app.route('/submit')
def get_results(query):
    # set the apikey and limit  

    # get the top 10 GIFs for the search term


    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(r.content)
        top_10gifs = top_10gifs["results"]
    else:
        top_10gifs = None


    return render_template("base.html", top_10gifs = top_10gifs)


if __name__ == '__main__':
    app.run(debug=True)
