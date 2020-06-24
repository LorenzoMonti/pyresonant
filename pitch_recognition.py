import aubio
import numpy as np
import pyaudio
import time
from pynput.keyboard import Key, Controller
import mapping_keyboard as mk

def pitch_recognition(stream, pDetection, pitch_queue, current_pitch, printOut, mapping_list, volume_thresh=0.01):
    keyboard = Controller()
    while True:

        data = stream.read(1024, exception_on_overflow=False)
        samples = np.fromstring(data, dtype=aubio.float_type)
        pitch = pDetection(samples)[0]

        volume = np.sum(samples**2)/len(samples) * 100

        if pitch and volume > volume_thresh:  # adjust with your mic!
            current_pitch.frequency = pitch
        else:
            continue

        if printOut:
            print(current_pitch)
        else:
            current = current_pitch.nameWithOctave
            pitch_queue.put({'Note': current, 'Cents': current_pitch.microtone.cents})

        pitch = str(current_pitch)

        mk.mapping_keyboard(pitch, keyboard, mapping_list)
