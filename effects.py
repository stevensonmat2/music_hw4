import numpy as np
from scipy import signal


class Effect:
    pass

class Sqaure(Effect):

    def apply_effect(self, audio_data):
        return signal.square(audio_data)