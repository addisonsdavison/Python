# from flask import Flask, render_template
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
    # return render_template("index.html")
# ------------------------

@app.route('/dojo')
def Dojo():
    return "Dojo!"

# ------------------------

@app.route('/say/<name>')
def Hello(name):
    # print(name)
    return "Hi, " + name + "!"

# ------------------------

@app.route('/repeat/<int:num>/hello')
def SayHello(num):
    print(type(num))
    return "Hello! " * num

# -------------------------

@app.route('/repeat/<int:num>/bye')
def SayBye(num):
    print(type(num))
    return "Bye " * num

# ---------------------------

@app.route('/repeat/<int:num>/dogs')
def Dogs(num):
    print(type(num))
    return "Dogs " * num






if __name__=="__main__":
    app.run(debug=True)