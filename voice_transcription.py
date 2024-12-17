import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
    """
    Converts audio file to text using Google's Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(file_path)
    audio.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Test the function
if __name__ == "__main__":
    file_path = "test_audio.mp3"  # Replace with your file path
    print("Transcribed Text:", transcribe_audio(file_path))
