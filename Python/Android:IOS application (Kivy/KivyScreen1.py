from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScreen(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name = name)
        btn = Button(text = 'Switch to another screen')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name = name)
        btn = Button(text = 'Come back, come back!')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        return sm
    
#! Run the code (the app)

app = MyApp()
app.run()