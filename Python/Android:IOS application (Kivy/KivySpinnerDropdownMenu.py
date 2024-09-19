import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


class TemperatureConverter(BoxLayout):
    def __init__(self, **kwargs):
        super(TemperatureConverter, self).__init__(**kwargs)
        self.orientation = 'vertical'

        #* Label to prompt the user
        self.label = Label(text = 'Enter temperature: ')
        self.add_widget(self.label)

        #* Text input field for the temperature
        self.input = TextInput(text = '', multiline = False)
        self.add_widget(self.input)

        #* Spininer (dropdown) to select the conversion type
        self.spinner = Spinner(
            text = 'Choose temperature',
            values = ('Celcius to Fahrenheit', 'Celcius to Kelvin',
                      'Fahrenheit to Celcius', 'Fahrenheit to Kelvin',
                      'Kelvin to Celcius', 'Kelvin to Fahrenheit')
        )
        self.add_widget(self.spinner)

        #* Button to trigger conversion
        self.button = Button(text = 'Conversion')
        self.button.bind(on_press = self.convert_temperature)
        self.add_widget(self.button)


        #* Label to display the result
        self.result = Label(text = '')
        self.add_widget(self.result)

    def convert_temperature(self, instance):
        try:
            #* Get the temperature input
            temperature = float(self.input.text)
            #* Get the conversion type
            conversion_type = self.spinner.text

            #* Perform the conversion based on the selected option
            if conversion_type == 'Celcius to Fahrenheit':
                result = (temperature * 9 / 5) + 32
                self.result.text = f'Result: {result} F'
            elif conversion_type == 'Celcius to Kelvin':
                result = temperature + 273.15
                self.result.text = f'Result: {result} K'
            elif conversion_type == 'Fahrenheit to Celcius':
                result = (temperature - 32) * 5 / 9
                self.result.text = f'Result: {result} C'
            elif conversion_type == 'Fahrenheit to Kelvin':
                result = (temperature - 32) * 5 / 9 + 273.15
                self.result.text = f'Result: {result} K'
            elif conversion_type == 'Kelvin to Celcius':
                result = temperature - 273.15
                self.result.text = f'Result: {result} C'
            elif conversion_type == 'Kelvin to Fahrenheit':
                result = (temperature - 273.15) * 9 / 5 + 32
                self.result.text = f'Result: {result} F'
        except ValueError:
            #* Handle invalid input
            self.result.text = 'Please enter valid number'


class app(App):
    def build(self):
        return TemperatureConverter()
    

if __name__ == '__main__':
    app().run()