import whisper
def get_text_(model_whisper:str="turbo",audio_='')->str:
    model = whisper.load_model(model_whisper)
    result = model.transcribe(audio_,
        language="ru",
        task="transcribe",
        verbose=False,
        temperature=0.3,
        word_timestamps=False,
        fp16=False
        )
    return result["text"]
