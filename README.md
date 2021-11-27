# 🎵 BardMac-sicPlayer 🍎

A bard performance music player for MacOS !

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

### Running the script

This is a Python3 script with the following dependancies:
- mido: midi handling library, install it with pip

- pyautogui: automation library, install it with pip 

- pysimplegui: GUI making library, install it with pip

- python3-tkinter: tkinter support for python, needed by pysimplegui, install it with [Homebrew](https://brew.sh/)

Then run in terminal:
  python3 BardMac-sicPlayer.py

### Building binaries

To make this a standalone install py2app with pip and then run "python3 setup.py py2app"
  
