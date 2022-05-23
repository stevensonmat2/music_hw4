import numpy as np
from scipy import signal
# from scipy.io import wavfile
# import scipy.io
# import wave

class Effect:
    pass

class Toaster(Effect):

    def apply_effect(self, audio_data):
        return signal.square(audio_data)
        # amplitude = np.iinfo(np.int16).max
        # maxamp = amplitude
        # clipped_data = (amplitude/2) * audio_data

        # for index, frame in enumerate(clipped_data):
        #     if frame > maxamp:
        #         clipped_data[index] = maxamp
        #     elif frame < -maxamp:
        #         clipped_data[index] = -maxamp
            
        # return clipped_data
