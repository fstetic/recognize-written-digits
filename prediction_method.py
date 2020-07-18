import cv2
import numpy as np

def predict(model, points_coords, height, width):
	np.set_printoptions(suppress=True)  # don't use scientific notation
	full_image_array = [[points_coords.get((j,i),0) for j in range(height)] for i in range(width)]

	kernel = np.ones((20, 20), np.uint8)
	dilatation = cv2.dilate(np.float32(full_image_array), kernel, iterations=2)
	image_to_predict = cv2.resize(dilatation, (28,28))

	prediction = model.predict(np.expand_dims(image_to_predict, axis=0))
	return_predictions = {i: prediction[0][i]*100 for i in range(10)}
	return {k: v for k, v in sorted(return_predictions.items(), key=lambda item: item[1], reverse=True)}