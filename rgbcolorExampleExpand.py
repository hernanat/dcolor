import numpy as np
import rgbcolor
dc = rgbcolor.DColor()
dc.plot(lambda z : z,title='z expand 1',expand=1)
dc.plot(lambda z : z,title='z expand 3',expand=3)
dc.plot(lambda z : z+2,title='z+2 expand 1',expand=1)
dc.plot(lambda z : z-2,title='z-2 expand 3',expand=3)
dc.plot(lambda z : 1/z,title='1/z expand 1',expand=1)
dc.plot(lambda z : 1/z,title='1/z expand 3',expand=3)
dc.plot(lambda z : (np.sin(1/z)),title='sin(1/z) expand 1',expand=1)
dc.plot(lambda z : (np.sin(1/z)),title='sin(1/z) expand 3',expand=3)
dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j) expand .25',expand=.25 )
dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j) expand .5',expand=.5 )
dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j) expand 8',expand=8 )
