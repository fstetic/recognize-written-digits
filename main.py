import tkinter as tk
from gui import Window

def main():
	root = tk.Tk()
	root.geometry("900x600")
	root.grid_rowconfigure(0,weight=1)
	root.grid_columnconfigure(0,weight=1)
	window = Window(root)
	window.mainloop()

if __name__ == '__main__':
	main()