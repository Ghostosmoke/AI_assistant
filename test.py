import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
from get_audio import microphone
class ComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример QComboBox")
        self.resize(300, 100)

        # Основной лейаут
        layout = QVBoxLayout()

        # Создание выпадающего списка
        self.combo = QComboBox()
        self.combo.addItems(microphone())
        # print(microphone())

        # self.combo.addItems(microphone(name='name'))  # Добавление списка

        # self.combo.currentIndexChanged.connect(self.selection_change)

        # Лейбл для отображения выбора
        self.label = QLabel("Выберите пункт")

        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selection_change(self):
        # Обработка изменения выбора
        self.label.setText(f"Выбрано: {self.combo.currentText()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ComboBoxDemo()
    demo.show()
    sys.exit(app.exec())