import flask
import reddit

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    reddit.new_postings()
    return {'for_sale': reddit.postings}

reddit.setup()
app.run()
