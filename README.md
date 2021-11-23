# BardMac-sicPlayer
Python script that converts .midi files to .scpt files, akin to BardMusicPlayer, but for mac!

Refer to the graphic https://bardmusicplayer.com/perf_settings.png for key bindings. 

To run: 

install python3

install python module mido 

install python module pyautogui

install pysimplegui

install python3-tkinter

ensure keybindings are set as per bardmusicplayer settings

to run:
open up bard perform mode in FFXIV with instrument of choice.

run cmd line:
  python3 play.py "path/To/MidiFile/song.midi" 

Switch back to FFXIV in performance mode, and rock out

It helps to have the terminal set up in automtor, as it gives you a simple means to stop the song.

Playing will start after a 2 second delay. this can be updated in the play.py, under the sleep(2) function.


If you have issues installing python3, reddit user a5920 wrote up a guide that worked for them:

Install python3 for mac Mac by typing python3 in terminal

Install command line developer tools from the popup

Download https://bootstrap.pypa.io/get-pip.py, 

Type python3 <drag get-pip.py here> in terminal, 
  
Then python3 -m pip install mido 
  
And python3 -m pip install pyautogui
  
And python3 -m pip install pysimplegui
  
And brew install python3-tkinter
  
The last line needs homebrew which you can get here : https://brew.sh/
  
---

To make this a standalone install py2app with "pip3 install py2app" and then run "python3 setup.py py2app"
  
If you want to try a compiled version just download it here https://github.com/realAbitbol/BardMac-sicPlayer/releases
Works on my system but I currently have no ida if it works on a system where the dependancies aren't already installed.
Please let me know !
