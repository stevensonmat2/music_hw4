from numpy import random
import numpy as np
import math
import sounddevice as sd


class SineModule:
    def play(self, note, duration, attack, is_square=False):
        fs = 48000
        f = 440.0 * (2 ** ((note - 69) / 12))

        sine_wave = np.sin((2 * np.pi * np.arange(fs * duration) * f / fs))

        if is_square:
            sine_wave = np.sign(sine_wave)

        length = len(sine_wave)
        ramp = length * attack

        # got help from class mates on this loop
        for i in range(length):
            if i <= ramp:
                sine_wave[i] *= i / ramp
            else:
                sine_wave[i] *= (length - i) / ramp

        return sine_wave.astype(np.float32)


class Synth:
    def __init__(self, args, sine_module=SineModule()) -> None:
        self.volume = args.volume
        self.accent = args.accent
        self.fs = 48000
        self.sine_module = sine_module
        self.root = args.root
        self.bps = args.bpm / 60
        self.duration = 1 / self.bps
        self.beats = args.beats
        self.attack = args.ramp
        self.stream = sd.Stream(samplerate=self.fs, channels=1)

    def play_sequence(self):
        self.stream.start()
        beats = self.beats

        while True:
            if beats == 0:
                beats = self.beats
            self.stream.write(self.output_data(beats))
            beats -= 1

    def output_data(self, beats):
        duration = self.duration
        attack = self.attack
        is_square = False

        if beats == self.beats:
            note = self.root
            is_square = True
        else:
            note = self.random_note()

        data = self.calculate_amplitude(self.volume) * self.sine_module.play(
            note, duration, attack, is_square=is_square
        )

        return data

    def random_note(self):
        scale_notes = [2, 4, 5, 7, 9, 11, 12]
        note = self.root + random.choice(scale_notes, 1)[0]

        return note

    def calculate_amplitude(self, volume):
        exponent = (-6 * (10 - volume)) / 20
        amplitude = math.pow(10, exponent)

        return amplitude
