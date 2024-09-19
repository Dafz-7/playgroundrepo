from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

#* Pengaturan warna background aplikasi
color = (0.0, 0.1, 0.8, 0.0)
Window.clearcolor = color

class SimpleMathApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        #* Label dan input untuk panjang
        self.label_panjang = Label(text="Masukkan panjang: ")
        self.input_panjang = TextInput(hint_text="Panjang", multiline=False, input_filter='float')

        #* Label dan input untuk lebar
        self.label_lebar = Label(text="Masukkan lebar: ")
        self.input_lebar = TextInput(hint_text="Lebar", multiline=False, input_filter='float')

        #* Tombol untku menghitung luas
        self.button_hitung = Button(text="Hitung luas", background_color=(0.1, 0.11, 0, 1)) #* Tombol warna hijau
        self.button_hitung.bind(on_press=self.hitung_luas)
        
        #* Label untuk menampilkan hasil
        self.label_hasil = Label(text="Hasil: ")

        #* Menambahkan widget ke layout
        layout.add_widget(self.label_panjang)
        layout.add_widget(self.input_panjang)
        layout.add_widget(self.label_lebar)
        layout.add_widget(self.input_lebar)
        layout.add_widget(self.button_hitung)
        layout.add_widget(self.label_hasil)
        
        return layout
    
    def hitung_luas(self, instance):
        try:
            panjang = float(self.input_panjang.text)
            lebar = float(self.input_lebar.text)
            luas = panjang * lebar
            self.label_hasil.text = f"Hasil: {luas}"
        except ValueError:
            self.label_hasil.text = "Masukkan angka yang valid."

if __name__ == '__main__':
    SimpleMathApp().run()