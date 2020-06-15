import tkinter as tk
from tkinter import font
from math import sqrt
from sudoku import solver

class Sudoku:
	board = [[3,6,0,0,4,0,2,0,0],
			 [0,0,7,0,0,9,3,8,0],
			 [0,0,9,0,0,0,6,0,0],
			 [1,2,0,0,6,0,7,5,3],
			 [9,0,0,1,0,8,4,2,0],
			 [0,0,6,5,0,3,0,9,0],
			 [7,5,0,0,9,1,0,6,0],
			 [0,9,0,0,0,2,0,3,0],
			 [8,1,2,0,5,6,9,4,0]]

	# board = [[0,3,4,0],[4,0,0,2],[1,0,0,3],[0,2,1,0]] // Try this board too
	board_len = len(board)
	board_cell = int(sqrt(board_len))
	height = width = (25/36) * 720
	zeros = []

	# Creates the grid structure and populates each cell
	def __init__(self,root):
		root.title("Sudoku Solver")
		frame = tk.Frame(root, height = 720, width = 600, bg="white")
		frame.pack()

		canvas = tk.Canvas(frame, bg = "white", highlightthickness = 4, highlightbackground = "black")
		canvas.place(relx = 1/12, rely = 5/72, relheight = 25/36, relwidth = 5/6)
		px = py = 0


		for i in range(self.board_len):
			if i%self.board_cell == 0 and i != 0:
				canvas.create_line(0,py,self.width,py, width = 4)
				canvas.create_line(px,0,px,self.height, width = 4)
			else:
				canvas.create_line(0,py,self.width,py)
				canvas.create_line(px,0,px,self.height)
			py += self.height/self.board_len
			px += self.width/self.board_len

		self.populate(canvas)

			
		button = tk.Button(frame, text="Solve Puzzle!", font=("Arial", 18), command = lambda: self.solve(canvas))
		button.place(relx = 1/3, rely = 5/6, relwidth = 1/3, relheight = 5/72)

	# Method used to populate initial Sudoku grid
	def populate(self,canvas):
		px = py = self.width/(2*self.board_len)
		for i in range(self.board_len):
			for j in range(self.board_len):
				if self.board[i][j] != 0:
					canvas.create_text(px, py, text = str(self.board[i][j]), font=("Arial", 18))
				else:
					self.zeros.append([i,j,px,py])
				px += self.width/self.board_len
			px = self.width/(2*self.board_len)
			py += self.height/self.board_len

	# Method called when solve button is pressed to populate empty cells with solution
	def solve(self,canvas):
		if solver(self.board):
			for i in self.zeros:
				canvas.create_text(i[2], i[3], text = str(self.board[i[0]][i[1]]), font=("Arial", 18))
		else:
			print("No solution")



if __name__ == "__main__":
	root = tk.Tk()
	main = Sudoku(root)
	root.mainloop()