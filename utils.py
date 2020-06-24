import pyaudio
import csv


def read_mapping_from_cli(input):
    mapping_list = []
    tmp_list = input.split(',')
    mapping_list = [ tmp_list[i].split('-') for i in range(0, len(tmp_list)) ]
    return mapping_list #list of tuples

def read_mapping_csv(path):
    reader = csv.reader(open(path, 'r'))
    mapping_list = []
    for row in reader:
        key, value = row
        mapping_list.append([key, value])
    return mapping_list #list of tuples


def find_interfaces():
    print("No input device specified. Printing list of input devices now: ")
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print("Device number (%i): %s" % (i, p.get_device_info_by_index(i).get('name')))
    print("Run this program with -input 1, or the number of the input you'd like to use.")
    exit()
