from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whois', methods=['POST'])
def whois():
    return 'saved!'
app.run(debug=True, host='0.0.0.0', port=8000)
