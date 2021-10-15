from flask import Flask, send_file, render_template
from pathlib import Path
import os

app = Flask(__name__)

@app.route("/<id>")
def index(id) :
    if not os.path.isdir(Path("presentation/%s" % (id))) :
        return "<h1>Invalid ID</h1>"

    with open(Path("presentation/%s/keyframes.txt" % (id)), "r") as f :
        keyframes = f.read().split("\n")

    return render_template("main.html", id=id, keyframes=str(keyframes))

@app.route("/video/<id>")
def video(id) :
    if not os.path.isdir(Path("presentation/%s" % (id))) :
        return "<h1>Invalid ID</h1>"
    
    return send_file(Path("presentation/%s/video.mp4" % (id)))

app.run(threaded=True, host="0.0.0.0", port=5000)