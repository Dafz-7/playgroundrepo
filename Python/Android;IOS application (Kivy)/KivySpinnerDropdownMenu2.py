from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10)
        
        # Spinner for selecting temperature type
        self.label = Label(text="Select Input Temperature :")
        self.layout.add_widget(self.label)
        
        self.input_scale_spinner = Spinner(
            text='Select Temperature',
            values=('Celsius', 'Fahrenheit', 'Reaumur', 'Kelvin'),
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5}
        )
        self.layout.add_widget(self.input_scale_spinner)
        
        # Spinner for selecting output scale
        self.output_label = Label(text="Select Output Temperature Scale:")
        self.layout.add_widget(self.output_label)
        
        self.output_scale_spinner = Spinner(
            text='Select Temperature',
            values=('Celsius', 'Fahrenheit', 'Reaumur', 'Kelvin'),
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5}
        )
        self.layout.add_widget(self.output_scale_spinner)
        
        # Spinner for selecting temperature value
        self.temp_label = Label(text="Select Temperature:")
        self.layout.add_widget(self.temp_label)
        
        self.temp_spinner = Spinner(
            text='0',
            values=('0', '20', '25', '30', '35', '40', '50'),
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5}
        )
        self.layout.add_widget(self.temp_spinner)
        
        # Button to go to the converter screen
        self.button = Button(text="Go to Converter", on_press=self.go_to_converter)
        self.layout.add_widget(self.button)
        
        self.add_widget(self.layout)
    
    def go_to_converter(self, instance):
        app = App.get_running_app()
        app.temp_value = float(self.temp_spinner.text)
        app.input_scale = self.input_scale_spinner.text
        app.output_scale = self.output_scale_spinner.text
        self.manager.current = 'converter'

class ConverterScreen(Screen):
    def __init__(self, **kwargs):
        super(ConverterScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10)
        
        self.result_label = Label(text="Converted Temperature:")
        self.layout.add_widget(self.result_label)
        
        self.convert_button = Button(text="Convert", on_press=self.convert_temp)
        self.layout.add_widget(self.convert_button)
        
        self.add_widget(self.layout)
    
    def convert_temp(self, instance):
        app = App.get_running_app()
        input_value = app.temp_value
        input_scale = app.input_scale
        output_scale = app.output_scale
        
        converted_value = self.convert_temperature(input_value, input_scale, output_scale)
        self.result_label.text = f"{input_value}°{input_scale[0]} = {converted_value:.2f}°{output_scale[0]}"
    
    def convert_temperature(self, value, from_scale, to_scale):
        # Convert to Celsius first
        if from_scale == 'Fahrenheit':
            value = (value - 32) * 5/9
        elif from_scale == 'Kelvin':
            value -= 273.15
        elif from_scale == 'Reaumur':
            value *= 1.25
        
        # Convert from Celsius to the desired output scale
        if to_scale == 'Fahrenheit':
            value = (value * 9/5) + 32
        elif to_scale == 'Kelvin':
            value += 273.15
        elif to_scale == 'Reaumur':
            value *= 0.8
        
        return value

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        
        # Create a Spinner to navigate between screens
        self.spinner = Spinner(
            text='Select Slide',
            values=('Input Temperature', 'Converter'),
            size_hint=(0.3, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )
        self.spinner.bind(text=self.on_spinner_select)
        
        # Create ScreenManager
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(InputScreen(name='input'))
        self.screen_manager.add_widget(ConverterScreen(name='converter'))
        
        # Add Spinner and ScreenManager to layout
        self.orientation = 'vertical'
        self.add_widget(self.spinner)
        self.add_widget(self.screen_manager)
    
    def on_spinner_select(self, spinner, text):
        # Switch screen based on spinner selection
        if text == 'Input Temperature':
            self.screen_manager.current = 'input'
        elif text == 'Converter':
            self.screen_manager.current = 'converter'

class SpinnerSlidesApp(App):
    temp_value = None  # To store selected temperature
    input_scale = 'Celsius'  # To store selected input scale
    output_scale = 'Fahrenheit'  # To store selected output scale
    
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    SpinnerSlidesApp().run()
