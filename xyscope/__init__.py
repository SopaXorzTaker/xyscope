import sys
import tkinter
import argparse
import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal
from PIL import Image, ImageTk


class XYScope(object):
    def _update_image(self):
        photo_image = ImageTk.PhotoImage(self.image)
        self.panel.configure(image=photo_image)
        self.panel.image = photo_image

    def _render_frame(self):
        pixels = self.image.load()

        samples = self.samples[self.sample_index:self.sample_index + self.frame_samples]
        rollover = self.frame_samples - len(samples)

        if rollover:
            samples = np.concatenate(samples, self.samples[:rollover])

        self.sample_index += 1
        self.sample_index %= len(self.samples)

        samples = signal.resample(samples, len(samples) * self.smooth)

        # Decay the displayed picture
        for x in range(self.width):
            for y in range(self.height):
                r, g, b = pixels[x, y]
                g -= self.decay

                if g < 0:
                    g = 0

                pixels[x, y] = (r, g, b)

        for sample in samples:
            left, right = sample

            left /= 65536
            right /= 65536

            x_scale = self.width / 2
            y_scale = self.height / 2

            x = int(x_scale + left * x_scale)
            y = int(y_scale + right * y_scale)

            r, g, b = pixels[x, y]
            g += self.attack

            if g > 255:
                g = 255

            pixels[x, y] = (r, g, b)

    def _next_frame(self):
        self._render_frame()
        self._update_image()
        self.root.after(self.delay, self._next_frame)

    def __init__(self):
        parser = argparse.ArgumentParser(prog=sys.modules[__name__].__name__,
                                         description="View a stereo wave file in a X/Y scope.")
        parser.add_argument("filename", type=str, help="The wave file to read")
        parser.add_argument("-a", "--attack", type=int, default=128, help="The attack value")
        parser.add_argument("-d", "--decay", type=int, default=64, help="The decay value")
        parser.add_argument("-f", "--frame-samples", type=int, default=0, help="The samples rendered per frame")
        parser.add_argument("-s", "--smooth", type=int, default=32, help="Factor of smoothing the drawn lines")
        parser.add_argument("-w", "--delay", type=int, default=10, help="Delay between the frames")
        parser.add_argument("-x", "--width", type=int, default=256, help="Width of the plot")
        parser.add_argument("-y", "--height", type=int, default=256, help="Height of the plot")
        params = parser.parse_args()

        self.file_name, self.attack, self.decay, self.frame_samples, self.smooth, self.delay, self.width, self.height =\
            params.filename, params.attack, params.decay, params.frame_samples, params.smooth, params.delay,\
            params.width, params.height

        self.sample_rate, self.samples = wavfile.read(self.file_name)
        self.sample_index = 0

        if not isinstance(self.samples[0], np.ndarray) or len(self.samples[0]) is not 2:
            parser.exit(1, "error: the file must be stereo!\n")

        if not self.frame_samples:
            self.frame_samples = self.sample_rate // (self.delay * 100)

        self.image = Image.new("RGB", (self.width, self.height))

        self.root = tkinter.Tk()
        self.root.title("X/Y scope")
        self.panel = tkinter.Label(self.root)
        self._update_image()
        self.panel.pack()
        self._next_frame()
        self.root.mainloop()
