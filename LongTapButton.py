from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import BooleanProperty, StringProperty

from Mybutton import MyButton


class LongTapButton(MyButton):
    activated = BooleanProperty(False)
    activated_theme = StringProperty('GREEN')
    disactivated_theme = StringProperty('PINK')

    def __init__(self, **kwargs):
        super(LongTapButton, self).__init__( **kwargs)
        self.bind(on_touch_up=self.delete_clock_of_long_tap)
        if kwargs.get('activated_theme'):
            self.activated_theme = kwargs.get('activated_theme')
        if kwargs.get('disactivated_theme'):
            self.disactivated_theme = kwargs.get('disactivated_theme')
        self.theme = self.disactivated_theme
        self.set_theme()

    def long_tapped(self, *args):
        if self.activated:
            self.text = "Disactivated"
            self.theme = self.disactivated_theme
            self.set_theme()
            self.activated = False
        else:
            self.text = "Activated"
            self.theme = self.activated_theme
            self.set_theme()
            self.activated = True

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.create_clock_of_long_tap(touch)

    def create_clock_of_long_tap(self, touch):
        touch.ud['event'] = Clock.schedule_once(callback=self.long_tapped, timeout=2)
        if self.collide_point(*touch.pos):
            self.my_sh = self.my_sh_pressed

    def delete_clock_of_long_tap(self, widget, touch):
        Clock.unschedule(touch.ud['event'])
        self.my_sh = self.my_sh_unpressed


class TApp(App):
    def build(self):
        return LongTapButton(text="Test", activated_theme='RARE',disactivated_theme='CONTRAST', type_button='BORDER')


if __name__ == "__main__":
    TApp().run()
