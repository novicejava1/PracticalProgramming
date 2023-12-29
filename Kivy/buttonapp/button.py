from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class ButtonApp(App):
    def build(self):
        parent = GridLayout(cols=2)
        b1 = Button(text='Hello Kivy', font_size = 50)
        b2 = Button(text='Hello Python', font_size = 50)
        parent.add_widget(b1)
        parent.add_widget(b2)
        return parent

if __name__ == '__main__':
    appInstance = ButtonApp()
    appInstance.run()