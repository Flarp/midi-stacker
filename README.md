# midi-stacker
Small Python JACK program that creates chords from MIDI notes

## Why?

I made this program due to my frustrations with [x42's MidiFilter plugin](https://github.com/x42/midifilter.lv2). I'm sure they were made in good faith, but the chord plugin is absolutely abysmal; you can only use major intervals, and you can only use notes if they fit inside a scale. This pretty much means you're stuck with major chords but only if the root note falls into a major scale (if you play a note outside the major scale, it simply won't even try to make the chord)

This program fits all my needs (all you need to do is connect a MIDI device into its `in` port, select a chord quality from the GUI, and connect the `out` port to the desired destination) but I will eventually add the ability to manually modify intervals.
