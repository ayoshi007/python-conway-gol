import io
import math
import tkinter as tk
from tkinter import ttk
import ctypes

from PIL import Image
from conway_gol.grid import GridOfLife


WIDTH = 800
CANVAS_HEIGHT = 800
BUTTON_HEIGHT = 36
INIT_UPDATE_FREQ = 10
ALIVE_COLOR = 'black'
DEAD_COLOR = 'white'

BUTTON_IMAGES = {
    'Open':             Image.open('conway_gol/resources/open.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Save':             Image.open('conway_gol/resources/save.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Play':             Image.open('conway_gol/resources/play.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Pause':            Image.open('conway_gol/resources/pause.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Step forward':     Image.open('conway_gol/resources/step_forward.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Step backward':    Image.open('conway_gol/resources/step_backward.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Reset':            Image.open('conway_gol/resources/reset.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
    'Edit':             Image.open('conway_gol/resources/edit.png').resize(size=(BUTTON_HEIGHT, BUTTON_HEIGHT)),
}

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class UIOfLife(tk.Tk):
    def __init__(self, title='Conway\'s Game of Life', size=(WIDTH, CANVAS_HEIGHT + BUTTON_HEIGHT)):
        super().__init__()

        self.__set_window(title, size)
        self.__create_canvas()
        self.__create_menu_bar()
        self.__create_inputs()

        self._grid = GridOfLife(CANVAS_HEIGHT, WIDTH)

    def __set_window(self, title: str, size: tuple[int, int]):
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(height=False, width=False)

    def __create_canvas(self):
        self._dead_color = DEAD_COLOR
        self._alive_color = ALIVE_COLOR
        self._canvas = tk.Canvas(self, bg=self._dead_color)
        self._canvas.config(height=CANVAS_HEIGHT, width=CANVAS_HEIGHT)
        self._canvas.pack(side=tk.TOP)
    
    def __create_menu_bar(self):
        '''
        File:
            Open (Ctrl+O)
            Save (Ctrl+S)
            ---
            Exit
        '''
        self._menu_bar = tk.Menu(self)
        self._file_menu = tk.Menu(self._menu_bar, tearoff=0)
        self._file_menu.add_command(label='Open', accelerator='Ctrl+O')
        self._file_menu.add_command(label='Save', accelerator='Ctrl+S')
        self._file_menu.add_separator()
        self._file_menu.add_command(label='Exit', command=self.destroy)

        self._menu_bar.add_cascade(label='File', menu=self._file_menu)

        self.config(menu=self._menu_bar)
        pass

    def __create_inputs(self):
        '''
        Edit, Reset, Step back, Play/pause, Step forward, Open, Save, Speed, Zoom
        '''
        pass

    def draw(self):
        pass


def start():
    ui = UIOfLife()
    ui.draw()
    ui.mainloop()
