input = inputs[0]

data_in = inputs[0].PointData["RTData"]
minval = numpy.min(data_in)
maxval = numpy.max(data_in)

data_out = (data_in - minval) / (maxval - minval)
output.PointData.append(data_out, "Normalized")

