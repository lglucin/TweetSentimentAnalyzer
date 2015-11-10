from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Paiyge Sunnn!"

@app.route("/hello<name>")
def hello(name):
	return "SUP FOO %s" % name



if __name__ == "__main__":
    app.run()