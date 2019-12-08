from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def on_about():
    return render_template("about.html")

@app.route("/portfolios")
def on_portfolios():
    return render_template("portfolios.html")

@app.route("/portfolios/fakebook")
def on_fakebook():
    return render_template("HW2_Fakebook_page.html")

@app.route("/portfolios/fakebook_sl")
def on_fakebook_sl():
    return render_template("HW2_Fakebook_page_slo.html")

@app.route("/portfolios/boogle")
def on_boogle():
    return render_template("Boogle_login.html")

if __name__ == "__main__":
    app.run()