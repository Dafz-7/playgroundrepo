from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def test():
    print("Hello!")

class MyApp(App):
    def build(self):
        txt = Label(text = 'This is a label')
        btn = Button(text = 'This is a button')
        btn.on_press = test

        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout
    
MyApp().run()