from test_module import TestModule
from effects import Toaster
import pyaudio
import time

class Synth:
    """
    Manages all components that comprise a synth, including the audio stream, a sound generator,
    a midi interface, and an optional effect.
    """

    def __init__(self, args, sound_moudle=TestModule(), effect=Toaster()) -> None:

        self.p = pyaudio.PyAudio()
        self.volume = args.volume  # range [0.0, 1.0]
        self.fs = 48000  # sampling rate, Hz, must be integer
        # self.midi_interface = MidiInterface(self.process_midi)
        self.sound_module = sound_moudle
        self.effect = effect
        self.root = args.root
        self.bps = 60 / args.bpm
        self.beats = args.beats
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.fs,
            output=True,
        )

    def play_sequence(self):
        """
        Begins the audio stream, and continuously writes wave data to the output stream based
        on midi input.
        """
        self.stream.start_stream()
        beats = self.beats
        while True:
            if beats == 0:
                beats = self.beats
            self.stream.write(self.output_data(beats))
            time.sleep(self.bps)
            beats -= 1

    def output_data(self, beats):
        """
        Applies volume and effects to final wave data
        """
        apply_effect = False

        if beats == self.beats:
            note = self.root
            apply_effect = True
        else:
            note = self.random_note()

        data = self.volume * self.sound_module.play(note)
        if apply_effect:
            data = self.effect.apply_effect(data)
        return data

    def random_note(self):
        return self.root