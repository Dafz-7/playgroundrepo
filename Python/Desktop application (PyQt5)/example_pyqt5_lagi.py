import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QHBoxLayout

# Fungsi untuk melakukan perhitungan
def hitung(angka):
    try:
        hasil = eval(angka)  # Menggunakan fungsi eval untuk mengevaluasi ekspresi matematika
        return str(hasil)
    except Exception as e:
        return "Error"
    
#! Function for adding a symbol from a button
def add_symbol(input_text, symbol):
    current_text = input_text.text()
    input_text.setText(current_text + symbol)

# Fungsi untuk membuat UI
def init_ui():
    # Membuat layout utama
    layout = QVBoxLayout()

    # Membuat QLineEdit untuk input teks
    input_text = QLineEdit()
    input_text.setPlaceholderText("Masukkan ekspresi matematika...")

    # Membuat label untuk menampilkan hasil perhitungan
    result_label = QLabel("Hasil perhitungan: ")

    # Membuat tombol untuk menampilkan hasil di jendela baru
    show_result_button = QPushButton("Tampilkan Hasil di Jendela Baru")
    show_result_button.clicked.connect(lambda: show_result_in_new_window(input_text))

    #! Making layout for the symbols:
    symbol_layout = QHBoxLayout()
    symbols = ["+", "-", "*", "/"]
    for symbol in symbols:
        button = QPushButton(symbol)
        button.clicked.connect(lambda checked, s = symbol: add_symbol(input_text, s))
        symbol_layout.addWidget(button)

    # Menambahkan widget ke dalam layout
    layout.addWidget(input_text)
    layout.addWidget(result_label)
    layout.addWidget(show_result_button)

    # Menetapkan layout utama ke widget
    widget = QWidget()
    widget.setLayout(layout)

    widget.setWindowTitle("Contoh PyQt Perhitungan Angka")
    widget.setGeometry(300, 300, 300, 200)

    widget.show()
    sys.exit(app.exec_())

# Fungsi untuk menampilkan hasil di jendela baru
def show_result_in_new_window(input_text):
    # Membuat jendela baru
    dialog = QDialog()

    # Membuat layout untuk jendela baru
    layout = QVBoxLayout()

    # Mengambil hasil perhitungan menggunakan fungsi hitung
    result = hitung(input_text.text())

    # Membuat label untuk menampilkan hasil perhitungan
    result_label = QLabel("Hasil perhitungan: " + result)

    # Membuat tombol untuk menutup jendela baru
    close_button = QPushButton("Tutup")
    close_button.clicked.connect(dialog.close)

    # Menambahkan widget ke dalam layout jendela baru
    layout.addWidget(result_label)
    layout.addWidget(close_button)

    # Menetapkan layout ke jendela baru
    dialog.setLayout(layout)

    # Menampilkan jendela baru
    dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    init_ui()