#!/usr/bin/env python

import kivy
import lovecal

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput

class ValidateInput(TextInput):

    invalid_set = r"[-.\'@_!#$%^&*()<>?/\|}{~:0123456789 ]"
    count = 0

    def insert_text(self, substring, from_undo=False):
        firstname = [c for c in substring if c not in self.invalid_set]
        s = ''.join(firstname)
        return super().insert_text(s, from_undo=from_undo)

    def keyboard_on_key_up(self, keycode, text):
        if self.readonly and text[1] == "backspace":
            self.readonly = False
            self.do_backspace()

class Manager(ScreenManager):

    result = StringProperty(None)
    percentage = StringProperty(None)

    def playstart(self):
        sound = SoundLoader.load('send.wav')
        sound.play()

    def playreturn(self):
        sound = SoundLoader.load('send.wav')
        sound.play()


    def results(self):
        sound = SoundLoader.load('send.wav')
        print(self.ids.firstname.text)
        print(self.ids.secondname.text)
        first = self.ids.firstname.text
        second = self.ids.secondname.text
        results = lovecal.calculator(first, second)
        print(results)
        self.result = results['result']
        self.percentage = results['percentage']
        print(self.result)
        print(self.percentage)
        sound.play()

class ScreenApp(App):
    def build(self):
        self.sm = Manager()
        return self.sm

if __name__ == '__main__':
    ScreenApp().run()
