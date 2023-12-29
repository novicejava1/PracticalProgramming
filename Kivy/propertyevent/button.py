import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyBoxLayout(BoxLayout):

    b1 = ObjectProperty(None)
    b2 = ObjectProperty(None)
    
    def callme(self):
        print("B1 - I was hit!!")
        self.b1.text = "I was hit"
    
    def pinchme(self):
        print("B2 - I was pinched!!")
        self.b2.text = "I was pinched"


class ButtonApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    ButtonApp().run()
