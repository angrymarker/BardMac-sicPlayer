# BardMac-sicPlayer
Python script that converts .midi files to .scpt files, akin to BardMusicPlayer, but for mac!

Refer to the graphic https://bardmusicplayer.com/perf_settings.png for key bindings.

FFXIV.

To run: 
install python3
install python module mido 
run cmd line:
  python3 main.py "path/To/MidiFile/song.midi" -1 --user

2nd argument (-1) is the length of the song you'd wish to limit it to (in seconds). if it's -1, it'll output the full song.

to run:
open up bard perform mode in FFXIV with instrument of choice.
ensure keybindings are set 
open up the generated .scpt file
press play, and click/focus on FFXIV
after 10 seconds, song will start
