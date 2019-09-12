from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get("search gif")
    results = get_results(query)
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", results = results)


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
    else:
        top_10gifs = None

    return top_10gifs

if __name__ == '__main__':
    app.run(debug=True)
