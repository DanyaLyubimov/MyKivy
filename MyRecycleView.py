from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from MyCard import MyCard

Builder.load_string('''
<NewRecycleView>:
    viewclass: 'MyCard'
    RecycleBoxLayout:
        padding: 30, 10
        spacing: 10
        background_color: (0.8, 0.8, 0.8, 1)
        default_size: None, dp(130)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class NewRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(NewRecycleView, self).__init__(**kwargs)
        self.data = [{'data': str('Date: 22-02-22'),
                      'title': str('Title'),
                      'description': str('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor')} for _ in range(7)]



class RecycleApp(App):
    def build(self):
        return NewRecycleView()


if __name__ == '__main__':
    RecycleApp().run()
