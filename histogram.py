from paraview.vtk import vtkImageData
from paraview import python_view

def render(view, width, height):
	print("render(view, %d, %d)" % (width, height))

    n = view.GetNumberOfVisibleDataObjects()
	for idx in range(n):
	    dataobj = view.GetVisibleDataObjectForSetup(idx)
		print("Memory size:", dataobj.GetActualMemorySize(), "kilobytes")

	#dataObject = view.GetVisibleDataObjectForRendering(0)
	#scalars = dataObject.GetPointData().GetArray('scalars')

	figure = python_view.matplotlib_figure(width, height)
	ax = figure.add_subplot(1,1,1)
	ax.minorticks_on()
	ax.set_title('Plot title')
	ax.set_xlabel('X label')
	ax.set_ylabel('Y label')

	return python_view.figure_to_image(figure)