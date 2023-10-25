from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route("/")
def index():
    def get_current_time():
        while True:
            yield datetime.now().strftime("%A, %B %d %Y %H:%M:%S")
            time.sleep(1)

    return render_template("index.html", current_time=get_current_time())

if __name__ == "__main__":
    app.run(debug=True)
