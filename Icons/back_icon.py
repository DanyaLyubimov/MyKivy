import os

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class Icon(ButtonBehavior, Image):
    pressed = 'atlas://Icons/myatlas/img2_pressed'
    unpressed = 'atlas://Icons/myatlas/img2'

    def __init__(self, **kwargs):
        super(Icon, self).__init__(**kwargs)
        os.path.join(os.path.dirname(__file__), '', 'my_atlas.atlas')
        self.source = f'atlas://Icons/myatlas/img2'


    def wait_func(self, time):
            print('Wait')

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.source = self.pressed
            Clock.schedule_once(self.wait_func, 1)
        super(Icon, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.source = self.unpressed


class MApp(App):
    def build(self):
        return Icon()


if __name__ == '__main__':
    MApp().run()
