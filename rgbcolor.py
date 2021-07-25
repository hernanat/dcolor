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

    def makeRGB(self, zz,expand) :
        absz = np.abs(zz)
        expand = 1/expand
        r = expand*absz*.5
        g = expand*absz*1.00
        b = expand*absz*.5
        r = np.clip(r,0,1)
        g = np.clip(g,0,1)
        b = np.clip(b,0,1)
        return np.dstack((r,g,b))

    def plot(self, f, xdim=8, ydim=8, plt_dpi=100,title="none",expand=1):
        """Plot a complex-valued functionq
            f -- a (preferably) lambda-function defining a complex-valued function
            Keyword Arguments:
            xdim -- x dimensions
            ydim -- y dimensions
            plt_dpi -- density of pixels per inch
        """
        zz=f(self.z(self.xx,self.yy))
        rgb = self.makeRGB(zz,expand)
        fig = plt.figure(figsize=(xdim, ydim), dpi=plt_dpi)
        ax = fig.gca()
        val = str('x xmin=')
        val = val + str(self._xmin) + " xmax=" + str(self._xmax)
        ax.set_xlabel(val)
        val = str('y ymin=')
        val = val + str(self._ymin) + " xmax=" + str(self._ymax)
        ax.set_ylabel(val)
        ax.imshow(rgb)
        ax.invert_yaxis() # make CCW orientation positive
        ax.get_xaxis().set_visible(True)
        ax.get_yaxis().set_visible(True)
        ax.set_title(title)
        plt.show()

    def z(self, x, y):
        """return complex number x+iy
            If inputs are arrays, then it returns an array with corresponding x_j+iy_j values
        """
        return x+1j*y
