from dcolor import dc

#dc.showPlot(lambda z : (z**5+1j*z**4+z**3+1j*z**2+z+1j+1)/np.sin(z))
dc.savePlot(lambda z : z**3+2j*z**2+2j+z,"foo.jpg")
dc.showPlot(lambda z : (1/(1-1j*z))-(1+1j*z))
# dc.showPlot(lambda z : z**3)
# dc.showPlot(lambda z : ((z+1-2j)*(z+2+2j)*((z-2)**2))/(z**3))
# dc.showPlot(lambda z : np.sin(z))
