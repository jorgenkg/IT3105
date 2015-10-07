from Tkinter import *
from random import *

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = { 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", 512:"#edc850", 1024:"#edc53f", 2048:"#FFAE00", 4096:"#FFAE00", 8192:"#FFAE00", 16384:"#FFAE00", 32768:"#FFAE00", 65536:"#FFAE00" }
CELL_COLOR_DICT = {       2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", 32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", 512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2", 4096:"#f9f6f2", 8192:"#f9f6f2", 16384:"#f9f6f2", 32768:"#f9f6f2", 65536:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")



class GameWindow(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        
        self.grid_cells = []
        self.init_grid()
        self.update_grid( (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) )

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                # font = Font(size=FONT_SIZE, family=FONT_FAMILY, weight=FONT_WEIGHT)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
       
    def update_view(self, board ):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = 1 << board[i*4+j] if board[i*4+j]!=0 else 0
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()
