from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Our First Print ... //Our Last print..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
