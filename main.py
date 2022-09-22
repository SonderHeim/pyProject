from flask import Flask, render_template

app = Flask(__name__)


@app.route("/BearsHome")
def bearsHome():
    return render_template('BearsHome.html')

@app.route("/Home")
@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/aboutTeam")
def aboutTeam():
    return render_template('aboutTeam.html')

if __name__ == "__main__":
    app.run(debug=True)