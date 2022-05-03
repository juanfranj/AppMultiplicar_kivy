from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivymd.app import MDApp


class Puzle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.app.title = "Puzle"
    
    def on_kv_post(self, base_widget):
        grid = self.ids["puzle"]
        for celda in range(0,42):
            self.label = self.celda_inicio(celda)
            grid.add_widget(self.label)
    
    def celda_inicio(self,celda):
        # with self.canvas.before:
        #     # Setting background of banner in a scroll screen
        #     Color(rgba=(1, .4, 0, 0.1))
        #     self.rect = RoundedRectangle(radius=[(40.0, 40.0), (40.0, 40.0), (40.0, 40.0), (40.0, 40.0)])
        # self.bind(pos=self.update_rect, size=self.update_rect)

        label = Label(text = f"{celda}")
        label.font_style = "H6"
        label.color_background = (0, .33, 0, 1)

        with label.canvas:
            # Setting background of banner in a scroll screen
            Color(rgba=(1, .4, 0, 0.1))
            RoundedRectangle(radius=[(40.0, 40.0), (40.0, 40.0), (40.0, 40.0), (40.0, 40.0)])

        return label

    # Setting background banner
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

