from flask import Flask, request
from ie_utils import tokenize


app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello Pierre'

 #if get no responce with sentence returns empty
@app.route("/toke")
def do_tokenize():
    print (request.args)
    sentence = request.args.get("sentence", "")
    lower = request.args.get("lower","F")
    try:
        return str(tokenize(sentence,lower=lower))
    except ValueError:
        return "[]"

