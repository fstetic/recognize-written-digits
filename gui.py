import tkinter as tk
import model

class Window(tk.Frame):
	def __init__(self, root=None):
		super().__init__(root)
		self.canvas = tk.Canvas(self, bg="white", height=500, width=500)
		self.canvas.pack()
		self.pack()
		self.canvas.bind('<ButtonPress>', self.start_drawing)
		self.matrix_coords = dict()

	def start_drawing(self, event):
		self.canvas.old_coords = None
		self.canvas.delete("all")
		self.canvas.bind('<Motion>', self.draw_line)
		self.canvas.bind('<ButtonRelease>', self.stop_drawing)

	def stop_drawing(self, event):
		self.canvas.unbind('<Motion>')
		self.canvas.unbind('<ButtonPress>')
		self.canvas.unbind('<ButtonRelease>')
		model.predict(self.matrix_coords, self.canvas.winfo_height(), self.canvas.winfo_width())
		self.canvas.bind('<ButtonPress>', self.start_drawing)

	# https://stackoverflow.com/questions/47996285/how-to-draw-a-line-following-your-mouse-coordinates-with-tkinter
	def draw_line(self, event):
		x, y = event.x, event.y
		self.matrix_coords[(x,y)] = 1
		if self.canvas.old_coords:
			x1, y1 = self.canvas.old_coords
			self.canvas.create_line(x, y, x1, y1)
		self.canvas.old_coords = x, y