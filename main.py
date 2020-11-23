from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '250')

from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

sound = SoundLoader.load('finish.mp3')

class ControlButton(Button):
    pass

class Timer(Widget):
    countdown = NumericProperty(0)
    time = StringProperty("")
    active = BooleanProperty(False)
        
    def stop_timer(self):
        self.active = False
        self.countdown = 0

    def start_timer(self, minutes = 1800):
        self.active = True
        self.countdown = minutes

    def update(self, dt):
        mins, secs = divmod(self.countdown, 60) 
        self.time = '{:02d}:{:02d}'.format(mins, secs)  
        if self.active: 
            if self.countdown:
                self.countdown -= 1
            else:
                sound.seek(0)
                sound.play()
                self.stop_timer()


class TimerApp(App):
    def build (self):
        timer = Timer()
        Clock.schedule_interval(timer.update, 1)
        return timer


if __name__ == "__main__":
    TimerApp().run()
