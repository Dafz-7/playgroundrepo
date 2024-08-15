import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QHBoxLayout, QMenu, QAction

# Fungsi untuk melakukan operasi matematika
def hitung(angka1, angka2, operasi):
    try:
        angka1 = int(angka1)
        angka2 = int(angka2)

        if operasi == "Tambah":
            hasil = angka1 + angka2
        elif operasi == "Kurang":
            hasil = angka1 - angka2
        elif operasi == "Kali":
            hasil = angka1 * angka2
        elif operasi == "Bagi":
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                return "Error (Pembagian oleh nol)"
        else:
            return "Error (Operasi tidak valid)"

        return str(hasil)
    except Exception as e:
        return "Error"

# Fungsi untuk membuat UI
def init_ui():
    # Membuat layout utama
    layout = QVBoxLayout()

    # Membuat QLineEdit untuk input angka pertama
    input_angka1 = QLineEdit()
    input_angka1.setPlaceholderText("Masukkan angka pertama...")

    # Membuat QLineEdit untuk input angka kedua
    input_angka2 = QLineEdit()
    input_angka2.setPlaceholderText("Masukkan angka kedua...")

    # Membuat ComboBox untuk memilih operasi matematika
    operasi_combo = QPushButton("Operasi Matematika")
    operasi_menu = QMenu()
    operasi_menu.addAction(QAction("Tambah", operasi_combo))
    operasi_menu.addAction(QAction("Kurang", operasi_combo))
    operasi_menu.addAction(QAction("Kali", operasi_combo))
    operasi_menu.addAction(QAction("Bagi", operasi_combo))
    operasi_combo.setMenu(operasi_menu)

    # Membuat label untuk menampilkan hasil perhitungan
    result_label = QLabel("Hasil perhitungan: ")

    # Membuat tombol untuk menampilkan hasil di jendela baru
    show_result_button = QPushButton("Tampilkan Hasil di Jendela Baru")
    show_result_button.clicked.connect(lambda: show_result_in_new_window(input_angka1.text(), input_angka2.text(), operasi_combo.text()))

    # Menambahkan widget ke dalam layout
    layout.addWidget(input_angka1)
    layout.addWidget(input_angka2)
    layout.addWidget(operasi_combo)
    layout.addWidget(result_label)
    layout.addWidget(show_result_button)

    # Menetapkan layout utama ke widget
    widget = QWidget()
    widget.setLayout(layout)

    widget.setWindowTitle("Contoh PyQt Operasi Matematika")
    widget.setGeometry(300, 300, 300, 200)

    widget.show()
    sys.exit(app.exec_())
    

# Fungsi untuk menampilkan hasil di jendela baru
def show_result_in_new_window(angka1, angka2, operasi):
    # Membuat jendela baru
    dialog = QDialog()

    # Membuat layout untuk jendela baru
    layout = QVBoxLayout()

    # Mengambil hasil perhitungan menggunakan fungsi hitung
    result = hitung(angka1, angka2, operasi)

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
