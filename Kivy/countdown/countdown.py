from time import sleep
import kivy
kivy.require('2.0.0')

from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class MyWidget(Widget):

    counter = ObjectProperty(0)

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
    
    def update(self, dt):
        self.counter.text = str(int(self.counter.text) + 1)
        #print(self.counter.text)

        if self.counter.text == "10":
            return False

class countdownApp(App):
    def build(self):
        countdown = MyWidget()
        Clock.schedule_interval(countdown.update, 1)
        return countdown

if __name__ == '__main__':
    countdownApp().run()
