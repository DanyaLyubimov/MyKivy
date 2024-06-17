from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<MyCard>:

    title: 'Title'

    orientation: "vertical"
    padding: self.width*0.1, self.height*0.1
    spacing: 10
    canvas:
        Color:
            rgb: 0.5, 0.7, 0.7, 0.5
        RoundedRectangle:
            size: self.size
            pos: self.pos
        Color:
            rgb: 1, 1, 1, 0.5
        BoxShadow:
            size: self.size
            pos: self.pos
            inset: True
    BoxLayout:
        size_hint_y: 0.3
        Label:
            size_hint_x:2.5
            font_size: "30dp"
            id: l2
            text: root.title
            halign: 'left'
            text_size: self.size
        Label:
            size_hint_x:1
            id: l1
            text: root.data
            halign: 'right'
            text_size: self.size
    Label:
        size_hint_y: 0.7
        id: l3
        valign: 'top'
        halign: 'left'
        text: root.description
        text_size: self.size
''')

class MyCard(ButtonBehavior, BoxLayout):
    title = StringProperty()
    data = StringProperty("23-12-2024")
    description =StringProperty("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
class RecycleApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        a = BoxLayout(padding="20dp")
        a.add_widget(MyCard())
        return a


if __name__ == '__main__':
    RecycleApp().run()