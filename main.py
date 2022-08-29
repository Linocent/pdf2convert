from kivy.app import App

from screens import *


class Converter(App):
    def build(self):
        self.title = "Converter"


if __name__ == "__main__":
    Converter().run()
