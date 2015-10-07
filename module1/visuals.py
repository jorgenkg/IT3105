# encoding: utf-8
from Tkinter import *
from random import *

window_size               = 800
board_padding             = 0

BACKGROUND_COLOR_GAME     = "#e1f9d7"
BACKGROUND_COLOR_OBSTACLE = "#f36e81"
BACKGROUND_COLOR_OBSERVED = "#79e5c4"
BACKGROUND_COLOR_EXPANDED = "#39d9a7"
BACKGROUND_COLOR_ROBOT    = "#3993d9"
BACKGROUND_COLOR_GOAL     = "#ffc943"


class MapGUI(Frame):
    def __init__(self, screen_width, screen_height, board ):
        Frame.__init__(self)
        self.grid()
        self.master.title('Maze')
        self.grid_cells = []
        
        self.screen_width  = screen_width
        self.screen_height = screen_height
        
        self.initialize()
        self.update_view( board )
        
        
    def initialize(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=window_size, height=window_size)
        background.grid()
        for i in xrange(self.screen_height):
            grid_row = []
            for j in xrange(self.screen_width):
                cell = Frame(background, bg=BACKGROUND_COLOR_GAME, width=window_size/self.screen_width, height=window_size/self.screen_height)
                cell.grid(row=i, column=j, padx=board_padding, pady=board_padding)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_GAME, justify=CENTER, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
        
        self.prev_board = [[ 0 ] * self.screen_width] * self.screen_height
       
    def update_view(self, board ):
        for i, row in enumerate( board ):
            for j, n in enumerate( row ):
                if n == self.prev_board[i][j]:
                    # no repaint
                    continue
                if n == 0:
                    self.grid_cells[i][j].configure(
                                          text = "", 
                                          bg = BACKGROUND_COLOR_GAME )
                elif n==-1:
                    self.grid_cells[i][j].configure(
                                          #text = "%d" % (i*self.screen_height+j),
                                          bg = BACKGROUND_COLOR_OBSTACLE)
                elif n==1:
                    self.grid_cells[i][j].configure(
                                          #text = "%d" % (i*self.screen_height+j),
                                          bg = BACKGROUND_COLOR_OBSERVED)
                elif n==2  :
                    self.grid_cells[i][j].configure(
                                          #text = "%d" % (i*self.screen_height+j),
                                          bg = BACKGROUND_COLOR_EXPANDED)
                elif n==3  :
                    self.grid_cells[i][j].configure(
                                          #text = "%d" % (i*self.screen_height+j),
                                          bg = BACKGROUND_COLOR_GOAL)
                else:
                    self.grid_cells[i][j].configure(
                                          #text = "%d" % (i*self.screen_height+j),
                                          bg = BACKGROUND_COLOR_ROBOT)
        self.update_idletasks()
        self.prev_board = board