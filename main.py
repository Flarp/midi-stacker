from tkinter import *
import jack
import struct
from threading import Thread

chords = {
  "Pass": [0],
  "Major": [0, 4, 7],
  "Minor": [0, 3, 5],
  "Diminished": [0, 3, 6],
  "Major 7th": [0, 4, 7, 11],
  "Minor 7th": [0, 3, 7, 10],
  "Minor major 7th": [0, 3, 7, 11],
  "Dominant 7th": [0, 4, 7, 10],
  "Dominant 7th #9th": [0, 3, 4, 7, 10],
  "Dominant 7th b5th": [0, 4, 6, 10],
  "Suspended 2nd": [0, 2, 7],
  "Suspended 4th": [0, 5, 7],
  "Augmented": [0, 4, 8],
  "Augmented 7th": [0, 4, 8, 10],
  "Diminished 7th": [0, 3, 6, 9],
  "Half diminished 7th": [0, 3, 6, 10],
  "Augmented major 7th": [0, 4, 8, 11],
  "Major 9th": [0, 4, 7, 9, 14],
  "Minor 9th": [0, 3, 7, 10, 14],
  "Dominant 9th": [0, 4, 7, 10, 14],
  "Dominant minor 9th": [0, 4, 7, 10, 15],
  "Major add 2": [0, 2, 4, 7],
  "Minor add 2": [0, 2, 3, 5],
  "Minor add 9": [0, 4, 7, 14],
  "Major add 4": [0, 4, 5, 7],
  "Major add 6": [0, 4 ,7, 9],
  "major add 6 9": [0, 4 ,7, 9, 14],
  "Major add 7 6": [0, 4, 7, 9, 10],
  "Major mixed 3rd": [0, 4, 7, 3],
  "Jazz suspended": [0, 5, 7, 10, 14],
  "Major 11th": [0, 4,7, 11, 14, 17]
}

def jack_namespace():

    client = jack.Client("MIDI Chord Stacker")

    inport = client.midi_inports.register("in")
    outport = client.midi_outports.register("out")

    NOTEON = 9
    NOTEOFF = 8

    @client.set_process_callback
    def process(frames):
        outport.clear_buffer()
        for offset, data in inport.incoming_midi_events():
            outport.write_midi_event(offset, data) # passthrough
            if len(data) == 3: # this is probably a note event
                event, pitch, vel = struct.unpack("3B", data)
                if event >> 4 in (NOTEON, NOTEOFF): # thanks python!
                    for int in chords[chord.get()]:
                        outport.write_midi_event(offset, (event, pitch + int, vel))
                else:
                    outport.write_midi_event(offset, data)
            else:
                outport.write_midi_event(offset, data)

    client.activate()
    input()   
master = Tk()

chord = StringVar()
chord.set("Pass")
options = OptionMenu(master, chord, *chords.keys())
options.pack()

if __name__ == "__main__":
    Thread(target=jack_namespace).start()
    mainloop()
