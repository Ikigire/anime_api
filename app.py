from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
        <h1>Hola si funciona esto!</h1>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
