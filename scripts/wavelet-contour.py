from paraview.simple import *

wavelet = Wavelet()
Show(wavelet)

contour = Contour(Input=wavelet)
contour.Isosurfaces = [200.0]
Show(contour)

SaveScreenshot("iso.png")
