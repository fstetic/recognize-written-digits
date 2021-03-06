from flask import Flask, render_template, request, jsonify
import prediction_method
import tensorflow as tf

model = tf.keras.models.load_model('model')  # global is needed so model can be loaded only once
app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def start():
	return render_template("template.html")

@app.route('/script', methods=['POST'])
def predict():
	data = request.get_json()   # get list of coordinates
	prediction = prediction_method.predict(model, data, 500, 600)
	return jsonify(prediction)