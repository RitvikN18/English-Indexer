import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from indexer import func
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods=["POST", "GET"])
def handle_data():
    if request.method == "POST":
        files = request.files.getlist("file")
        name = []

        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join("uploads", filename))
            name.append(filename)
        print(name)
        savage = func(name)
        arr = []
        for x in savage:
            arr.append(x)
            arr.sort()
        for x in arr:
            print(x)
            for y in savage:
                if x == y:
                    for z in savage[y]:
                        print(z, ":", savage[y][z])
        return render_template("result.html", savage=savage, arr=arr)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
