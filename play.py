from mido import MidiFile, MetaMessage
import sys
from pathlib import Path
from time import sleep
import ntpath
import pyautogui
from pyautogui import press

DEFAULT_TEMPO = 0.5


def ticks2s(ticks, tempo, ticks_per_beat):
    """
        Converts ticks to seconds
    """
    return ticks/ticks_per_beat * tempo


def note2freq(x):
    """
        Convert a MIDI note into a frequency (given in Hz)
    """
    a = 440
    b = (a/32) * (2 ** ((x-9)/12))
    b = round(b)
    keystroke = '\t\t keystroke "'
    #NOT USED -- start
    if b == 1864:
        return 'j'
    elif b == 1760:
        return '8'
    elif b == 1568:
        return '5'
    elif b == 1397:
        return '4'
    elif b == 1319:
        return '3'
    elif b == 1175:
        return '2'
    elif b == 1047:
        return '8'
    elif b == 988:
        return '7'
    elif b == 932:
        return 'j'
    elif b == 880:
        return '6'
    elif b == 831:
        return 'h'
    elif b == 784:
        return '5'
    elif b == 740:
        return 'g'
    elif b == 698:
        return '4'
    elif b == 659:
        return '3'
    elif b == 622:
        return 'f'
    elif b == 587:
        return '2'
    elif b == 554:
        return 'd'
    elif b == 523:
        return '1'
    elif b == 494:
        return 't'
    elif b == 466:
        return 'c'
    elif b == 440:
        return'r'
    elif b == 415:
        return 'x'
    elif b == 392:
        return  'e'
    elif b == 370:
        return 'z'
    elif b == 349:
        return  'w'
    elif b == 330:
        return 'q'
    elif b == 311:
        return 'l'
    elif b == 294:
        return '0'
    elif b == 277:
        return 'k'
    elif b == 262:
        return  '9'
    elif b == 247:
        return  's'
    elif b == 233:
        return  '.'
    elif b == 220:
        return  'a'
    elif b == 208:
        return 'm'
    elif b == 196:
        return  'p'
    elif b == 185:
        return  'n'
    elif b == 175:
        return 'o'
    elif b == 165:
        return 'i'
    elif b == 156:
        return 'b'
    elif b == 147:
        return  'u'
    elif b == 139:
        return 'v'
    elif b == 131:
        return  'y'
    else:
        keystroke += ' NOT FOUND'
    keystroke += ', freq: ' + str(b)
    return keystroke


if __name__ == '__main__':
    
    pyautogui.PAUSE = 0
    # Import the MIDI file...
    mid = MidiFile(sys.argv[1])
    if mid.type == 3:
        print("Unsupported type.")
        exit(3)

    """
        wait 2 seconds to switch window
    """
    sleep(2)
    try:
        for msg in mid.play():
            if hasattr(msg, 'velocity'):
                print(msg)
                if int(msg.velocity) > 0:
                    #print(msg.note)
                    #print(note2freq(msg.note))
                    press(note2freq(msg.note))
            
    except KeyboardInterrupt:
        print('quit')
        sys.exit()
