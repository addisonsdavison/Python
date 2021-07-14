from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ="keep it secret, keep it safe"

@app.route('/')
def Counter():
    if "number" in session:
        session['number'] += 0
    else:
        session['number'] = 0
    return render_template("index.html")

@app.route('/add', methods = ['POST'])
def add():
    session['number'] += 1
    return redirect('/')



@app.route('/destroy_session', methods = ['POST'])
def reset():
    session['number'] = 1
    return  redirect('/')











if __name__=="__main__":
    app.run(debug=True)