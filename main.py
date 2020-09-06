import os
from flask import Flask, render_template, request, jsonify

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'prediction.sqlite'),
	)

	@app.route('/predict')
	def start():
		return render_template("template.html")

	@app.route('/script', methods=['POST'])
	def predict():
		data = request.get_json()
		prediction = {1:12.3, 3:12.444, 2:13.1231, 7:14.124, 9:15.541, 8:11.245, 0:11.321, 6:14.444, 4:4.121, 5:2.21321}
		return jsonify(prediction)

	return app