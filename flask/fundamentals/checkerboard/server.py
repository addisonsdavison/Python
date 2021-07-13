from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def FirstBoard():
    return render_template("checkerboard.html", rows=8, columns=8)

@app.route('/<int:y>')
def SecondBoard(y):
    return render_template("checkerboard.html", rows=8, columns=y)


@app.route('/<int:x>/<int:y>')
def ThirdBoard(x,y):
    return render_template("checkerboard.html", rows=x, columns=y)



if __name__=="__main__":
    app.run(debug=True)

