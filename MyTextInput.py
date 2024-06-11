from kivy.app import App
from kivy.graphics import Color, BoxShadow, Line
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


class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.bind(pos=self.update_shape, size=self.update_shape, focus=self.on_focus)
        self.padding = (self.width // 4+5, "10dp")
        self.font_size = self.size[0] // 5

    def on_enter(instance, value):
        print('User pressed enter in', instance)

    def update_shape(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            if self.focus:
                color = Color(1, 1, 1, 1)
            else:
                color = Color(0.9, 0.9, 0.9, 1)
            BoxShadow(size=(int(self.width * 0.95), int(self.height * 0.95)),
                      pos=(self.x + int(0.025 * self.width), self.y + int(0.025 * self.height)),

                      )
            Color(0, 0, 0, 1)

    def on_focus(self, instance, value):
        if self.focus:
            self.hint_text = ''
        elif self.text == '':
            self.hint_text = 'Введите запрос...'
        self.update_shape()


class BaseApp(App):
    def build(self):
        return MyTextInput()


if __name__ == '__main__':
    BaseApp().run()