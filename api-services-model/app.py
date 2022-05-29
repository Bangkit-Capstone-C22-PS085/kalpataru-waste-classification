import os
import io
import base64

import numpy as np
import tensorflow as tf

from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)
CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']


@app.route('/api/predict/', methods=['GET', 'POST'])
def image_predict():
    data = dict()
    if request.method == 'POST':
        try:
            image64 = request.form['b64']
            data = get_prediction_image(image64=image64)
            data['status'] = 'success'
        except KeyError:
            data['status'] = 'error'

    return data


def get_prediction_image(image64):
    model = __load_model()
    img = __prepocess_img(image64)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    predictions = model.predict(img_array)

    data = dict()
    data['predictions'] = dict()
    data['image'] = dict()

    data['image']['label'] = CLASS_NAMES[np.argmax(predictions[0])]
    data['image']['confidential'] = str(100 * np.max(predictions[0]))

    for i, score in enumerate(predictions[0]):
        score = 100 * score
        data['predictions'][CLASS_NAMES[i]] = str(score)

    return data


def __prepocess_img(image64):
    image = base64.b64decode(image64)
    image = Image.open(io.BytesIO(image))
    image = image.resize((180, 180), Image.ANTIALIAS).convert('RGB')
    return image


def __load_model():
    # change the path according to the environment
    model_dir = os.path.join(os.getcwd(), 'api-services-model', 'model_ml')
    model_name = 'trash-classification.h5'
    model_path = os.path.join(model_dir, model_name)
    model = tf.keras.models.load_model(model_path)
    return model


if __name__ == '__main__':
    app.run(host='0.0.0.0')
