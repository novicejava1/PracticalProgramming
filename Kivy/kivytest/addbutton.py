import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MyButtonApp(App):
    def build(self):
        layout = BoxLayout(padding=50)

        with layout.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        
        layout.bind(pos=update_rect, size=update_rect)

        button1 = Button(text='Pinch Me')
        button2 = Button(text='Hit Me')
        layout.add_widget(button1)
        layout.add_widget(button2)

        for child in layout.children:
            print(child.text)

        return layout

if __name__ == '__main__':
    MyButtonApp().run()