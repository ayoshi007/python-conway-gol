import tkinter as tk
from conway_gol.grid import GridOfLife


class UIOfLife:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Conway's Game of Life")

        menu_bar = tk.Menu(self.window)
        self.window.config(
            width=800, height=600,
            menu=menu_bar,
            background='black'
        )
        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label='Load pattern', accelerator='Ctrl+O')
        file_menu.add_command(label='Save pattern', accelerator='Ctrl+S')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.window.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)

        display_menu = tk.Menu(menu_bar, tearoff=False)
        display_menu.add_command(label='Show buttons', underline=1, accelerator='Ctrl+B')
        display_menu.add_command(label='Clear', accelerator='Ctrl+C')
        menu_bar.add_cascade(label='Display', menu=display_menu)

        self.canvas = tk.Canvas(self.window, width=600, height=400, highlightbackground='black', highlightthickness=1)
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        self.button_frame = tk.Frame(self.window, relief=tk.RAISED, bg='grey')
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=8, pady=2)

        open_button = tk.Button(self.button_frame, text='Open')
        open_button.pack(side=tk.RIGHT)
        save_button = tk.Button(self.button_frame, text='Save')
        save_button.pack(side=tk.RIGHT)
        play_pause_button = tk.Button(self.button_frame, text='Play/Pause')
        play_pause_button.pack(side=tk.RIGHT)
        step_forward_button = tk.Button(self.button_frame, text='Step forward')
        step_forward_button.pack(side=tk.RIGHT)
        step_backward_button = tk.Button(self.button_frame, text='Step backward')
        step_backward_button.pack(side=tk.RIGHT)
        clear_button = tk.Button(self.button_frame, text='Clear')
        clear_button.pack(side=tk.RIGHT)
        self.speed_var = tk.IntVar(value=10)
        self.speed_scale = tk.Scale(self.button_frame, label=f'{self.speed_var.get()}/s', showvalue=0, from_=1, to=100, orient=tk.HORIZONTAL, length=75, variable=self.speed_var)
        def update_label(val):
            self.speed_scale.config(label=f'{self.speed_var.get()}/s')
        self.speed_scale.config(command=update_label)
        self.speed_scale.set(self.speed_var.get())
        self.speed_scale.pack(side=tk.RIGHT)
        self.edit_button = tk.Button(self.button_frame, text='Edit')
        self.edit_button.pack(side=tk.RIGHT)


    def load_pattern(self):
        pass

    def save_pattern(self):
        pass

    def end_game(self):
        pass

    def show_buttons(self):
        pass

    def clear_grid(self):
        pass

    def toggle_editor(self):
        pass

    def step_forward(self):
        pass

    def step_backward(self):
        pass
    
    def start(self):
        self.window.mainloop()


def start():
    ui = UIOfLife()
    ui.start()
