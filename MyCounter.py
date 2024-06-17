from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from Mybutton import MyButton

Builder.load_string('''
<MyCounter>:
    incr_button: incr_button
    decr_button: decr_button
    orientation: 'horizontal'
    Label:
        id: board
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        text: '0'+str(root.value) if root.value in [_ for _ in range(10)] else str(root.value)
        color: 0, 0, 0, 1
        font_size: (self.height if self.height < 2*self.width else self.width) // len(board.text)
    BoxLayout:
        size_hint_x: 0.5
        orientation: 'vertical'
        MyButton:
            id:incr_button
            text: '+'
            theme: 'GREEN'
            type_button: 'BORDER'
            on_press: root.incr_value(1)
        MyButton:
            id:decr_button
            text: '-'
            theme: 'CONTRAST'
            type_button: 'BORDER'
            on_press: root.incr_value(-1)
''')


class MyCounter(BoxLayout):
    max_value = NumericProperty(100)
    min_value = NumericProperty(-99)
    value = NumericProperty(0)
    board = ObjectProperty()
    incr_button = ObjectProperty()
    decr_button = ObjectProperty()

    def __init__(self, **kwargs):
        super(MyCounter, self).__init__(**kwargs)
        self.bind(on_touch_up=self.delete_clock_up)
        self.bind(on_touch_down=self.create_clock_up)

    def delete_clock_up(self, widget, touch):
        if touch.ud.get('first_event'):
            Clock.unschedule(touch.ud['first_event'])
        if touch.ud.get('event') is not None:
            Clock.unschedule(touch.ud['event'])

    def incr_value(self, value):
        temp =self.value + value
        if temp > self.max_value:
            self.value = self.min_value
        elif temp < self.min_value:
            self.value = self.max_value
        else:
            self.value += value

    def incr_cycle(self, touch, value):
        touch.ud['event'] = Clock.schedule_interval(lambda dt: self.incr_value(value), 0.1)

    def create_clock_up(self, widget, touch):
        if self.incr_button.collide_point(*touch.pos):
            touch.ud['first_event'] = Clock.schedule_once(lambda dt: self.incr_cycle(touch, 1), 1)
        elif self.decr_button.collide_point(*touch.pos):
            touch.ud['first_event'] = Clock.schedule_once(lambda dt: self.incr_cycle(touch, -1), 1)

class TApp(App):
    def build(self):
        return MyCounter()


if __name__ == "__main__":
    TApp().run()
