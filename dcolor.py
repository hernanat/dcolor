import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import hsv_to_rgb
class DColor:

    def __init__(self, minBright=0.85, samples=2500, xmin=-10, xmax=10, ymin=-10, ymax=10):
        self._minBright = minBright
        self._samples = samples

        self._xmin = xmin
        self._xmax = xmax

        self._ymin = ymin
        self._ymax = ymax

        self.makeDomain()

    def z(self, x, y):
        return x+1j*y


    def makeDomain(self):
        x = np.linspace(self._xmin, self._xmax, self._samples)
        y = np.linspace(self._ymin, self._ymax, self._samples)
        self.xx, self.yy=np.meshgrid(x,y)
        return self.xx,self.yy

    def makeColorModel(self, zz):
        arg = self.normalize(np.mod(np.angle(zz),-2*np.pi))
        mod = self.normalize(np.abs(np.log2(np.abs(zz))))
        mod[mod<self._minBright]=self._minBright
        return arg, mod

    def normalize(self, arr):
        arrMin = np.min(arr)
        arrMax = np.max(arr)
        arr = np.subtract(arr,arrMin)
        return np.divide(arr, arrMax-arrMin)

    def plot(self, f):
        zz=f(self.z(self.xx,self.yy))
        arg,mod = self.makeColorModel(zz)
        s = np.ones_like(arg)
        rgb = hsv_to_rgb(np.dstack((arg,s,mod)))
        fig = plt.figure()
        plt.imshow(rgb)
        ax = plt.gca().invert_yaxis()
        plt.show()

d = DColor()
d.plot(lambda z : z**2)
