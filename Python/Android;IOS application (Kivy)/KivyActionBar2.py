from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton, ActionPrevious
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Definisi HomeScreen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Selamat Datang di Aplikasi Rumus"))
        self.add_widget(layout)

# Definisi PersegiScreen
class PersegiScreen(Screen):
    def __init__(self, **kwargs):
        super(PersegiScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input untuk panjang sisi
        self.input_sisi = TextInput(hint_text="Masukkan panjang sisi", size_hint=(1, 0.2))
        self.layout.add_widget(self.input_sisi)

        # Tombol untuk menghitung 
        hitung_button = Button(text="Hitung Luas Persegi", size_hint=(1, 0.2))
        hitung_button.bind(on_press=self.hitung_luas)
        self.layout.add_widget(hitung_button)

        # Label hasil
        self.result_label = Label(text="Hasil: ", size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

    def hitung_luas(self, instance):
        try:
            sisi = float(self.input_sisi.text)
            luas = sisi ** 2
            self.result_label.text = f"Hasil: Luas Persegi = {luas}"
        except ValueError:
            self.result_label.text = "Input tidak valid!"

# Definisi SegitigaScreen
class SegitigaScreen(Screen):
    def __init__(self, **kwargs):
        super(SegitigaScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input untuk alas dan tinggi
        self.input_alas = TextInput(hint_text="Masukkan panjang alas", size_hint=(1, 0.2))
        self.input_tinggi = TextInput(hint_text="Masukkan tinggi", size_hint=(1, 0.2))
        self.layout.add_widget(self.input_alas)
        self.layout.add_widget(self.input_tinggi)

        # Tombol untuk menghitung
        hitung_button = Button(text="Hitung Luas Segitiga", size_hint=(1, 0.2))
        hitung_button.bind(on_press=self.hitung_luas)
        self.layout.add_widget(hitung_button)

        # Label hasil
        self.result_label = Label(text="Hasil: ", size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

    def hitung_luas(self, instance):
        try:
            alas = float(self.input_alas.text)
            tinggi = float(self.input_tinggi.text)
            luas = 0.5 * alas * tinggi
            self.result_label.text = f"Hasil: Luas Segitiga = {luas}"
        except ValueError:
            self.result_label.text = "Input tidak valid!"

# Definisi aplikasi dengan ActionBar dan ScreenManager
class ActionBarApp(App):
    def build(self):
        # Screen Manager untuk mengelola layar
        self.sm = ScreenManager()

        # Menambahkan berbagai screen ke Screen Manager
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(PersegiScreen(name='persegi'))
        self.sm.add_widget(SegitigaScreen(name='segitiga'))

        # Layout utama aplikasi
        layout = BoxLayout(orientation='vertical')

        # Membuat ActionBar
        action_bar = ActionBar(size_hint=(1, 0.1))

        # Membuat ActionView
        action_view = ActionView()

        # Tombol navigasi ke "Home"
        action_previous = ActionPrevious(title='Aplikasi Rumus', with_previous=False)
        action_view.add_widget(action_previous)

        # Tambahkan tombol Home
        action_view.add_widget(ActionButton(text="Home", on_press=self.go_to_home))

        # Tambahkan tombol Persegi untuk menghitung luas persegi
        action_view.add_widget(ActionButton(text="Persegi", on_press=self.go_to_persegi))

        # Tambahkan tombol Segitiga untuk menghitung luas segitiga
        action_view.add_widget(ActionButton(text="Segitiga", on_press=self.go_to_segitiga))

        # Tambahkan ActionView ke ActionBar
        action_bar.add_widget(action_view)

        # Tambahkan ActionBar dan ScreenManager ke layout utama
        layout.add_widget(action_bar)
        layout.add_widget(self.sm)

        return layout

    # Fungsi navigasi
    def go_to_home(self, instance):
        self.sm.current = 'home'

    def go_to_persegi(self, instance):
        self.sm.current = 'persegi'

    def go_to_segitiga(self, instance):
        self.sm.current = 'segitiga'

# Menjalankan aplikasi
if __name__ == '__main__':
    ActionBarApp().run()
