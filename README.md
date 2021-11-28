# 🎵 BardMac-sicPlayer 🍎

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/realAbitbol/BardMac-sicPlayer/graphs/commit-activity) [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A bard performance music player for MacOS !

*A fork of the awesome work of **@Angrymarker** https://github.com/angrymarker/BardMac-sicPlayer with some cool things like improved playback and a GUI*

![image](https://user-images.githubusercontent.com/73762857/143772494-7d998104-2032-4ad3-b3ce-5c672bc84c76.png)


---

### 💾 Download

Latest version : [💾 v1.0-alpha8](https://github.com/realAbitbol/BardMac-sicPlayer/releases/download/v1.0-alpha8/BardMac-sicPlayer.app.zip)

Changelog :
- Slightly nicer UI
- Improved playback
- Countdown to start
- Optimizations
- Fixed progressbar
- Removed the hold_notes and tempo option (didn't work correctly, might be readded at a later time)

Every release can be found 👉[HERE](https://github.com/realAbitbol/BardMac-sicPlayer/releases)

🎵 Midi tunes : You can get some (mostly) compatible midis on the excellent [Bard Music Player](https://bardmusicplayer.com) Midi Library 👉[HERE](https://songs.bardmusicplayer.com)

---

### 🎹 Usage
- Click the Keybindings button to see the required key bindings in performance mode in game.
- In game, open up bard perform mode with your instrument of choice.
- On BardMac-sicPlayer, browse to a folder containing the midi files you want to play.
- Select a song.
- Press Play.
- Within 3 seconds set ff14 as your active window by clicking on it.

### ⚙️ Options
- Debug : Shows debug window.
- Min interval : minimum interval between two keystrokes. 0.05 seems to be a sweet spot. Set this too low and you might experience some missed keystrokes if you don't have a perfect framerate.

### 🔧 Troubleshooting
- Music partially plays : set the performance mode keybinds as expected by the tool (press the Keybindings button for reference)
- Music doesnt play at all :
  - Make sure FF14 is your active window.
  - Give the program accessibility permissions if MacOS, sowehow, didn't already ask you for them by going to System Settings > Security and confidentiality > Accessibility > press the + button and select the app.
 
 ### 🆘 Need help ?
 
 Just file an issue [HERE](https://github.com/realAbitbol/BardMac-sicPlayer/issues).

 I'll do my best to help you.
 
 ### 💡 An idea ? A suggestion ?
 
 Let's discuss it [HERE](https://github.com/realAbitbol/BardMac-sicPlayer/discussions).

---

## 🤖 For developpers

### ▶️ Running the script

This is a [Python3](https://www.python.org/downloads/) script with the following dependencies:
- [mido](https://pypi.org/project/mido/) : midi handling library, install it with pip.

- [pyautogui](https://pypi.org/project/PyAutoGUI/) : automation library, install it with pip.

- [pysimplegui](https://pypi.org/project/PySimpleGUI/) : GUI making library, install it with pip.

- [python-tk](https://formulae.brew.sh/formula/python-tk@3.9) : tkinter support for python, needed by pysimplegui, install it with [Homebrew 🍺](https://brew.sh/).

Then run in terminal :

```bash
python3 BardMac-sicPlayer.py
```

### 📦 Building binaries

To make this a standalone install [py2app](https://pypi.org/project/py2app/) with pip and then run in terminal :
```bash
python3 setup.py py2app
```  

### 🧑‍💻 👩‍💻 Want to help ?

Welcoming all pull requests !
