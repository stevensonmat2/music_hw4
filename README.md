Matt Stevenson
HW 4 Aleatoric

For this project I reused a lot from other projects from this class. I used a synth class to manage my audio stream and a sound module class to generate the waves. For the envelope, I multiplied frames in my note array using the ramp value in a two equations for the first and last halves of the note array. 

Implementing the random note selection was pretty straight forward, but the enevelope was very difficult for me.
After working with class mates and changing from pyaudio to sounddevice I was able to get the envelope working.

To run, just use "python3 main.py" with whatever args you want as required by the rubric.

A source for some ideas I used: https://sidparida.com/category/python-audio-synthesis-from-scratch/
