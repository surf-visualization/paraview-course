def render(view, width, height):
  from paraview.vtk import vtkImageData
  image = vtkImageData()
  image.SetDimensions(width, height, 1)
  from paraview.numeric import VTK_UNSIGNED_CHAR
  image.AllocateScalars(VTK_UNSIGNED_CHAR, 4)
  pixel_array = image.GetPointData().GetArray(0)
  pixel_array.FillComponent(0, 255.0)
  pixel_array.FillComponent(1, 0.0)
  pixel_array.FillComponent(2, 0.0)
  pixel_array.FillComponent(3, 0.0)
  return image