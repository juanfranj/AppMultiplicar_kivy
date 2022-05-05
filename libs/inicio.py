from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()


    def on_pre_enter(self, *args):
        self.app.title = "PequeMates"