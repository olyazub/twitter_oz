from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/next", methods=["GET","POST"])
def next():
    from Zubyk_lab3_ex1 import findall
    request.args.get("acct")
    users = findall("location","acct")
    return render_template("Olha_Zubyk_twitmap.html")

if __name__=="main":
    app.run()
