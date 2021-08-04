#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.colors as mcolors

class DColor:
    def __init__(self, samples=1000, xmin=-8, xmax=8, ymin=-8, ymax=8):
        mpl.rcParams['toolbar'] = 'None'
        self._samples = samples
        #axes
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
        self.makeDomain()

    def makeDomain(self):
        """Create the domains for Real (x) and Imaginary (y) values respectively"""
        x = np.linspace(self._xmin, self._xmax, self._samples)
        y = np.linspace(self._ymin, self._ymax, self._samples)
        self.xx, self.yy=np.meshgrid(x,y)

    def makeColorModel(self, zz):
        """Create the HSV color model for the function domain that will be plotted"""
        H = self.normalize(np.angle(zz) % (2. * np.pi)) #Hue determined by arg(z)
        r = np.log2(1. + np.abs(zz))
        S = (1. + np.abs(np.sin(2. * np.pi * r))) / 2.
        V = (1. + np.abs(np.cos(2. * np.pi * r))) / 2.

        return H,S,V

    def normalize(self, arr):
        """Used for normalizing data in array based on min/max values"""
        arrMin = np.min(arr)
        arrMax = np.max(arr)
        arr = arr - arrMin
        return arr / (arrMax - arrMin)

    def plot(self, f, xdim=8, ydim=8, plt_dpi=100,title=''):
        """Plot a complex-valued function
            Arguments:
            f -- a (preferably) lambda-function defining a complex-valued function
            Keyword Arguments:
            xdim -- x dimensions
            ydim -- y dimensions
            plt_dpi -- density of pixels per inch
        """
        fig = plt.figure(figsize=(xdim, ydim), dpi=plt_dpi)
        ax = fig.gca()
        val = str('x xmin=')
        val = val + str(self._xmin) + " xmax=" + str(self._xmax)
        ax.set_xlabel(val)
        val = str('y ymin=')
        val = val + str(self._ymin) + " xmax=" + str(self._ymax)
        ax.set_ylabel(val)
        zz=f(self.z(self.xx,self.yy))
        H,S,V = self.makeColorModel(zz)
        image = np.dstack((H,S,V))
        image = np.reshape(image,(len(self.xx),len(self.yy),3))
        ax.imshow(image)
        ax.invert_yaxis() #make CCW orientation positive
        ax.get_xaxis().set_visible(True)
        ax.get_yaxis().set_visible(True)
        ax.set_title(title)
        plt.show()

    def z(self, x, y):
        """return complex number x+iy
            If inputs are arrays, then it returns an array with corresponding x_j+iy_j values
        """
        return x+1j*y

