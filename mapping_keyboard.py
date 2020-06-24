from pynput.keyboard import Key, Controller

def mapping_keyboard(pitch, keyboard, mapping_list):
    for i in range(0, len(mapping_list)):
        if(pitch.rfind(mapping_list[i][0]) != -1): # notes
            keyboard.press(mapping_list[i][1]) # key
