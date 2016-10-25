xyscope - a little X/Y oscilloscope written in Python
=====================================================

xyscope is a simple x/y oscilloscope which can be used to view stereo wav files.

Usage:
------
`python -m xyscope [-a attack] [-d decay] [-f samples] [-s smooth] [-w delay] file.wav`
    
attack - the brightness that a displayed pixel gains when the beam strikes it.
decay - the brightness that a displayed pixel loses every frame.
samples - the number of samples to be displayed every frame.
smooth - applies a resampler to smooth the displayed waveform out.
delay - an amount of time to sleep between frames.

Dependencies:
-------------
numpy, scipy, Pillow.

License:
--------
GNU GPL v3.