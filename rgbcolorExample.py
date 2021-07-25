import numpy as np
import rgbcolor
dc = rgbcolor.DColor()
dc.plot(lambda z : z,title='z expand 2',expand=2)
dc.plot(lambda z : z+2,title='z+2 expand 2',expand=2)
dc.plot(lambda z : z-2,title='z-2 expand 2',expand=2)
dc.plot(lambda z : z+2j,title='z+2j expand 2',expand=2)
dc.plot(lambda z : z-2j,title='z-2j expand 2',expand=2)
dc.plot(lambda z : 1/z,title='1/z expand 2',expand=2)
dc.plot(lambda z : (np.sin(2*np.pi/z)),title='sin(2*np.pi/z)')
dc.plot(lambda z : (np.cos(2*np.pi/z)),title='cos(2*np.pi//z)')
dc.plot(lambda z : np.sin(z),title='sin(z) expand 2',expand=2)
dc.plot(lambda z : np.cos(z),title='cos(z) expand 1',expand=1)
dc.plot(lambda z : z**3 -1,title='z**3 -1 expand 2',expand=2)
dc.plot(lambda z : z**2+2+2j,title='z**2+2+2j expand 2',expand=2)
dc.plot(lambda z : z**8+2+2j,title='z**8+2+2j expand 8',expand=8)
dc.plot(lambda z : z**16+2+2j,title='z**16+2+2j expand 256',expand=256)
dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j) expand .25',expand=.25)
