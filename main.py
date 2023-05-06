import os
import keyboard
import sys
import datetime
import sounddevice as sd
import whisper
from notion_client import Client
import queue
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

import time
import multiprocessing
import shutil

from dotenv import load_dotenv
load_dotenv()

# Set up Notion client
notion = Client(auth=os.environ["NOTION_API_KEY"])
notion_page_id = os.environ["NOTION_PAGE_ID"]

# Load the Whisper model
model = whisper.load_model("base")

success_song = AudioSegment.from_wav("beeps/success.wav")
error_song = AudioSegment.from_wav("beeps/error.wav")
start_song = AudioSegment.from_wav("beeps/start.wav")
stop_song = AudioSegment.from_wav("beeps/stop.wav")

def play_success_sound():
    play(success_song)

def play_error_sound():
    play(error_song)

def play_start_sound():
    play(start_song)

def play_stop_sound():
    play(stop_song)

# Function to record audio
def record_audio(filename):
    sample_rate = 44100
    channels = 1
    q = queue.Queue()

    def audio_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    try:
        with sf.SoundFile(filename, mode='x', samplerate=sample_rate,
                          channels=channels, subtype='PCM_24') as file:
            with sd.InputStream(samplerate=sample_rate, channels=channels, callback=audio_callback):
                keyboard.wait('space')
                sd.stop()
                while not q.empty():
                    file.write(q.get())
    except Exception as e:
        print(f"Error while recording audio: {e}")

# Function to transcribe audio
def transcribe_audio(filename):
    result = model.transcribe(filename)
    return result["text"]

# Function to append transcription to Notion document
def append_to_notion(text):
    # Define the block object for appending
    current_date = datetime.date.today().strftime('%B %d, %Y')
    children = [
        {
            "object": "block",
            "type": "paragraph",
            'paragraph': {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"{current_date}\n"
                        },
                        "annotations": {
                            "bold": True
                        }
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            } 
        } 
    ]

    # Append the block to the page
    notion.blocks.children.append(
        block_id=notion_page_id,
        children=children
    )

def recording_process():
    os.makedirs("temp_recordings", exist_ok=True)
    os.makedirs("completed_recordings", exist_ok=True)
    while True:
        print("Press the space key to start recording...")
        keyboard.wait("space")
        play_start_sound()
        print("Recording... Press the space key to stop recording.")
        current_date_time = datetime.datetime.now().strftime("%B %d, %Y %H-%M-%S")
        temp_audio_filename = f"temp_recordings/audio_{current_date_time}.wav"
        completed_audio_filename = f"completed_recordings/audio_{current_date_time}.wav"
        record_audio(temp_audio_filename)
        play_stop_sound()
        shutil.move(temp_audio_filename, completed_audio_filename)
        print(f"Audio recorded and saved to {completed_audio_filename}")

def transcribing_process():
    while True:
        try:
            time.sleep(5)
            for file in os.listdir("completed_recordings"):
                if file.endswith(".wav"):
                    audio_file_path = os.path.join("completed_recordings", file)
                    transcription = transcribe_audio(audio_file_path)
                    print("Transcription:", transcription)
                    append_to_notion(transcription)
                    play_success_sound()
                    os.remove(audio_file_path)
                    print(f"Transcription uploaded to Notion and {audio_file_path} deleted.")
        except Exception as e:
            print(f"Error while transcribing and uploading audio. Trying again in 5 seconds...")

if __name__ == "__main__":
    try:
        record_process = multiprocessing.Process(target=recording_process)
        transcribe_process = multiprocessing.Process(target=transcribing_process)

        record_process.start()
        transcribe_process.start()

        record_process.join()
        transcribe_process.join()
    # Catch any kind of error and play error sound
    except Exception as e:
        play_error_sound()
        print(e)
