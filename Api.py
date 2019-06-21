from flask import Flask

app = Flask(__name__)


@app.route('/price')
def Hello():
    return "hello_world"
    

if __name__ == '__main__':
    app.run()
