import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello World', font_size=72)

if __name__ == '__main__':
    app = MyApp()
    app.run()