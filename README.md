# 🎵 BardMac-sicPlayer 🎵

A fork of the awesome work of @Angrymarker https://github.com/angrymarker/BardMac-sicPlayer with some cool things like improved playback and a GUI

<img width="787" alt="image" src="https://user-images.githubusercontent.com/73762857/143594996-11713acc-4b3e-4f0d-bd27-244ae48dd17b.png">

Python script that plays .midi files akin to BardMusicPlayer, but for mac!

➡️ [DOWNLOAD HERE](https://github.com/realAbitbol/BardMac-sicPlayer/releases)

Refer to the graphic https://bardmusicplayer.com/perf_settings.png for key bindings in game.

### 🎹 Usage
- In game open up bard perform mode with your instrument of choice
- On BardMac-sicPlayer, browse to a folder containing the mid files you want to play
- Select a song
- Press play
- Within 3 seconds set ff14 as your active window by clicking on it

### ⚙️ Options
- Hold Notes : new experimental playback mode that hold keys the right time. Works better with some mid files, works strange with some others.
- Debug: Show debug window
- Min interval : minimum interval between two keystrokes. 0.05 seems to be a sweet spot. Set this too low and you might experience some missed keystrokes if you don't have a perfect framerate.
- Tempo: Only for hold notes mode, modifies the keystrokes durations thus speeding or slowing down playback.

### 🔧 Troubleshooting
- Music partially plays: set the performance mode keybinds as expected by the tool (press the Keybindings button for reference)
- Music doesnt play at all:
  - Make sure FF14 is your active window
  - Give the program accessibility permissions if MacOS, sowehow, didn't already ask you for them by going to System Settings > Security and confidentiality > Accessibility > press the + button and select the tool app
 
 ### 🆘 Need help ?
 
 Just file an issue [HERE](https://github.com/realAbitbol/BardMac-sicPlayer/issues).

 I'll do my best to help you.
 
 ### 📈 An idea ? A suggestion ?
 
 Let's discuss it [HERE](https://github.com/realAbitbol/BardMac-sicPlayer/discussions)

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
