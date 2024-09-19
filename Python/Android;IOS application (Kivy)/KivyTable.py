from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TableApp(App):
    def build(self):
        self.data_list = [] #* To save input data

        #* Main layout
        main_layout = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)

        #* Input data box
        input_layout = BoxLayout(size_hint = (1, None), height = 50)

        self.input_name = TextInput(hint_text = "Name", size_hint = (None, None), size = (150, 40))
        self.input_address = TextInput(hint_text = "Address", size_hint = (None, None), size = (250, 40))

        add_button = Button(text = "Add", size_hint = (None, None), size = (100, 40))
        add_button.bind(on_press = self.add_row)

        input_layout.add_widget(self.input_name)
        input_layout.add_widget(self.input_address)
        input_layout.add_widget(add_button)

        #* Scrool view for the table
        self.scrollview = ScrollView(size_hint = (1, None), size = (600, 400))

        #* Layout for the table
        self.table_layout = GridLayout(cols = 3, padding = 10, spacing = 10, size_hint = (None, None))
        self.table_layout.bind(minimum_height = self.table_layout.setter("height"))
        self.table_layout.width = 600

        #* Table header
        self.add_table_header()

        #* Adding layout table to scrollview
        self.scrollview.add_widget(self.table_layout)

        #* Adding all components to the main layout
        main_layout.add_widget(input_layout)
        main_layout.add_widget(self.scrollview)

        return main_layout
    
    def add_table_header(self):
        headers = ["Name", "Address", "Action"]
        for header in headers:
            label = Label(text = header, bold = True, size_hint = (None, None), size = (150, 40))
            self.table_layout.add_widget(label)

    def add_row(self, instance):
        #* Getting the input value
        name = self.input_name.text
        address = self.input_address.text

        if name and address: #* Making sure no input is empty
            #* Adding data to the list
            self.data_list.append((name, address))

            #* Adding new input data to the table
            name_label = Label(text = name, size_hint = (None, None), size = (150, 40))
            address_label = Label(text = address, size_hint = (None, None), size = (250, 40))
            delete_button = Button(text = "Delete", size_hint = (None, None), size = (100, 40))

            #* Binding events to delete rows
            delete_button.bind(on_press = lambda btn, row = len(self.data_list) - 1: self.delete_row(row))

            self.table_layout.add_widget(name_label)
            self.table_layout.add_widget(address_label)
            self.table_layout.add_widget(delete_button)

            #* Emptying input when adding the data
            self.input_name.text = ""
            self.input_address.text = ""

    def delete_row(self, row):
        #* Delete data from the list
        if 0 <= row < len(self.data_list):
            del self.data_list[row]
            #* Delete all widgets from the table
            self.table_layout.clear_widgets()
            #* Adding back the table header
            self.add_table_header()
            #* Adding back the data to the table
            for idx, data in enumerate(self.data_list):
                name_label = Label(text = data[0], size_hint = (None, None), size = (150, 40))
                address_label = Label(text = data[1], size_hint = (None, None), size = (250, 40))
                delete_button = Button(text = "Delete", size_hint = (None, None), size = (100, 40))
                delete_button.bind(on_press = lambda btn, row = idx: self.delete_row(row))
                self.table_layout.add_widget(name_label)
                self.table_layout.add_widget(address_label)
                self.table_layout.add_widget(delete_button)

#* Running the app
if __name__ == "__main__":
    TableApp().run()