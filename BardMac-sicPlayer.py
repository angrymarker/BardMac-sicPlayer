import sys
import os.path
import _thread
from time import sleep
import mido as mi
import pyautogui as pa
import PySimpleGUI as Sg


def note2freq(x):
    """
        Convert a MIDI note into a frequency (given in Hz)
    """
    a = 440
    b = (a / 32) * (2 ** ((x - 9) / 12))
    b = round(b)
    keystroke = '\t\t keystroke "'
    # NOT USED -- start
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
        return 'r'
    elif b == 415:
        return 'x'
    elif b == 392:
        return 'e'
    elif b == 370:
        return 'z'
    elif b == 349:
        return 'w'
    elif b == 330:
        return 'q'
    elif b == 311:
        return 'l'
    elif b == 294:
        return '0'
    elif b == 277:
        return 'k'
    elif b == 262:
        return '9'
    elif b == 247:
        return 's'
    elif b == 233:
        return '.'
    elif b == 220:
        return 'a'
    elif b == 208:
        return 'm'
    elif b == 196:
        return 'p'
    elif b == 185:
        return 'n'
    elif b == 175:
        return 'o'
    elif b == 165:
        return 'i'
    elif b == 156:
        return 'b'
    elif b == 147:
        return 'u'
    elif b == 139:
        return 'v'
    elif b == 131:
        return 'y'
    else:
        keystroke += ' NOT FOUND'
    keystroke += ', freq: ' + str(b)
    return keystroke


def read_files(f):
    folder = f
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except OSError:
        file_list = []

    file_names = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".mid", ".midi"))
    ]
    file_names.sort()
    return file_names


def play_midi(midi_file):
    pa.PAUSE = 0
    # Import the MIDI file...
    mid = mi.MidiFile(midi_file)
    if mid.type == 3:
        Sg.popup("Unsupported file")
        window["-STOP-"].click()
        return

    # wait 3 seconds to switch window
    sleep(3)
    window["-STATE-"].update('Playing.')
    length = mid.length
    hold_notes = values["-HOLD NOTES-"]
    debug = values["-DEBUG-"]
    min_interval = values["-MIN INTERVAL-"]
    tempo = values["-TEMPO-"]
    try:
        current_time = 0
        for msg in mid.play():
            if hasattr(msg, 'velocity'):
                if int(msg.velocity) > 0:
                    if hold_notes:
                        pa.keyDown(note2freq(msg.note))
                        sleep(max(msg.time / tempo, min_interval / tempo, min_interval))
                        pa.keyUp(note2freq(msg.note))
                    else:
                        pa.press(note2freq(msg.note))
                        sleep(min_interval)
                    if debug:
                        Sg.Print(msg)
            if stop:
                break
            current_time += msg.time
            window["-PROGRESS-"].update_bar(current_time, length)
            window.refresh()
        window["-STOP-"].click()
    except KeyboardInterrupt:
        sys.exit()


# GUI
Sg.theme('System Default For Real')

folder_and_options_line = [
    [
        Sg.Text("Midi tunes folder"),
        Sg.In("", size=(40, 1), enable_events=True, key="-FOLDER-"),
        Sg.FolderBrowse(),
        Sg.Checkbox('Hold notes', default=False, key="-HOLD NOTES-"),
        Sg.Checkbox('Debug', default=False, key="-DEBUG-"),
        Sg.Spin([x / 100.0 for x in range(0, 11, 1)], initial_value=0.05, size=4, key="-MIN INTERVAL-"),
        Sg.Text("Min interval"),
        Sg.Spin([x / 10.0 for x in range(0, 21, 1)], initial_value=1.00, size=4, key="-TEMPO-"),
        Sg.Text("Tempo"),
    ],
]

file_list_column = [
    [
        Sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [Sg.Text("Selected file:")],
    [Sg.Text(size=(40, 1), key="-TOUT-")],
    [
        Sg.Text('Stopped.', key="-STATE-", size=7),
        Sg.ProgressBar(0, orientation='h', key='-PROGRESS-', visible=True, size=(45, 20))
    ],
    [
        Sg.Button('Play!', enable_events=True, key="-PLAY-", disabled=True),
        Sg.Button('Stop', enable_events=True, key="-STOP-", disabled=True),
    ]
]

# ----- Full layout -----
layout = [
    folder_and_options_line,
    [
        Sg.Column(file_list_column),
        Sg.VSeperator(),
        Sg.Column(image_viewer_column),
    ]
]

window = Sg.Window("BardMac-sicPlayer v1.0-alpha4", layout, finalize=True)

# Run the Event Loop

stop = False
filename = None

while True:
    event, values = window.read()
    if event == "Exit" or event == Sg.WIN_CLOSED:
        stop = True
        break
    # Folder name was filled in, make a list of files in the folder
    elif event == "-FOLDER-":
        window["-FILE LIST-"].update(read_files(values["-FOLDER-"]))
        window["-TOUT-"].update('')
        window["-PLAY-"].update(disabled=True)

    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(values["-FILE LIST-"][0])
            window["-PLAY-"].update(disabled=False)
        except IndexError:
            pass

    elif event == "-PLAY-":  # Play button pressed
        if filename is not None:
            stop = False
            window["-PLAY-"].update(disabled=True)
            window["-STOP-"].update(disabled=False)
            window["-STATE-"].update('Switch')
            _thread.start_new_thread(play_midi, (filename,))

    elif event == "-STOP-":  # Stop button pressed
        stop = True
        window["-STOP-"].update(disabled=True)
        window["-PLAY-"].update(disabled=False)
        window["-STATE-"].update('Stopped.')
        window["-PROGRESS-"].update_bar(0, 0)

window.close()
