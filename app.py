from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
sns.set()
from datetime import datetime
import re
from flask import render_template, send_file
from io import BytesIO
import jinja2


app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"


# @app.route("/hello/<name>")
# def hello_there(name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return content

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/test")
def dataframe():
    df = pd.read_csv("data/heights.csv")
    return render_template("example.html",  data=df.head(5).to_html())


@app.route("/visualization/")
def visualization():
    fig, ax = plt.subplots()
    df = pd.read_csv("data/heights.csv")
    heights = np.array(df['height(cm)'])
    plt.hist(heights)
    
    # plt.plot(heights, color="blue", )
    plt.title("Height Distribution of Presidents of USA")
    plt.xlabel("height(cm)")
    plt.ylabel("Number")
    
    # return render_template("example.html",  data=df.head(5).to_html())
   
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)    
    return send_file(img, mimetype='img/png')


@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)