import pyaudio
import wave
from pydub import AudioSegment
import os


def record_audio(filename="audio_file/output.mp3" , record_seconds=5 , sample_rate=48000, DEVICE_INDEX = 6, channels=1):
    """
    Запись звука с микрофона и сохранение в MP3
    """
    # ВАЖНО: Устанавливаем количество каналов = 1 (моно)
    # Параметры записи
    chunk = 1024  # Размер буфера
    format = pyaudio.paInt16  # Формат данных

    # Инициализация PyAudio
    p = pyaudio.PyAudio()

    # Получаем информацию об устройстве №6
    device_info = p.get_device_info_by_index(DEVICE_INDEX)
    print(f"Используется устройство: {device_info['name']}")
    print(f"Макс. входных каналов: {device_info['maxInputChannels']}")



    # Открытие потока для записи
    stream = p.open(format=format ,
                    channels=channels ,  # ← ИЗМЕНИТЕ ЭТО НА 1!
                    rate=sample_rate ,
                    input=True ,
                    input_device_index=DEVICE_INDEX ,
                    frames_per_buffer=chunk)

    print(f"Запись началась... ({record_seconds} секунд)")

    # Запись данных
    frames = []
    for i in range(0 , int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Запись завершена!")

    # Остановка и закрытие потока
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Сохранение во временный WAV файл
    temp_wav = "temp_recording.wav"
    wf = wave.open(temp_wav , 'wb')
    wf.setnchannels(channels)  # ← ТАКЖЕ 1 КАНАЛ ЗДЕСЬ
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Конвертация WAV в MP3
    audio = AudioSegment.from_wav(temp_wav)
    audio.export(filename , format="mp3" , bitrate="192k")

    # Удаление временного WAV файла
    os.remove(temp_wav)

    print(f"Аудио сохранено как {filename}")
    print(f"Размер файла: {os.path.getsize(filename) / 1024:.2f} KB")

def microphone():
    for i in range(pyaudio.PyAudio().get_device_count()):
        dev = pyaudio.PyAudio().get_device_info_by_index(i)
        print((i , dev['name'] , dev['maxInputChannels']))
# if __name__ == "__main__":
#     microphone()
#     # Простая запись
#     record_audio("audio_file/my_recording.mp3",record_seconds=5 )