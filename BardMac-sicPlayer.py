# Copyright (C) 2021 Angrymarker & realAbitbol
# This file is part of BardMac-sicPlayer <https://github.com/chiditarod/dogtag>.
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
import _thread
from time import sleep
import mido as mi
import pyautogui as pa
import PySimpleGUI as Sg


def note2freq(note):
    # Converts a MIDI note into a frequency (given in Hz)

    freq = round((440 / 32) * (2 ** ((note - 9) / 12)))
    keystroke = '\t\t keystroke "'

    if freq == 1864:
        return 'j'
    elif freq == 1760:
        return '8'
    elif freq == 1568:
        return '5'
    elif freq == 1397:
        return '4'
    elif freq == 1319:
        return '3'
    elif freq == 1175:
        return '2'
    elif freq == 1047:
        return '8'
    elif freq == 988:
        return '7'
    elif freq == 932:
        return 'j'
    elif freq == 880:
        return '6'
    elif freq == 831:
        return 'h'
    elif freq == 784:
        return '5'
    elif freq == 740:
        return 'g'
    elif freq == 698:
        return '4'
    elif freq == 659:
        return '3'
    elif freq == 622:
        return 'f'
    elif freq == 587:
        return '2'
    elif freq == 554:
        return 'd'
    elif freq == 523:
        return '1'
    elif freq == 494:
        return 't'
    elif freq == 466:
        return 'c'
    elif freq == 440:
        return 'r'
    elif freq == 415:
        return 'x'
    elif freq == 392:
        return 'e'
    elif freq == 370:
        return 'z'
    elif freq == 349:
        return 'w'
    elif freq == 330:
        return 'q'
    elif freq == 311:
        return 'l'
    elif freq == 294:
        return '0'
    elif freq == 277:
        return 'k'
    elif freq == 262:
        return '9'
    elif freq == 247:
        return 's'
    elif freq == 233:
        return '.'
    elif freq == 220:
        return 'a'
    elif freq == 208:
        return 'm'
    elif freq == 196:
        return 'p'
    elif freq == 185:
        return 'n'
    elif freq == 175:
        return 'o'
    elif freq == 165:
        return 'i'
    elif freq == 156:
        return 'b'
    elif freq == 147:
        return 'u'
    elif freq == 139:
        return 'v'
    elif freq == 131:
        return 'y'
    else:
        keystroke += ' NOT FOUND'
    keystroke += ', freq: ' + str(freq)
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
        Sg.Checkbox('Hold notes', default=False, enable_events=True, key="-HOLD NOTES-"),
        Sg.Checkbox('Debug', default=False, key="-DEBUG-"),
        Sg.Spin([x / 100.0 for x in range(0, 11, 1)], initial_value=0.05, size=4, key="-MIN INTERVAL-"),
        Sg.Text("Min interval"),
        Sg.Spin([x / 10.0 for x in range(0, 21, 1)], initial_value=1.00, size=4, key="-TEMPO-", disabled=True),
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
    [Sg.Button('Keybindings', enable_events=True, key="-KEYBINDINGS-")]
]

# Full layout
layout = [
    folder_and_options_line,
    [
        Sg.Column(file_list_column),
        Sg.VSeperator(),
        Sg.Column(music_player_column),
    ]
]

window = Sg.Window("BardMac-sicPlayer v1.0-alpha4", layout, finalize=True)

# Event Loop
stop = False
filename = None

while True:
    event, values = window.read()
    if event == "Exit" or event == Sg.WIN_CLOSED:
        stop = True
        break

    elif event == "-FOLDER-":  # Folder name was changed, fill the files list
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

    elif event == "-HOLD NOTES-":  # Hold notes checkbox modified
        window["-TEMPO-"].update(disabled=not values["-HOLD NOTES-"])

    elif event == "-KEYBINDINGS-":  # Keybindings button pressed
        Sg.popup_annoying(title="Keybindings", image='resources/keybindings.png')

window.close()
