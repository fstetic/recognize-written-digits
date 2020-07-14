import tensorflow as tf
import cv2
import numpy as np

def predict(matrix_coords, height, width):
	model = tf.keras.models.load_model('first_model')
