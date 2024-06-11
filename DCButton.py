from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import BooleanProperty, StringProperty

from Mybutton import MyButton


class DCButton(MyButton):
    activated = BooleanProperty(False)
    activated_theme = StringProperty('GREEN')
    disactivated_theme = StringProperty('PINK')


    def __init__(self, **kwargs):
        super(DCButton, self).__init__(**kwargs)
        self.register_event_type('on_double_press')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))
        if kwargs.get('activated_theme'):
            self.activated_theme = kwargs.get('activated_theme')
        if kwargs.get('disactivated_theme'):
            self.disactivated_theme = kwargs.get('disactivated_theme')
            self.theme = self.disactivated_theme
            self.set_theme()

    def on_double_press(self, *args):
        self.on_double_press_ofc()
        self.on_double_click()

    # Override this function
    def on_double_click(self):
        pass

    def on_double_press_ofc(self, *args):
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
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        Clock.schedule_once(lambda dt: MyButton.on_touch_down(self, touch), 0.2)


class TApp(App):
    def build(self):
        return DCButton(text="Test", activated_theme='CONTRAST', disactivated_theme='RARE')


if __name__ == "__main__":
    TApp().run()
