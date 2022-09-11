import config  # noqa
import os
from PIL import Image

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty


class LoadDialog(FloatLayout):
    cancel = ObjectProperty()
    search = ObjectProperty()


class MainScreen(Screen):
    loadfile = ObjectProperty()
    savefile = ObjectProperty()
    path = StringProperty()
    selection = StringProperty()

    def dismiss_popup(self):
        self._popup.dismiss()
        print(self.path)

    def show_load(self):
        content = LoadDialog(cancel=self.dismiss_popup, search=self.makePdf)
        self._popup = Popup(
            title='Choisissez un fichier',
            content = content,
            size_hint=(.9,.9)
        )
        self._popup.open()

    def makePdf(self, path):
        img_list = []
        pdf_path = f"{path}/images.pdf" 
        for file in os.listdir(path):
            if file.endswith('png'):
                file = Image.open(os.path.join(path, file))
                file = file.convert('RGB')
                img_list.append(file)
        img_list[0].save(
            pdf_path,
            'PDF',
            resolution=100.0,
            save_all=True,
            append_images=img_list
        )


Builder.load_file('screens/first_page.kv')
