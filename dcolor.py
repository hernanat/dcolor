import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import hsv_to_rgb
class DColor:

    def __init__(self):

        self._minBright = 0.85
        self._samples = 2500

        self._xmin = -10
        self._xmax = 10

        self._ymin = -10
        self._ymax = 10

        self.makeGrid()

    def f(self,x,y):
        z=x+1j*y
        #return np.sin(1/z)
        return z
    def g(self,x, y):
        s = x + 1j*y
        return (s+2)/(s**2 + s + 1)


    def makeGrid(self):
        x = np.linspace(self._xmin, self._xmax, self._samples)
        y = np.linspace(self._ymin, self._ymax, self._samples)
        self.xx, self.yy=np.meshgrid(x,y)
        return self.xx,self.yy

    def makeColorModel(self, zz):
        arg = self.normalize(np.mod(np.angle(zz),-2*np.pi))
        mod = self.normalize(np.abs(np.log2(np.abs(zz))))
        mod = [[self._minBright if x < self._minBright else x for x in m] for m in mod]
        return arg, mod

    def normalize(self, arr):
        arrMin = np.min(arr)
        arrMax = np.max(arr)
        arr = np.subtract(arr,arrMin)
        return np.divide(arr, arrMax-arrMin)

    def plot(self):
        zz=self.g(self.xx,self.yy)
        arg,mod = self.makeColorModel(zz)
        s = np.ones_like(arg)
        rgb = hsv_to_rgb(np.dstack((arg,s,mod)))
        fig = plt.figure()
        plt.imshow(rgb)
        ax = plt.gca().invert_yaxis()
        plt.show()

d = DColor()
d.plot()
