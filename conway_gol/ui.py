import io
import math
import platform
import ctypes
import tkinter as tk
from tkinter import font
from tkinter import ttk

from PIL import Image, ImageTk
from conway_gol.grid import GridOfLife

PLATFORM = platform.system()
INIT_UPDATE_FREQ = 10
RESOURCE_PATH = 'conway_gol/resources'


class UIOfLife(tk.Tk):
    def __init__(self, title='Conway\'s Game of Life'):
        super().__init__()
        self.__configure_platform()
        self.__get_images()
        self.__set_styles()
        self.__set_window(title)
        self.__create_canvas()
        self.__create_menu_bar()
        self.__create_inputs()

        self._grid = GridOfLife(self._canvas_height, self._width)
    
    def __configure_platform(self):
        self._width = 1000 if PLATFORM == 'Windows' else 1600
        self._canvas_height = 1000 if PLATFORM == 'Windows' else 1600
        self._font_size = 12 if PLATFORM == 'Windows' else 36
        self._button_height = 48 if PLATFORM == 'Windows' else 72
        self._alive_color = 'black'
        self._dead_color = 'white'
        self._icon_path = f'{RESOURCE_PATH}/icon.ico' if PLATFORM == 'Windows' else f'{RESOURCE_PATH}conway_gol/resources/icon.xpm'

    def __get_images(self):
        self._button_images = {
            'Open':             ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/open.png').resize(size=(self._button_height, self._button_height))),
            'Save':             ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/save.png').resize(size=(self._button_height, self._button_height))),
            'Play':             ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/play.png').resize(size=(self._button_height, self._button_height))),
            'Pause':            ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/pause.png').resize(size=(self._button_height, self._button_height))),
            'Step forward':     ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/step_forward.png').resize(size=(self._button_height, self._button_height))),
            'Step backward':    ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/step_backward.png').resize(size=(self._button_height, self._button_height))),
            'Reset':            ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/reset.png').resize(size=(self._button_height, self._button_height))),
            'Edit':             ImageTk.PhotoImage(Image.open(f'{RESOURCE_PATH}/edit.png').resize(size=(self._button_height, self._button_height))),
        }

    def __set_styles(self):
        self._font = ('Calibri', self._font_size)
        self._root_style = ttk.Style()
        self._root_style.configure('.', font=self._font, padx=0, pady=0)

        self._button_style = ttk.Style()
        self._button_style.configure('GOL.TButton')
        self._slider_style = ttk.Style()
        self._slider_style.configure('GOL.Horizontal.TScale', padx=12, pady=4)
        if PLATFORM == 'Windows':
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def __set_window(self, title: str):
        self.title(title)
        self.iconbitmap(default=self._icon_path)
        self.resizable(height=False, width=False)

    def __create_canvas(self):
        self._canvas = tk.Canvas(self, bg=self._dead_color)
        self._canvas.config(height=self._canvas_height, width=self._canvas_height)
        self._canvas.pack(side=tk.TOP)
    
    def __create_menu_bar(self):
        '''
        File:
            Open (Ctrl+O)
            Save (Ctrl+S)
            ---
            Exit
        '''
        self._menu_bar = tk.Menu(self, font=self._font)
        self._file_menu = tk.Menu(self._menu_bar, tearoff=0, font=self._font)
        self._file_menu.add_command(label='Open', accelerator='Ctrl+O')
        self._file_menu.add_command(label='Save', accelerator='Ctrl+S')
        self._file_menu.add_separator()
        self._file_menu.add_command(label='Exit', command=self.destroy)

        self._menu_bar.add_cascade(label='File', menu=self._file_menu)

        self.config(menu=self._menu_bar)

    def __create_inputs(self):
        '''
        Edit, Reset, Step back, Play/pause, Step forward, Open, Save, Speed, Zoom
        '''
        self._input_frame = ttk.Frame(self)
        self._input_frame.config(width=self._width, height=self._button_height)
        
        self._edit_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Edit'])
        self._edit_button.pack(side=tk.LEFT)

        self._reset_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Reset'])
        self._reset_button.pack(side=tk.LEFT)

        self._step_back_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Step backward'])
        self._step_back_button.pack(side=tk.LEFT)

        self._is_playing = False
        self._play_pause_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Play'], command=self.__play_pause)
        self._play_pause_button.pack(side=tk.LEFT)

        self._step_forward_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Step forward'])
        self._step_forward_button.pack(side=tk.LEFT)

        self._open_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Open'])
        self._open_button.pack(side=tk.LEFT)

        self._save_button = ttk.Button(self._input_frame, style='GOL.TButton', image=self._button_images['Save'])
        self._save_button.pack(side=tk.LEFT)

        self._speed_slider_frame = ttk.Frame(self._input_frame, padding=(12, 0))

        self._speed_value = INIT_UPDATE_FREQ
        self._speed_label = ttk.Label(self._speed_slider_frame, text=f'Speed: {self._speed_value}')
        self._speed_label.pack(side=tk.TOP)
        self._speed_slider = ttk.Scale(self._speed_slider_frame, style='GOL.Horizontal.TScale', from_=1, to_=100, variable=self._speed_value, command=self.__change_speed)
        self._speed_slider.set(self._speed_value)
        self._speed_slider.pack(side=tk.BOTTOM)

        self._speed_slider_frame.pack(side=tk.LEFT)

        self._zoom_slider_frame = ttk.Frame(self._input_frame, padding=(12, 0))

        self._zoom_value = 1.0
        self._zoom_label = ttk.Label(self._zoom_slider_frame, text=f'Zoom: {self._zoom_value}')
        self._zoom_label.pack(side=tk.TOP)
        self._zoom_slider = ttk.Scale(self._zoom_slider_frame, style='GOL.Horizontal.TScale', from_=0.01, to_=10, variable=self._zoom_value, command=self.__zoom)
        self._zoom_slider.set(self._zoom_value)
        self._zoom_slider.pack(side=tk.BOTTOM)

        self._zoom_slider_frame.pack(side=tk.LEFT)

        self._input_frame.pack(fill='x')

    def __play_pause(self):
        if self._is_playing:
            self._play_pause_button.config(image=self._button_images['Play'])
        else:
            self._play_pause_button.config(image=self._button_images['Pause'])
        
        self._is_playing = not self._is_playing

    def __zoom(self, v):
        self._zoom_label.config(text=f'Zoom: {round(float(v), ndigits=1)}')
    
    def __change_speed(self, v):
        self._speed_value = round(float(v))
        self._speed_label.config(text=f'Speed: {self._speed_value}')

    def draw(self):
        pass


def start():
    ui = UIOfLife()
    ui.draw()
    ui.mainloop()

