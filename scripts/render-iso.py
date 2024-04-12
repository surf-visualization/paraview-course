# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
aLT_PRPB001Avtk = LegacyVTKReader(registrationName='ALT_PRPB001A.vtk', FileNames=['/home/melis/courses/hpc-course/data/ALT_PRPB001A.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
aLT_PRPB001AvtkDisplay = Show(aLT_PRPB001Avtk, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
aLT_PRPB001AvtkDisplay.Representation = 'Outline'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=aLT_PRPB001Avtk)

MIN_VAL = 1281
MAX_VAL = 37120

STEPS = 20
step = (MAX_VAL - MIN_VAL) / (STEPS-1)

for i in range(STEPS):
    
    print('Step %d' % i)

    # Properties modified on contour1
    contour1.Isosurfaces = [MIN_VAL + i*step]

    # show data in view
    contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'

    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get color transfer function/color map for 'scalars'
    scalarsLUT = GetColorTransferFunction('scalars')

    # get opacity transfer function/opacity map for 'scalars'
    scalarsPWF = GetOpacityTransferFunction('scalars')

    # get 2D transfer function for 'scalars'
    scalarsTF2D = GetTransferFunction2D('scalars')

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(893, 585)

    # current camera placement for renderView1
    renderView1.CameraPosition = [336.44564941026204, -40.955401519430424, -310.740377798584]
    renderView1.CameraFocalPoint = [71.5, 71.5, 71.5]
    renderView1.CameraViewUp = [-0.1324838405407721, -0.9719884588926027, 0.19413002800996726]
    renderView1.CameraParallelScale = 123.84163274117472

    # save screenshot
    SaveScreenshot(filename='/home/melis/iso-%02d.png' % i, viewOrLayout=renderView1, location=16, ImageResolution=[893, 585])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(893, 585)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [336.44564941026204, -40.955401519430424, -310.740377798584]
renderView1.CameraFocalPoint = [71.5, 71.5, 71.5]
renderView1.CameraViewUp = [-0.1324838405407721, -0.9719884588926027, 0.19413002800996726]
renderView1.CameraParallelScale = 123.84163274117472


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------