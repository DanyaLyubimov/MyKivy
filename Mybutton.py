from functools import partial

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.properties import StringProperty, BoundedNumericProperty, \
    ListProperty, AliasProperty, BooleanProperty, NumericProperty, \
    OptionProperty, ReferenceListProperty
from kivy.graphics import *
from kivy.graphics import RoundedRectangle
from theming import THEMS_BORDER, THEMS_SHADOW

Builder.load_string('''
<Label>:
    color: (.9,.9,.9,1)
    
<MyButton>:

    background_normal:""
    background_color: (0, 0, 0, 0)
''')


class MyButton(Button):
    types_buttons = ['BORDER', 'SHADOW']
    my_bg = ListProperty([1, 1, 1, 1])
    my_sh_unpressed = [0.13, 0.59, 0.96, 1]
    my_sh = ListProperty([*my_sh_unpressed])
    my_sh_pressed = [0.08, 0.36, 0.8, 1]
    touch_bg_pressed = [15 / 255, 140 / 255, 220 / 255, 1]
    touch_bg_unpressed = [21 / 255, 153 / 255, 235 / 255, 1]
    touch_bg = ListProperty(touch_bg_unpressed)
    theme = StringProperty('RARE')
    type_button = StringProperty(types_buttons[0])

    def __init__(self, **kwargs):
        if kwargs.get('theme'):
            self.theme = kwargs['theme']
        if kwargs.get('type_button') and kwargs.get('type_button') in self.types_buttons:
            self.type_button = kwargs['type_button']
        super(MyButton, self).__init__(**kwargs)
        self.bind(text=self.onn_text)
        self.bind(pos=self.onr)
        self.set_theme()

    def set_theme(self):
        if self.type_button == 'BORDER' and THEMS_BORDER.get(self.theme):
            self.my_sh_pressed = THEMS_BORDER[self.theme]['SHADOW_PRESSED']
            self.my_sh_unpressed = THEMS_BORDER[self.theme]['SHADOW']
            self.touch_bg_pressed = THEMS_BORDER[self.theme]['BG_PRESSED']
            self.touch_bg_unpressed = THEMS_BORDER[self.theme]['BG']
            self.touch_bg = self.touch_bg_unpressed
            self.my_sh = self.my_sh_unpressed
        elif self.type_button == 'SHADOW' and THEMS_SHADOW.get(self.theme):
            self.my_sh_pressed = THEMS_SHADOW[self.theme]['SHADOW_PRESSED']
            self.my_sh_unpressed = THEMS_SHADOW[self.theme]['SHADOW']
            self.touch_bg_pressed = THEMS_SHADOW[self.theme]['BG_PRESSED']
            self.touch_bg_unpressed = THEMS_SHADOW[self.theme]['BG']
            self.touch_bg = self.touch_bg_unpressed
            self.my_sh = self.my_sh_unpressed

    def onr(self, index, value):
        self.update_canvas()

    def on_theme(self, index, value):
        self.set_theme()

    def on_type_button(self, index, value):
        self.set_theme()

    def onn_text(self, instance, value):
        self.font_size = self.size[0] // (len(value) if self.text != '' else 6) + 3

    def init(self, **kwargs):
        super(MyButton, self).init(**kwargs)

    def on_size(self, *args):
        self.update_canvas()

    def on_my_sh(self, *args):
        self.update_canvas()

    def draw_border(self):
        self.canvas.before.clear()
        self.font_size = self.size[0] // (len(self.text) if self.text != '' else 6) + 4
        if self.font_size > 0.75 * self.height:
            self.font_size = int(0.75 * self.height)
        with self.canvas.before:
            Color(*self.my_bg)
            Rectangle(size=self.size, pos=self.pos)
            Color(*self.my_sh)
            RoundedRectangle(size=(int(self.width * 0.95), int(self.height * 0.9)),
                             pos=(self.x + int(0.025 * self.width), self.y + int(0.05 * self.height)),
                             radius=[self.width / 15 + self.height / 15])
            Color(*self.touch_bg)
            RoundedRectangle(size=(int(self.width * 0.93), int(self.height * 0.9) - self.width * 0.02),
                             pos=(
                                 self.x + int(0.035 * self.width),
                                 self.y + int(0.05 * self.height) + self.width * 0.01),
                             radius=[self.width / 15 + self.height / 15])
            Color(1, 1, 1, 1)

    def draw_shadow(self):
        self.canvas.before.clear()
        self.font_size = self.size[0] // (len(self.text) if self.text != '' else 6) + 4
        if self.font_size > 0.75 * self.height:
            self.font_size = int(0.75 * self.height)
        with self.canvas.before:
            Color(*self.my_bg)
            Rectangle(size=self.size, pos=self.pos)
            Color(*self.my_sh)
            BoxShadow(size=(int(self.width * 0.95), int(self.height * 0.9)),
                      pos=(self.x + int(0.025 * self.width), self.y + int(0.05 * self.height)), spread_radius=(-2, -2),
                      border_radius=(self.width / 10, self.width / 10, self.width / 10, self.width / 10),
                      blur_radius=self.width / 20 + self.height / 20)
            Color(*self.touch_bg)
            RoundedRectangle(size=(int(self.width * 0.8), int(self.height * 0.8)),
                             pos=(self.x + int(0.1 * self.width), self.y + int(0.1 * self.height)),
                             radius=[self.width / 15 + self.height / 15])

    def update_canvas(self):
        if self.type_button == 'BORDER':
            self.draw_border()
        else:
            self.draw_shadow()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            bg_anim = Animation(touch_bg=self.touch_bg_pressed, d=0.1) + Animation(
                touch_bg=self.touch_bg_unpressed, d=0.1)
            sh_anim = Animation(my_sh=self.my_sh_pressed, d=0.1) + Animation(
                my_sh=self.my_sh_unpressed, d=0.1)
            bg_anim.start(self)
            sh_anim.start(self)
            # self.my_sh = self.my_sh_pressed
            super(MyButton, self).on_touch_down(touch)


class TApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        a =BoxLayout(padding="20dp")
        a.add_widget(MyButton(text="Test", type_button='SHADOW', theme='ELEGANT'))
        return a


if __name__ == "__main__":
    TApp().run()
