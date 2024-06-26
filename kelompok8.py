import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem

class KasirApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Membuat widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Membuat layout utama
        main_layout = QVBoxLayout()

        # Membuat layout untuk input nama barang
        name_layout = QHBoxLayout()
        name_label = QLabel('Nama Barang:', self)
        self.name_edit = QLineEdit(self)
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_edit)
        main_layout.addLayout(name_layout)

        # Membuat layout untuk input harga barang
        price_layout = QHBoxLayout()
        price_label = QLabel('Harga Barang:', self)
        self.price_edit = QLineEdit(self)
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_edit)
        main_layout.addLayout(price_layout)

        # Membuat layout untuk input jumlah barang
        qty_layout = QHBoxLayout()
        qty_label = QLabel('Jumlah Barang:', self)
        self.qty_edit = QLineEdit(self)
        qty_layout.addWidget(qty_label)
        qty_layout.addWidget(self.qty_edit)
        main_layout.addLayout(qty_layout)

        # Membuat tombol untuk menambahkan barang
        self.add_button = QPushButton('Tambahkan Barang', self)
        self.add_button.clicked.connect(self.add_item)
        main_layout.addWidget(self.add_button)

        # Membuat tabel untuk menampilkan barang yang ditambahkan
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Nama Barang', 'Harga Barang', 'Jumlah Barang'])
        main_layout.addWidget(self.table)

        # Membuat label untuk menampilkan total harga
        self.total_label = QLabel('Total Harga: 0', self)
        main_layout.addWidget(self.total_label)

        # Mengatur layout ke widget utama
        central_widget.setLayout(main_layout)

        # Mengatur properti jendela
        self.setWindowTitle('Aplikasi Kasir Sederhana')
        self.setGeometry(300, 300, 400, 300)

    def add_item(self):
        # Mengambil nilai dari QLineEdit
        name = self.name_edit.text()
        try:
            price = float(self.price_edit.text())
            qty = int(self.qty_edit.text())
        except ValueError:
            self.total_label.setText('Input tidak valid. Harap masukkan angka yang benar.')
            return

        # Menambahkan barang ke tabel
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(f'{price:.2f}'))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(qty)))

        # Menghitung total harga
        self.calculate_total()

        # Mengosongkan input
        self.name_edit.clear()
        self.price_edit.clear()
        self.qty_edit.clear()

    def calculate_total(self):
        total = 0
        for row in range(self.table.rowCount()):
            price = float(self.table.item(row, 1).text())
            qty = int(self.table.item(row, 2).text())
            total += price * qty
        self.total_label.setText(f'Total Harga: {total:.2f}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KasirApp()
    ex.show()
    sys.exit(app.exec_())
