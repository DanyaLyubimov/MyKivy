from kivy.app import App
from kivy.graphics import Color, BoxShadow, Line, RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

Builder.load_string('''
<MyTextInput>:
    hint_text: 'Введите запрос...'
    valign: 'middle'
    multiline: True
''')


class PickTextInput(TextInput):
    def __init__(self, **kwargs):
        super(PickTextInput, self).__init__(**kwargs)
        self.bind(pos=self.update_shape, size=self.update_shape, focus=self.on_focus)
        self.padding = (self.width // 4+5, 10)
        self.font_size = self.size[0] // 5

    def update_shape(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            color = Color(0, 0, 0, 1)
            RoundedRectangle(size = self.size, pos=self.pos,radius = [30])
            if self.focus:
                color = Color(1, 1, 1, 1)
            else:
                color = Color(0.9, 0.9, 0.9, 1)
            RoundedRectangle(size=[self.size[0]-8, self.size[1]-8], pos=[self.pos[0]+4, self.pos[1]+4], radius=[30])
            Color(0.15, 0.15, 0.15, 1)  # White background color

    def on_focus(self, instance, value):
        if self.focus:
            self.hint_text = ''
        elif self.text == '':
            self.hint_text = 'Введите запрос...'
        self.update_shape()

class MApp(App):
    def build(self):
        return PickTextInput()


if __name__ == '__main__':
    MApp().run()