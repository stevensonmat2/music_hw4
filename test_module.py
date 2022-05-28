import numpy as np


class TestModule:
    def __init__(self) -> None:
        self.phase = 0

    def play(self, note, attack):


        fs = 48000  # sampling rate, Hz, must be integer
        duration = 1  # in seconds, may be float
        f = 440.0  # sine frequency, Hz, may be float
        f = (f / 32) * (2 ** ((note - 9) / 12))  # converts midi note to hz

        samples = (np.sin((2*np.pi*np.arange(fs*duration)*f/fs)))

        return samples.astype(np.float32)
