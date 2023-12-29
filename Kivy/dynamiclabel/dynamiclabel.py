import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty

class DynamicLabel(Widget):
    stack = NumericProperty(0)

    def updatestring(self, dt):
        self.stack = self.stack + 1
        #self.techstack.text = "Hello " + str(self.stack) + "!!"
        self.techstack.text = str(self.stack)
        if self.stack == 10:
            return False

class DynamicLabelApp(App):
    def build(self):
        dynamiclabel = DynamicLabel()
        Clock.schedule_interval(dynamiclabel.updatestring, 1.0)
        return dynamiclabel

if __name__ == '__main__':
    DynamicLabelApp().run()