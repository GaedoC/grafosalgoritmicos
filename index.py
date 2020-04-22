from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/in-gra')
def in_gra():
    return render_template('grafo.html')

if __name__ == '__main__':
    app.run(debug = True)