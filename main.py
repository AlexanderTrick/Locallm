from pyllamacpp.model import Model
import pyaudio
import vosk
import json
import pyttsx3
from asteval import Interpreter
import threading
from queue import Queue

SPEECH_TO_TEXT_MODEL_PATH = "models/vosk-model-small-en-us-0.15"
LLM_PATH = "models/koala-7B.ggmlv3.q4_0.bin"

vosk_model = vosk.Model(model_path=SPEECH_TO_TEXT_MODEL_PATH)
prompt_context = """Act as Bob. Bob is helpful, kind, honest,
and never fails to answer the User's requests immediately and with precision.

User: Nice to meet you Bob!
Bob: Welcome! I'm here to assist you with anything you need. What can I do for you today?
"""

prompt_prefix = "\nUser:"
prompt_suffix = "\nBob:"

model = Model(model_path=LLM_PATH,
              n_ctx=512,
              prompt_context=prompt_context,
              prompt_prefix=prompt_prefix,
              prompt_suffix=prompt_suffix)
rec = vosk.KaldiRecognizer(vosk_model, 16000)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

aeval = Interpreter()
prompt_queue = Queue()

def handle_text_input():
    while True:
        prompt = input()
        prompt_queue.put(prompt)

# Start the text input handler in a separate thread
threading.Thread(target=handle_text_input, daemon=True).start()

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        prompt = result['text']
        if not prompt.strip():  # Check if the prompt is empty
            continue  # Skip this iteration if the prompt is empty
        print(f"User: {prompt}")
        prompt_queue.put(prompt)  # Add the voice prompt to the queue
    elif not prompt_queue.empty():
        prompt = prompt_queue.get()  # Get the text prompt from the queue
        print(f"User (text): {prompt}")
    else:
        continue
    print(f"Bob: ", end='')
    response = ""
    for token in model.generate(prompt,
                                antiprompt='User:',
                                n_threads=6,
                                n_batch=1024,
                                n_predict=256,
                                n_keep=48,
                                repeat_penalty=1.0, ):
        response += f"{token}"
    response = response.strip()  # Remove leading and trailing whitespace

    print(response)
    engine.say(response)
    engine.runAndWait()
