import calendar
from datetime import datetime

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from MyCounter import MyCounter

Builder.load_string('''
<MyDatePicker>:
    orientation: 'vertical'
    dd: days
    mm: months
    yy: years
    confirm_button: butt
    spacing: self.height//15
    padding: self.height//20
    Label:
        text:"Выберите дату"
        font_size: "60dp"
        color: 0.1, 0.1, 0.1, 1
        size_hint_y: None
    BoxLayout:
        spacing: 10
        height: 200
        MyCounter:
            id: days
        MyCounter:
            id: months
            min_value: 1
            max_value: 12
        MyCounter:
            id: years
            min_value: 0
    MyButton:
        size_hint_y: 0.3
        size_hint_x: None
        width: "300dp"
        pos_hint: {'center_x': .5}
        id: butt
        text: "Потвердить"
        on_press:root.confirm()
''')


class MyDatePicker(BoxLayout):
    confirm_button = ObjectProperty()
    value = datetime.today()
    dd = ObjectProperty()
    mm = ObjectProperty()
    yy = ObjectProperty()

    today = datetime.today()

    def __init__(self, **kwargs):
        super(MyDatePicker, self).__init__(**kwargs)
        today = datetime.today()
        self.dd.value = today.day
        self.mm.value = today.month
        self.yy.value = today.year % 100
        self.mm.bind(value=self.change_window)
        self.yy.bind(value=self.change_window)
        self.dd.min_value = 0
        self.dd.max_value = MyDatePicker.days_in_month(today.year, today.month)

    def days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    def change_window(self, *args):
        if self.yy.value > 50:
            year = self.yy.value + 1900
        else:
            year = self.yy.value + 2000
        self.dd.max_value =  MyDatePicker.days_in_month(year, int(self.mm.value))
        if self.dd.max_value < self.dd.value:
            self.dd.value = self.dd.max_value


    def confirm(self):
        if self.yy.value > 50:
            year = self.yy.value + 1900
        else:
            year = self.yy.value + 2000
        self.value = f'{self.dd.value}-{self.mm.value}-{year}'
        print(self.value)

class RecycleApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyDatePicker()


if __name__ == '__main__':
    RecycleApp().run()
