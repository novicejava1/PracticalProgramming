from asyncio import events
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty

class MyWidget(Widget):
    
    count = NumericProperty(0)

    def eventcall(self, dt):
        print(self.count)
        self.count = self.count + 1
        if self.count == 10:
            print("unschedule the event")
            return False
            

class EventDispatchApp(App):
    def build(self):
        eventobj = MyWidget()
        #Clock.schedule_interval(eventobj.eventcall, 1.0)
        event = Clock.schedule_interval(eventobj.eventcall, 1.0)
        return eventobj
if __name__ == '__main__':
    EventDispatchApp().run()