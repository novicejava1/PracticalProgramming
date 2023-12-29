from re import MULTILINE
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    # initialze the constructor
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="firstname"))
   
        self.firstname = TextInput(multiline=False)
        self.add_widget(self.firstname)

        self.add_widget(Label(text='lastname'))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.button = Button(text="Submit")
        # Bind the button
        self.button.bind(on_press=self.press)
        self.add_widget(self.button)

    def press(self, instance):
        firstname = self.firstname.text
        lastname = self.lastname.text

        print(f'{ firstname } { lastname }')
        output = f'{ firstname } { lastname }'
        self.add_widget(Label(text=output))

        self.firstname.text = ''
        self.lastname.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()