import cv2
import numpy as np

def predict(model, list_of_points, height, width):
	np.set_printoptions(suppress=True)  # don't use scientific notation
	points_coords = {(point['row'], point['column']):1 for point in list_of_points}     # get dict from list of points
	full_image_array = [[points_coords.get((j,i),0) for j in range(height)] for i in range(width)]      # get full matrix from a sparse one

	kernel = np.ones((20, 20), np.uint8)
	dilation = cv2.dilate(np.float32(full_image_array), kernel, iterations=2)     # increase number thickness
	image_to_predict = cv2.resize(dilation, (28,28))                              # resize to dimensions used by model

	prediction = model.predict(np.expand_dims(image_to_predict, axis=(0,3)))    # expand to (1,28,28,1) array
	return {i: prediction[0][i]*100 for i in range(10)} # return percentage for each class