import tkinter as tk
from gui import Window

def main():
	window = Window(tk.Tk().geometry('600x600'))
	window.mainloop()

if __name__ == '__main__':
	main()