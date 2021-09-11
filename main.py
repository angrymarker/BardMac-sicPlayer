from mido import MidiFile, MetaMessage
import sys
from pathlib import Path
import ntpath

DEFAULT_TEMPO = 0.5


def ticks2s(ticks, tempo, ticks_per_beat):
    """
        Converts ticks to seconds
    """
    return ticks/ticks_per_beat * tempo


def note2freq(x):
    """
        Convert a MIDI note into a frequency (given in Hz)
    """
    a = 440
    b = (a/32) * (2 ** ((x-9)/12))
    b = round(b)
    keystroke = '\t\t keystroke "'
    #NOT USED -- start
    if b == 1864:
        #keystroke += 'j" --C6 (8)'
        keystroke += "no hitn note"
    elif b == 1760:
    #C6 8
        #keystroke += '8" --C6 (8)'
                keystroke += "no hitn note"
    elif b == 1568:
    #G5 - 5 E P
                #keystroke +=  '5" --G5'
                        keystroke += "no hitn note"
    elif b == 1397:
    #F5 - 4 W O
                #keystroke +=  '4" --F5'
                        keystroke += "no hitn note"
    elif b == 1319:
    #E5 - 3 Q I
                #keystroke +=  '3" --E5'
                        keystroke += "no hitn note"
    elif b == 1175:
    #D5 - 2 0 U
                #keystroke +=  '2" --D5'
                        keystroke += "no hitn note"
    #NOT USED - end
    elif b == 1047:
    #C5 - 1 9 F
                keystroke +=  '8" --C5'
    elif b == 988:
    #B4 - 7 T S
                keystroke +=  '7" --B4'
    elif b == 932:
        #Bb4 J C .
                keystroke +=  'j" --Bb4'
    elif b == 880:
    #A4 - 6 R A
                keystroke +=  '6" --A4'
    elif b == 831:
        #G#4 - H X M
                keystroke +=  'h" --G#4'
    elif b == 784:
    #G4 - 5 E P
                keystroke +=  '5" --G4'
    elif b == 740:
        #F#4 - G Z N
                keystroke +=  'g" --F#4'
    elif b == 698:
    #F4 - 4 W O
                keystroke +=  '4" --F4'
    elif b == 659:
    #E4 - 3 Q I
                keystroke +=  '3" --E4'
    elif b == 622:
        #Eb4 - F L B
                keystroke +=  'f" --Eb4'
    elif b == 587:
    #D4 - 2 0 U
                keystroke +=  '2" --D4'
    elif b == 554:
        #C#4 - D K V
                keystroke +=  'd" --C#4'
    elif b == 523:
    #C4 - 1 9 Y
                keystroke +=  '1" --C4'
    elif b == 494:
    #B3 7 T S
                keystroke +=  't" --B3'  #started
    elif b == 466:
        #Bb3 J C .
                keystroke +=  'c" --Bb3'
    elif b == 440:
    #A3 6 R A
                keystroke +=  'r" --A3'
    elif b == 415:
        #G#3 - H X M
                keystroke +=  'x" --G#3'
    elif b == 392:
    #G3 - 5 E P
                keystroke +=  'e" --G3'
    elif b == 370:
        #F#3 - G Z N
                keystroke +=  'z" --F#3'
    elif b == 349:
    #F3 - 4 W O
                keystroke +=  'w" --F3'
    elif b == 330:
    #E3 - 3 Q I
                keystroke +=  'q" --E3'
    elif b == 311:
        #Eb3 - F L B
                keystroke +=  'l" --Eb3'
    elif b == 294:
    #D3 - 2 0 U
                keystroke +=  '0" --D3'
    elif b == 277:
        #C#3 - D K V
                keystroke +=  'k" --C#3'
    elif b == 262:
    #C3 - 1 9 Y
                keystroke +=  '9" --C3'
    elif b == 247:
    #B2 - 7 T S
                keystroke +=  's" --B2'
    elif b == 233:
        #Bb2 J C .
                keystroke +=  '." --Bb2'
    elif b == 220:
    #A2 - 6 R A
                keystroke +=  'a" --A2'
    elif b == 208:
        #G#2 - H X M
                keystroke +=  'm" --G#2'
    elif b == 196:
    #G2 - 5 E P
                keystroke +=  'p" --G2'
    elif b == 185:
        #F#2 - G Z N
                keystroke +=  'n" --F#2'
    elif b == 175:
    #F2 - 4 W O
                keystroke +=  'o" --F2'
    elif b == 165:
    #E2 - 3 Q I
                keystroke +=  'i" --E2'
    elif b == 156:
        #Eb2 - F L B
                keystroke +=  'b" --Eb2'
    elif b == 147:
    #D2 - 2 0 U
                keystroke +=  'u" --D2'
    elif b == 139:
        #C#2 - D K V
                keystroke +=  'v" --C#2'
    elif b == 131:
    #C2 - 1 9 Y
                keystroke +=  'y" --C2'
    else:
        keystroke += ' NOT FOUND'
    return keystroke


