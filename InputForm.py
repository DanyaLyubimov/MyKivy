from kivy.app import App
from kivy.atlas import Atlas
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, ColorProperty, StringProperty, BooleanProperty, \
    NumericProperty
from kivy.resources import resource_find
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from MyTextInput import MyTextInput

from Mybutton import MyButton

Builder.load_string('''
<InputForm>:
    form: form_text
    button: form_button
    halign: 'right'
    top: root.top
    orientation: "horizontal"
    padding: "5dp"
    spacing: "5dp"
    canvas.before:
        Color:
            rgba: self.bg
        RoundedRectangle:
            size: self.size
            radius: [10]
            pos: self.pos
    MyTextInput:
        id: form_text
        font_size: form_button.font_size if root.dinamic_font_size else f'{root.fs}dp'
        hint_text: 'Введите запрос...'
        valign: 'middle'
        multiline: False
        size_hint_x: 0.65
        on_text: root.clicked()
    MyButton:
        my_bg: root.bg
        id: form_button
        valign: 'middle'
        size_hint_x: 0.35
        text: root.b_text
        on_press: root.clicked()
''')


class InputForm(BoxLayout):
    fs = NumericProperty(15)
    dinamic_font_size = BooleanProperty(True)
    input_information = StringProperty()
    form = ObjectProperty()
    button = ObjectProperty()
    b_text = StringProperty('Search')
    bg = ColorProperty((0, 0, 0, 1))

    def clicked(self):
        self.input_information = self.form.text

class BaseApp(App):
    def build(self):
        return InputForm()


if __name__ == '__main__':
    BaseApp().run()
