import tensorflow as tf
import tkinter as tk
from gui import Window

def main():
	# load in a pretrained model
	model = tf.keras.models.load_model('model')

	root = tk.Tk()  # initialize a window
	root.geometry("900x600+{}+{}".format(int(root.winfo_screenwidth()/2-450), int(root.winfo_screenheight()/2-300)))

	# makes elements behave normally when window is resized
	root.grid_rowconfigure(0,weight=1)
	root.grid_columnconfigure(0,weight=1)

	icon = tk.PhotoImage(file="icon.png")
	root.iconphoto(True, icon)

	window = Window(model, root)
	window.mainloop()

if __name__ == '__main__':
	main()