from flask import Flask
import tensorflow  as tf

app = Flask(__name__)


@app.route('/')
def main():
    return "Predict"


def __load_model():
    tf.keras.models.load_model('path')
    return 0

if __name__ == '__main__':
    app.run(host='0.0.0.0')
