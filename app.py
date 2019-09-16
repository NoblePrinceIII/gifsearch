from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get("search gif")
    results = get_results(query)


    return render_template("index.html", results = results)


@app.route('/submit')
def get_results(query):
    # set the apikey and limit
    apikey = "3OGJ9M5CUDUK"  # test value
    limit = 10

    # get the top 10 GIFs for the search term
    r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (query, apikey, limit))


    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(r.content)
        top_10gifs = top_10gifs["results"]
    else:
        top_10gifs = None


    return render_template("index.html", top_10gifs = top_10gifs, )


if __name__ == '__main__':
    app.run(debug=True)
