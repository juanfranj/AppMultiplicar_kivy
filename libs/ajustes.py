from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDThemePicker

class Ajustes(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app= MDApp.get_running_app()

    def change_mode(self, checkbox, value):
        if value:
            self.app.theme_cls.theme_style = "Dark"
        else:
            self.app.theme_cls.theme_style = "Light"
    
    @staticmethod
    def show_theme_picker():
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    
    def on_pre_enter(self, *args):
        self.app.title = "Ajustes"