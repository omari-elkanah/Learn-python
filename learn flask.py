#learn flask
from flask import Flask,render_template

app = Flask(__name__)
app.route('/')
def index():
    return render_template('template.html')
    #print("Hello World")
if __name__ =="__main__":
    app.run(debug=True)
