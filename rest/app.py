from flask import Flask, render_template
import util

app = Flask(__name__)


@app.route("/")
@app.route("/<city>")
def index(city="nyc"):
    temp = util.get_weather(city)
    photos = util.get_turtles()[0:10];
    d={'city':city,'temp':temp,'photos':photos}
    return render_template("index.html",d=d)



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
