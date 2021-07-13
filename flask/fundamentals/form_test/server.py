from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    
    print(request.form)
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    # request.form['name_of_input']
    print("Got Post Info")
    print(request.form)
    return redirect('/')
    


if __name__=="__main__":
    app.run(debug=True)