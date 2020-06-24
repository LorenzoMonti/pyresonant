import aubio
import numpy as np
import pyaudio
import time
import argparse
import queue
import music21
import utils as ut
import pitch_recognition as pr
import cli

# test flag
printOut = True
volume_thresh=0.001 # default

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    args = cli.cli(parser)

    if args.input is None:
        ut.find_interfaces()
    if(args.volthresh):
        volume_thresh = args.volthresh
    if(args.mapping):
        mapping_list = ut.read_mapping_from_cli(args.mapping)
    if(args.mappingcsv):
        mapping_list = ut.read_mapping_csv(args.mappingcsv)
    if(args.mapping is None and args.mappingcsv is None):
        print("csv mapping file and mapping cli argument not found")
        exit()

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, input=True,
                    input_device_index=args.input, frames_per_buffer=4096)
    time.sleep(1)

    # Aubio's pitch detection.
    pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
    pDetection.set_unit("Hz")
    pDetection.set_silence(-40)

    pitch_queue = queue.Queue()
    current_pitch = music21.pitch.Pitch()
    pr.pitch_recognition(stream, pDetection, pitch_queue, current_pitch, printOut, mapping_list, volume_thresh)
