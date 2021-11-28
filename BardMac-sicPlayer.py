# Copyright (C) 2021 Angrymarker & realAbitbol
# This file is part of BardMac-sicPlayer <https://github.com/realAbitbol/BardMac-sicPlayer>.
#
# BardMac-sicPlayer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BardMac-sicPlayer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BardMac-sicPlayer.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os.path
import time as ti
import mido as mi
import pyautogui as pa
import PySimpleGUI as Sg
from pathlib import Path

version = "BardMac-sicPlayer v1.0.2"
last_folder_path = os.path.join(Path.home(), ".bardmac")


def note2freq(x):
    # Converts a note to a frequency and returns the correct keybinding to press

    b = round((440 / 32) * (2 ** ((x - 9) / 12)))
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


def read_files(selected_folder):
    try:
        # Get list of files in folder
        file_list = os.listdir(selected_folder)
    except OSError:
        file_list = []

    file_names = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(selected_folder, f))
        and f.lower().endswith((".mid", ".midi"))
    ]
    file_names.sort()
    return file_names


def play_midi(midi_file):
    pa.PAUSE = 0
    # Import the MIDI file
    mid = mi.MidiFile(midi_file)
    if mid.type == 3:
        Sg.popup("Unsupported file")
        return

    # wait 3 seconds to switch window
    window["-STATE-"].update('in 3s')
    ti.sleep(1)
    window["-STATE-"].update('in 2s')
    ti.sleep(1)
    window["-STATE-"].update('in 1s')
    ti.sleep(1)

    window["-STATE-"].update('Playing.')
    length = mid.length
    debug = values["-DEBUG-"]
    min_interval = values["-MIN INTERVAL-"]

    try:
        start_time = ti.time()
        last_time = ti.time()
        for msg in mid.play():
            if hasattr(msg, 'velocity'):
                if int(msg.velocity) > 0:
                    elapsed_time = ti.time() - last_time
                    if elapsed_time < min_interval:
                        ti.sleep(max(0, min_interval-elapsed_time))
                    pa.press(note2freq(msg.note))
                    last_time = ti.time()
                    window["-PROGRESS-"].update_bar(round(ti.time()-start_time), length)

                    if debug:
                        Sg.Print(elapsed_time)

            if stop:
                break
    except KeyboardInterrupt:
        sys.exit()


def update_file_list(selected_folder):
    window["-FILE LIST-"].update(read_files(selected_folder))
    window["-TOUT-"].update('')
    window["-PLAY-"].update(disabled=True)


# GUI
Sg.theme('System Default For Real')

folder_and_options_line = [
    [
        Sg.Text("Midi tunes folder"),
        Sg.In("", size=(40, 1), enable_events=True, key="-FOLDER-"),
        Sg.FolderBrowse(),
        Sg.Checkbox('Debug', default=False, key="-DEBUG-", tooltip="Shows the debug window displaying Midi messages"),
        Sg.Spin([x / 100.0 for x in range(0, 11, 1)], initial_value=0.05, size=4, key="-MIN INTERVAL-",
                tooltip="Lower is more accurate but you might miss some notes unless you have a perfect frame-rate"),
        Sg.Text("Min interval",
                tooltip="Lower is more accurate but you might miss some notes unless you have a perfect frame-rate"),
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
music_player_column = [
    [Sg.Text("Selected file:")],
    [Sg.Text(size=(40, 1), key="-TOUT-")],
    [
        Sg.Text('Stopped.', key="-STATE-", size=7),
        Sg.ProgressBar(0, orientation='h', key='-PROGRESS-', visible=True, size=(45, 20))
    ],
    [
        Sg.Button('Play!', enable_events=True, key="-PLAY-", disabled=True),
        Sg.Button('Stop', enable_events=True, key="-STOP-", disabled=True),
    ],
    Sg.vbottom([Sg.Button('Keybindings', enable_events=True, key="-KEYBINDINGS-",
                          tooltip="Displays the required keybindings")])
]

# ----- Full layout -----
layout = [
    folder_and_options_line,
    [
        Sg.Column(file_list_column),
        Sg.VSeperator(),
        Sg.Column(music_player_column, vertical_alignment='t'),
    ]
]

window = Sg.Window(version, layout, finalize=True)
try:
    with open(last_folder_path, "r") as last_folder:
        folder = last_folder.readline()
        window["-FOLDER-"].update(folder)
        update_file_list(folder)
except FileNotFoundError:
    pass

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
        update_file_list(values["-FOLDER-"])
        with open(last_folder_path, "w") as last_folder:
            last_folder.write(values["-FOLDER-"])

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
            window.perform_long_operation(lambda:
                                          play_midi(filename),
                                          '-STOP-')

    elif event == "-STOP-":  # Stop button pressed
        stop = True
        window["-STOP-"].update(disabled=True)
        window["-PLAY-"].update(disabled=False)
        window["-STATE-"].update('Stopped.')
        window["-PROGRESS-"].update_bar(0, 0)

    elif event == "-KEYBINDINGS-":
        Sg.popup_annoying(title="Keybindings", image='resources/keybindings.png')

window.close()
