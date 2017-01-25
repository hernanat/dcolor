import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import hsv_to_rgb

class DColor:
    def __init__(self, minBright=0.4, samples=3500, xmin=-10, xmax=10, ymin=-10, ymax=10):
        #plot settings
        self._minBright = minBright
        self._samples = samples
        #axes
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
        self.makeDomain()

    def makeDomain(self):
        x = np.linspace(self._xmin, self._xmax, self._samples)
        y = np.linspace(self._ymin, self._ymax, self._samples)
        self.xx, self.yy=np.meshgrid(x,y)

    def makeColorModel(self, zz):
        H = self.normalize(np.mod(np.angle(zz),2*np.pi)) #Hue determined by arg(z)
        r = np.log2(np.add(1.0,np.abs(zz)))
        S = np.divide(np.add(1.0,np.abs(np.sin(np.multiply(2.0*np.pi,r)))),2.0)
        #S = np.ones_like(H)
        V = np.divide(np.add(1.0,np.abs(np.cos(np.multiply(2*np.pi,r)))),2.0)
        #V = np.ones_like(H)

        #V[np.abs(np.subtract(V,0.01))<0.01]+=0.01

        return H,S,V

    def normalize(self, arr):
        arrMin = np.min(arr)
        arrMax = np.max(arr)
        arr = np.subtract(arr,arrMin)
        return np.divide(arr, arrMax-arrMin)

    def plot(self, f, xdim=10, ydim=8, plt_dpi=100):
        x = np.linspace(self._xmin, self._xmax, self._xmax-self._xmin)
        y = np.linspace(self._ymin, self._ymax, self._ymax-self._ymin)

        zz=f(self.z(self.xx,self.yy))
        H,S,V = self.makeColorModel(zz)


        rgb = hsv_to_rgb(np.dstack((H,S,V)))

        fig = plt.figure(figsize=(xdim, ydim), dpi=plt_dpi)
        plt.imshow(rgb)
        plt.gca().invert_yaxis() #make CCW orientation positive
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()

    def z(self, x, y):
        return x+1j*y

dc = DColor()
#dc.plot(lambda z: (z**5+1j*z**4+z**3+1j*z**2+z+1j+1)/np.sin(z))
#dc.plot(lambda z: z)
#dc.plot(lambda z : (1/(1-1j*z))-(1+1j*z))
#dc.plot(lambda z : z**2)
