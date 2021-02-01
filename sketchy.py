#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Chris Morgan <christoph.morgan@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from scipy.ndimage.filters import gaussian_filter1d as gaussian
from PIL import Image
import numpy as pd
import pandas as pd
import argparse
import os
import pathlib

class Image:
    """Represents the raw formt of an image that is loaded"""

    def __init__(self, path):
        self.path = path
        self.form = path[-3:].capitalize()
        self.pil = Image(path)

    def __repr__(self):
        return """
            Path: {},
            Height:{},
            Width: {},
            Color Mode: {},
            Format: {}
            """.format(self.path, self.pil.height, self.pil.width, self.pil.mode, self.form)

    def __str__(self):
       return """
            \nPath: {},
            \nHeight:{},
            \nWidth: {},
            \nColor Mode: {},
            \nFormat: {}
            """.format(self.path, self.pil.height, self.pil.width, self.pil.mode, self.form)

    def plot(self):
        self.pil.show()

class Raster:
    """ Receives an Image class object and returns a three
        dimensionsal numpy array """

    def __init__(self, img):
        self.raster = np.array(img.pil)
        self.x = self.raster.shape[0]
        self.y = self.raster.shape[1]
        self.z = self.raster.shape[2]

    def posterize(self, args.thresh):
        """ Amplify the RGB color strength of colors by setting all colors,
            over a defined strength to the maximum strengh of 255 """
        self.raster[self.raster > args.thresh] = 255

    def isolate_color(self,raster):
        """ Filter color bands rasters and only select values with
            a maximum strength of 255 """

        # Create seperate raster images for individual color bands
        raster = self.raster

        red = raster.copy()
        green = raster.copy()
        blue = raster.copy()
        black = raster.copy()

        # create color channels
        cred = raster[..., 0] == 255
        cgreen = raster[..., 1] == 255
        cblue = raster[..., 2] == 255

        # isolate colors
        black[cred | cgreen | cblue ] = [255, 255, 255]
        red[cgreen | cblue ] = [255, 255, 255]
        green[cred | cblue ] = [255, 255, 255]
        blue[cred | cgreen ] = [255, 255, 255]

        #remove blacks
        for color in [red, green, blue]:
            color = color - black + 255

        self.red = red
        self.green = green
        self.blue = blue
        self.black = black

    def verify_colors(band):
        pass

    def create_series(band):
        return TimeSeries()

    def plot(band):
        plt.imshow(band)
        plt.show()
        pass


class TimeSeries:
    "blablbalbla"

    def __init__():
        pass

    def smoothen():
        pass

    def scale_axes():
        pass

    def plot():
        pass

def sketchy(args):
    """
    """

    # images
    img = Image(args.path)
    if arg.debug_plot()
        img.plot()

    # rasters
    raster = Raster(img)
    raster.posterize(args.threshold)
    raster.isolate_colors()

    for band in ["red", "green", "blue", "black"]:
        rb = raster.__dict__[band]
        rb.verify_colors()
        rb.get_ordinates()
        if args.debug_plot:
            rb.plot()
        if rb.verified:
            rb.series = create_timeseries()

    #timeseries
    for band in raster.verified:
        band.series.smoothen()
        band.series.scale_axes()
        #export
        band.series.write_header()
        band.series.export_zrxp()

if __name__ == "__main__":
    #add all parsing options

    parser = argparse.ArgumentParser(
    description='Load a simple time series sketch and convert it to a time series',
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='input file',
    )
    parser.add_argument(
        '-x', '--xrange',
        dest='xrange',
        default=("2020-01-01", "2020-01-07")
        type=tuple,
        help='Specify as a tuple the minimum and maximum extend of the x-axis bar (min,max)',
    )
    parser.add_argument(
        '-dt', '--delta',
        dest='delta',
        default="15T"
        type=string,
        help='Specify the desired time stamp interval duration, i.e. 15T, 2D',
    )
    parser.add_argument(
        '-y', '--yrange' ,
        dest='yrange',
        default='(-10,30)'
        type=tuple,
        help='Specify as a tuple the minimum and maximum extend of the y-axis bar (min,max)',
    )

    def color_subset(s):
        result = all(elem in list("rgbk") for elem in list(s))
        if result:
            return s
        else:
            msg('%s is not a subset of "rgbk", please provide a string permutation of these four characters')
            raise argparse.ArgumentTypeError(msg)

    parser.add_argument(
        '-c', '--colors',
        dest='color'
        type=color_subset,
        default="rgbk",
        help='Specify the colors to process as a string of characters'
    )
    parser.add_argument(
        '-b, --batch',
        dest='batch',
        type=string,
        default=None,
        help='Pass option to read an external csv which will batch process the entries'
    )
    sys.argv = ["sketchy.py  "Code/sketchseries/Validation/test1.jpg"]
    args = parser.parse_args()
    if args.batch not None:
        # loop through configurations stored in a csv file
        # For guidance on the format of the csv, see
        # csv example
        batches = pd.read_csv(args.batch, sep=',')
        for batch in batches:
            sketchy(params..)
    else:
        sketchy(args)
