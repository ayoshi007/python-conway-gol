import io
import PySimpleGUI as sg
from PIL import Image
from conway_gol.grid import GridOfLife


button_images = {
    'Open':             Image.open('conway_gol/resources/open.png').resize(size=(24, 24)),
    'Save':             Image.open('conway_gol/resources/save.png').resize(size=(24, 24)),
    'Play':             Image.open('conway_gol/resources/play.png').resize(size=(24, 24)),
    'Pause':            Image.open('conway_gol/resources/pause.png').resize(size=(24, 24)),
    'Step forward':     Image.open('conway_gol/resources/step_forward.png').resize(size=(24, 24)),
    'Step backward':    Image.open('conway_gol/resources/step_backward.png').resize(size=(24, 24)),
    'Reset':            Image.open('conway_gol/resources/reset.png').resize(size=(24, 24)),
    'Edit':             Image.open('conway_gol/resources/edit.png').resize(size=(24, 24)),
}
button_bytes_ios = {key: io.BytesIO() for key in button_images}
for key, val in button_images.items():
    val.save(button_bytes_ios[key], format='PNG')


def start():
    layout = [
        [sg.Canvas(size=(600, 400), key='canvas', background_color='red')],
        [
            sg.Button(image_source=button_bytes_ios['Edit'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Reset'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Step backward'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Play'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Step forward'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Open'].getvalue(), pad=(0, 0)),
            sg.Button(image_source=button_bytes_ios['Save'].getvalue(), pad=(0, 0)),
        ]
    ]
    window = sg.Window(title='Conway\'s Game of Life', layout=layout, resizable=True, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
