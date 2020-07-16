import tkinter as tk
import model

class Window(tk.Frame):
	def __init__(self, root=None):
		super().__init__(root)
		self.grid(sticky="nsew")
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1, weight=2)
		self.canvas = tk.Canvas(self, bg="white")
		self.canvas.grid(row=0,column=1, rowspan=10, sticky="nsew")
		self.labels, self.predictions_text  = list(), list()
		for i in range(10):
			self.grid_rowconfigure(i,weight=1)
			self.predictions_text.append(tk.StringVar())
			self.predictions_text[i].set("{}: x%".format(i))
			self.labels.append(tk.Label(self, bg="blue", fg="white", textvariable=self.predictions_text[i]))
			self.labels[i].grid(row=i,column=0, sticky="nsew")
		self.matrix_coords = dict()
		self.canvas.bind('<ButtonPress>', self.start_drawing)

	def start_drawing(self, event):
		self.canvas.old_coords = None
		self.matrix_coords.clear()
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
		if self.canvas.old_coords:
			x1, y1 = self.canvas.old_coords
			self.canvas.create_line(x, y, x1, y1)
			for p in self.get_points_in_line(x,y, x1, y1):
				self.matrix_coords[p] = 1
		self.canvas.old_coords = x, y

	# https://stackoverflow.com/questions/23930274/list-of-coordinates-between-irregular-points-in-python
	# Bresenham for getting all points
	@staticmethod
	def get_points_in_line(x0, y0, x1, y1):
		points_in_line = []
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2.0
			while x != x1:
				points_in_line.append((x, y))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2.0
			while y != y1:
				points_in_line.append((x, y))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		points_in_line.append((x, y))
		return points_in_line