from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 align=center>CUBETIQ Solution</h1><br /><a href='/about'>About</a>"

@app.route("/about")
def about():
    return "<h1 align=center>Sambo Chea</h1>"

if __name__ == '__main__':
    app.run()