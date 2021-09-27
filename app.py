from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    key = random.choice(list(image_urls_map))
    return render_template("index.html", cdac_project_url=image_urls_map, image_url=key)


if __name__ == "__main__":
    app.run(host="0.0.0.0")