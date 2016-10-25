xyscope - a little X/Y oscilloscope written in Python
=====================================================

xyscope is a simple x/y oscilloscope which can be used to view stereo wav files.

Usage
-----
`python -m xyscope [-a attack] [-d decay] [-f samples] [-s smooth] [-w delay] [-x width] [-y height] file.wav`<br />
    
attack - the brightness that a displayed pixel gains when the beam strikes it.<br />
decay - the brightness that a displayed pixel loses every frame.<br />
samples - the number of samples to be displayed every frame.<br />
smooth - applies a resampler to smooth the displayed waveform out.<br />
delay - an amount of time to sleep between frames.<br />
width - the width of the plot.<br />
height - the height of the plot.<br />

Dependencies
------------
numpy, scipy, Pillow.

License
-------
GNU GPL v3.
