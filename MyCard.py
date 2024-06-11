from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<MyCard>:
    data: 'Data'
    title: 'Title'
    description: 'Information'
    orientation: "vertical"
    padding: 10, 10
    spacing: 10
    canvas:
        Color:
            rgb: 0.5, 0.5, 0.5, 1
        RoundedRectangle:
            size: self.size
            pos: self.pos
        Color:
            rgb: 1, 1, 1, 1
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
    pass

class RecycleApp(App):
    def build(self):
        return MyCard()


if __name__ == '__main__':
    RecycleApp().run()