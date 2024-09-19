from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class ScrollButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        verticallayout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        horizontallayout = BoxLayout()
        txt = Label(text='Choose a screen')

        verticallayout.add_widget(ScrollButton(self, direction='down', goal='First', text='1'))
        verticallayout.add_widget(ScrollButton(self, direction='left', goal='Second', text='2'))
        verticallayout.add_widget(ScrollButton(self, direction='up', goal='Third', text='3'))
        verticallayout.add_widget(ScrollButton(self, direction='right', goal='Fourth', text='4'))

        horizontallayout.add_widget(txt)
        horizontallayout.add_widget(verticallayout)

        self.add_widget(horizontallayout)

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        verticallayout = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn = Button(text='Choice: 1', size_hint=(.5, 1), pos_hint={'left': 0})
        btn_back = ScrollButton(self, direction='up', goal='Main', text='Back', size_hint=(.5, 1), pos_hint={'right': 1})

        verticallayout.add_widget(btn)
        verticallayout.add_widget(btn_back)

        self.add_widget(verticallayout)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        verticallayout = BoxLayout(orientation='vertical')
        self.txt = Label(text='Choice: 2')
        verticallayout.add_widget(self.txt)

        horizontallayout_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        label_1 = Label(text='Enter password: ', halign='right')
        self.input = TextInput(multiline=False)

        horizontallayout_0.add_widget(label_1)
        horizontallayout_0.add_widget(self.input)
        verticallayout.add_widget(horizontallayout_0)

        horizontallayout = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        btn_false = Button(text="Ok!")
        btn_back = ScrollButton(self, direction='right', goal='Main', text='Back')

        horizontallayout.add_widget(btn_false)
        horizontallayout.add_widget(btn_back)
        verticallayout.add_widget(horizontallayout)
        self.add_widget(verticallayout)
        btn_false.bind(on_press=self.change_text)

    def change_text(self, *args):
        self.txt.text = self.input.text + '? Did not work...'

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn_back = ScrollButton(self, direction='down', goal='Main', text='Back', size_hint=(1, None), height='40sp')
        test_label = Label(text='Your own screen')

        layout.add_widget(test_label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        verticallayout = BoxLayout(orientation='vertical', spacing=8)
        a = 'START' + 'Choice: 3 ' * 200
        test_label = Label(text="Extra exercise", size_hint=(0.3, None))

        btn_back = ScrollButton(self, direction='left', goal='Main', text='Back', size_hint=(1, .2), pos_hint={'center_x': 0.5})
        self.label = Label(text=a, size_hint_y=None, font_size='24sp', halign='left', valign='top')
        self.label.bind(size=self.resize)
        self.scroll = ScrollView(size_hint=(1, 1))
        self.scroll.add_widget(self.label)

        verticallayout.add_widget(test_label)
        verticallayout.add_widget(btn_back)
        verticallayout.add_widget(self.scroll)
        self.add_widget(verticallayout)

    def resize(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='Main'))
        sm.add_widget(FirstScreen(name='First'))
        sm.add_widget(SecondScreen(name='Second'))
        sm.add_widget(ThirdScreen(name='Third'))
        sm.add_widget(FourthScreen(name='Fourth'))
        return sm

app = MyApp()
app.run()