if __name__ == '__main__':

    # Import the MIDI file...
    mid = MidiFile(sys.argv[1])
    cullTime = -1
    if len(sys.argv) > 2:
        cullTime = int(sys.argv[2])
    if mid.type == 3:
        print("Unsupported type.")
        exit(3)

    """
        First read all the notes in the MIDI file
    """

    tracksMerged = []
    messages = []
    notes = {}
    notesAdded = 0
    for i, track in enumerate(mid.tracks):
        if i > 0 and notesAdded > 0:
            break
        tempo = DEFAULT_TEMPO
        totaltime = 0
        print("Track: " + str(i))

        for message in track:
            
            t = ticks2s(message.time, tempo, mid.ticks_per_beat)
            totaltime += t

            if isinstance(message, MetaMessage):  # Tempo change
                if message.type == "set_tempo":
                    tempo = message.tempo / 10**6
                elif message.type == "end_of_track":
                    pass
                else:
                    print("Unsupported metamessage: " + str(message))
                    messages.append(message)

            else:  # Note
                notesAdded += 1
                if message.type == "control_change" or \
                   message.type == "program_change":
                    pass

                elif message.type == "note_on" or message.type == "note_off":
                    print(message)
                    if message.note not in notes:
                        notes[message.note] = 0
                    if message.type == "note_on" and message.velocity != 0:
                        notes[message.note] += 1
                        if(notes[message.note] == 1):
                            tracksMerged += \
                                [(totaltime, message.note, message.velocity)]

                    else:
                        notes[message.note] -= 1
                        if(notes[message.note] == 0):
                            tracksMerged += \
                                [(totaltime, message.note, message.velocity)]

                else:
                    print(message)

        print("totaltime: " + str(totaltime)+"s")

    """
        Now merge all the tracks alltogether
    """

    tracksMerged = sorted(tracksMerged, key=lambda x: x[0])
    music = []

    for i in range(len(tracksMerged)-1):
        a = tracksMerged[i][0]
        b = tracksMerged[i+1][0]
        t = round(b-a, 3)
        m = tracksMerged[i]
        music += [(t, note2freq(m[1]), m[2])]
    """
        Finally write it in CSV format in a file
    """
    he = "--LENGTH: " + str(mid.length)
    he += ("\n--TYPE: " + str(mid.type))
    he += ("\n--LENGTH: " + str(mid.length))
    he += ("\n--TICKS PER BEAT: " + str(mid.ticks_per_beat))
    for m in messages:
        he +=("\n--" + str(m))
    he += "\n\n on run\n\n"
    he += "\t delay(10)\n\n";
    he += '\t tell application "System Events"\n'
    time = 0
    
    for msg in music:
        if (msg[2] > 49):
            #he += '\t\t key down "' + str(msg[1]) + '"\n'
            #he += '\t\t delay (' + str(msg[0]) + ')\n'
            #he += '\t\t key up "' + str(msg[1]) + '"\n'
            #he += '\t\t keystroke "' + str(msg[1]) + '"\n'
            he += str(msg[1]) + '\n'
            he += '\t\t delay (' + str(msg[0]) + ')\n'
            time += msg[0]
            #print(msg[2])
        else:
            he += '\t\t delay (' + str(msg[0]) + ')\n'
            time += msg[0]
        if cullTime > -1 and time > cullTime:
            break
        #he += str(msg[0])+","+str(msg[1])+","+str(msg[2])+"\n"
        #he += str(msg[1]) +"\n"
    he += '\t end tell\n\n'
    he += 'end run'
    print("Creating file")
    #print(he)
    Path("/Users/marker/Downloads/midiparser-master/temp/" + ntpath.basename(sys.argv[1]) + ".scpt").touch()
    f = open("/Users/marker/Downloads/midiparser-master/temp/"+ ntpath.basename(sys.argv[1]) +".scpt", "w")
    #Path("/Users/jenniferaustin/Desktop/midiparser-master/temp/" + ntpath.basename(sys.argv[1]) + ".scpt").touch()
    #f = open("/Users/jenniferaustin/Desktop/midiparser-master/temp/"+ ntpath.basename(sys.argv[1]) +".scpt", "w")
    f.write(he)
    f.close()
