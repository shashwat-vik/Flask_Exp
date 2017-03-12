from app import app

@app.route("/")
def homepage():
    return "The only way in is out !"
