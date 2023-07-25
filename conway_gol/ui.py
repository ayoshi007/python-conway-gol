import tkinter as tk
from conway_gol.grid import GridOfLife


class UIOfLife:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Conway's Game of Life")

        menu_bar = tk.Menu(self.window)
        self.window.config(
            width=800, height=600,
            menu=menu_bar
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

        self.canvas = tk.Canvas(self.window, width=600, height=400, bg='grey')
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        self.button_frame = tk.Frame(self.window, relief=tk.RAISED, bg='grey')
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=5, pady=5)
        self.button_frame.
        open_button = tk.Button(self.button_frame, text="Open")
        open_button.pack(side=tk.RIGHT)
        save_button = tk.Button(self.button_frame, text="Save")
        save_button.pack(side=tk.RIGHT)


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
