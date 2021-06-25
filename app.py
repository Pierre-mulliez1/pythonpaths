from flask import Flask, request
from ie_utils import tokenize


app = Flask(__name__)

@app.route("/")
def home():
    return {"message":'Hello Pierre'}

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
    
    
if __name__ == "main":
    import os
    port = int(os.environ["PORT"])
    #auto run on heroku
    app.run(host="0.0.0.0", port = port)
    
#export port = 3000

