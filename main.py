import tensorflow as tf
import tkinter as tk
from gui import Window

def main():
	# load in a pretrained model
	model = tf.keras.models.load_model('first_model')

	root = tk.Tk()  # initialize a window
	root.geometry("900x600")

	# makes elements behave normally when window is resized
	root.grid_rowconfigure(0,weight=1)
	root.grid_columnconfigure(0,weight=1)

	window = Window(model, root)
	window.mainloop()

if __name__ == '__main__':
	main()