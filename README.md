# BardMac-sicPlayer
Python script that converts .midi files to .scpt files, akin to BardMusicPlayer, but for mac!

Refer to the graphic https://bardmusicplayer.com/perf_settings.png for key bindings. 

To run: 

install python3

install python module mido 

install python module pyautogui

ensure keybindings are set as per bardmusicplayer settings

to run:
open up bard perform mode in FFXIV with instrument of choice.

run cmd line:
  python3 play.py "path/To/MidiFile/song.midi" 

Switch back to FFXIV in performance mode, and rock out



Playing will start after a 2 second delay. this can be updated in the play.py, under the sleep(2) function.
