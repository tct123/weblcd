from nicegui import *
import gpiozero as gz

"""
My first application
"""


class WebLCD:
    def __init__(self, pin):
        self.pin = pin

    def gui(self):
        @ui.page("/")
        def home():
            textfield = ui.input(placeholder="input")

    ui.run()


def main():
    myapp = WebLCD(pin=1)
    myapp.gui()
