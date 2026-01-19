from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class SimpleRecordingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Запись")
        self.setFixedSize(300 , 100)

        # Основной layout
        self.layout = QHBoxLayout()

        # Кнопка запуска
        self.start_btn = QPushButton("▶ Запуск")
        self.start_btn.setFixedSize(80 , 40)
        self.start_btn.clicked.connect(self.start_recording)

        # Кнопка паузы
        self.pause_btn = QPushButton("⏸ Пауза")
        self.pause_btn.setFixedSize(80 , 40)
        self.pause_btn.clicked.connect(self.pause_recording)
        self.pause_btn.hide()  # Скрываем изначально

        # Кнопка остановки
        self.stop_btn = QPushButton("⏹ Стоп")
        self.stop_btn.setFixedSize(80 , 40)
        self.stop_btn.clicked.connect(self.stop_recording)
        self.stop_btn.hide()  # Скрываем изначально

        # Добавляем кнопки в layout
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.pause_btn)
        self.layout.addWidget(self.stop_btn)

        # Центрируем кнопки
        self.layout.addStretch()
        self.layout.insertWidget(0 , self.start_btn)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def start_recording(self):
        print("🎤 Запись начата")

        # Прячем кнопку запуска
        self.start_btn.hide()

        # Показываем кнопки паузы и остановки
        self.pause_btn.show()
        self.stop_btn.show()

    def pause_recording(self):
        print("⏸ Запись на паузе")

    def stop_recording(self):
        print("⏹ Запись остановлена")

        # Прячем кнопки паузы и остановки
        self.pause_btn.hide()
        self.stop_btn.hide()

        # Показываем кнопку запуска
        self.start_btn.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleRecordingApp()
    window.show()
    sys.exit(app.exec())