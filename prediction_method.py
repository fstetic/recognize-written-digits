import cv2
import numpy as np

def predict(model, matrix_coords, height, width):
	np.set_printoptions(suppress=True)  # don't use scientific notation
	full_coords = list()
	for i in range(width):
		full_coords.append([])
		for j in range(height):
			full_coords[i].append(matrix_coords.get((j,i),0))
	kernel = np.ones((20, 20), np.uint8)
	dilatation = cv2.dilate(np.float32(full_coords), kernel, iterations=2)
	prediction_image = cv2.resize(dilatation, (28,28))
	prediction = model.predict(np.expand_dims(prediction_image, axis=0))
	return_predictions = dict()
	for i in range(10):
		return_predictions[i] = prediction[0][i]*100
	return {k: v for k, v in sorted(return_predictions.items(), key=lambda item: item[1], reverse=True)}
