from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# import numpy as np
# from numpy import random
import random



class MainApp(App):
    def build(self):
        # label = Label(text = 'Hello World', color = 'red')
        btn1 = Button(text = 'Hello World', font_size = 14, on_press = self.button_press, background_color = [1,.6,.35,100])
        # btn1.bind(on_press = callback) 
        return btn1
    def button_press(self, instance):  

        instance.text = str(random.random())

if __name__ == '__main__':
    MainApp().run()

