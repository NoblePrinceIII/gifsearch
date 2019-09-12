from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")


def get_results():
    # set the apikey and limit
apikey = "3OGJ9M5CUDUK"  # test value
limit = 10

# our test search
search_term = "excited"

# get the top 8 GIFs for the search term
r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, limit))

if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    top_10gifs = json.loads(r.content)
    print top_10gifs
else:
    top_10gifs = None





# continue a similar pattern until the user makes a selection or starts a new search.
















if __name__ == '__main__':
    app.run(debug=True)
