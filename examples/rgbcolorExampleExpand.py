import numpy as np
import sys
sys.path.append('..')
import rgbcolor
dc = rgbcolor.DColor()
dc.plot(lambda z : z**2+4+4j,title='z**2+4+4j')
dc.plot(lambda z : z**8+4+4j,title='z**8+4+4j expand 8',expand=8)
dc.plot(lambda z : z**16+4+4j,title='z**16+4+4j expand 256',expand=256)
