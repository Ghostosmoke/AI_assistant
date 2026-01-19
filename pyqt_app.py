from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
from get_audio import microphone,record_audio

class DropArea(QLabel):
    fileDropped = pyqtSignal(str)  # Сигнал при успешной загрузке файла

    def __init__(self , parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("Перетащите аудиофайл сюда\n(поддерживаются: mp3, wav, ogg, flac)")
        self.setStyleSheet("""
            DropArea {
                border: 2px dashed #aaa;
                border-radius: 10px;
                padding: 20px;
                background-color: #f8f9fa;
                font-size: 14px;
                min-height: 100px;
            }
            DropArea:hover {
                border-color: #007bff;
                background-color: #e9ecef;
            }
        """)

    def dragEnterEvent(self , event):
        if event.mimeData().hasUrls():
            # Проверяем расширение файла
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if self.is_audio_file(file_path):
                    event.acceptProposedAction()
                    self.setStyleSheet("""
                        DropArea {
                            border: 2px solid #28a745;
                            border-radius: 10px;
                            padding: 20px;
                            background-color: #d4edda;
                            font-size: 14px;
                            min-height: 100px;
                        }
                    """)
                    return
        event.ignore()

    def dragLeaveEvent(self , event):
        self.setStyleSheet("""
            DropArea {
                border: 2px dashed #aaa;
                border-radius: 10px;
                padding: 20px;
                background-color: #f8f9fa;
                font-size: 14px;
                min-height: 100px;
            }
        """)

    def dropEvent(self , event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if self.is_audio_file(file_path):
                self.setText(f"Загружен файл:\n{file_path.split('/')[-1]}")
                self.fileDropped.emit(file_path)
                break

        self.setStyleSheet("""
            DropArea {
                border: 2px dashed #aaa;
                border-radius: 10px;
                padding: 20px;
                background-color: #f8f9fa;
                font-size: 14px;
                min-height: 100px;
            }
        """)

    def is_audio_file(self , file_path):
        audio_extensions = ['.mp3' , '.wav' , '.ogg' , '.flac' , '.m4a' , '.aac' , '.wma']
        return any(file_path.lower().endswith(ext) for ext in audio_extensions)


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
        self.pause_btn = QPushButton("|| Пауза")
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
        self.layout.insertWidget(3 , self.start_btn)
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
        self.pause_btn.hide()
        self.start_btn.show()

        print("|| Запись на паузе")

    def stop_recording(self):
        print("⏹ Запись остановлена")

        # Прячем кнопки паузы и остановки
        self.pause_btn.hide()
        self.stop_btn.hide()
        self.start_btn.show()

        # Показываем кнопку запуска
        self.start_btn.show()

class AudioUploadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Загрузка аудиофайла")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        # Область для перетаскивания
        self.drop_area = DropArea()
        self.drop_area.fileDropped.connect(self.on_file_dropped)
        layout.addWidget(self.drop_area)

        # Кнопка для выбора файла
        self.browse_btn = QPushButton("Выбрать файл...")
        self.browse_btn.clicked.connect(self.browse_file)
        self.browse_btn.setStyleSheet("""
            QPushButton {
                padding: 8px;
                font-size: 14px;
                background-color: #007bff;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        layout.addWidget(self.browse_btn)

        # Информация о выбранном файле
        self.file_info = QLabel("Файл не выбран")
        self.file_info.setStyleSheet("color: #6c757d;")
        layout.addWidget(self.file_info)

        self.setLayout(layout)

    def browse_file(self):
        file_path , _ = QFileDialog.getOpenFileName(
            self ,
            "Выберите аудиофайл" ,
            "" ,
            "Аудиофайлы (*.mp3 *.wav *.ogg *.flac *.m4a *.aac);;Все файлы (*)"
        )

        if file_path:
            self.drop_area.setText(f"Выбран файл:\n{file_path.split('/')[-1]}")
            self.file_info.setText(f"Путь: {file_path}")
            self.on_file_dropped(file_path)

    def on_file_dropped(self , file_path):
        self.file_info.setText(f"Загружен: {file_path.split('/')[-1]}")
        print(f"Файл загружен: {file_path}")
        # Здесь можно добавить обработку файла


# Пример использования в главном окне
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio File Uploader")
        self.setGeometry(100 , 100 , 800 , 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout = QVBoxLayout()
        # layout.addWidget(AudioUploadWidget())
        # central_widget.setLayout(layout)
        layout = QVBoxLayout()
        layout.addWidget(SimpleRecordingApp())
        central_widget.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())