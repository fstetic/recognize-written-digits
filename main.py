import tensorflow as tf
import tkinter as tk
from gui import Window

def main():
	model = tf.keras.models.load_model('first_model')
	root = tk.Tk()
	root.geometry("900x600")
	root.grid_rowconfigure(0,weight=1)
	root.grid_columnconfigure(0,weight=1)
	window = Window(model, root)
	window.mainloop()

if __name__ == '__main__':
	main()