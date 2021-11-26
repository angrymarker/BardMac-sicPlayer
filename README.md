# BardMac-sicPlayer

A fork of the awesome work of @Angrymarker https://github.com/angrymarker/BardMac-sicPlayer with some cool things like improved playback and a GUI

<img width="790" alt="image" src="https://user-images.githubusercontent.com/73762857/143489629-aa22c63a-6ed0-4060-ba36-6f7bf53f2c41.png">

Python script that plays .midi files akin to BardMusicPlayer, but for mac!

➡️ [DOWNLOAD HERE](https://github.com/realAbitbol/BardMac-sicPlayer/releases)

Refer to the graphic https://bardmusicplayer.com/perf_settings.png for key bindings in game.

---
## For developpers

### To run: 

install python3

install python module mido 

install python module pyautogui

install pysimplegui

install python3-tkinter

ensure keybindings are set as per bardmusicplayer settings

In game :
open up bard perform mode in FFXIV with instrument of choice.

run cmd line:
  python3 BardMac-sicPlayer.py

Switch back to FFXIV in performance mode, and rock out

Playing will start after a 3 second delay to let you switch your active window back to ff14.


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
## Building binaries

To make this a standalone install py2app with "pip3 install py2app" and then run "python3 setup.py py2app"
  
If you want to try a compiled version just download it here https://github.com/realAbitbol/BardMac-sicPlayer/releases
  
Important : 
  
Give application accessibility permissions in
  
System settings > Security and privacy > Accessibility
  
Click the "+" on the bottom and add the application.

Double check it's checked.
  
  
It works on my system but I currently have no idea if it works on a system where the dependancies aren't already installed.
  
Please let me know !
