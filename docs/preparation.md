# Preparation

In this course we are going to use ParaView and a number of datasets provided for the course. Both can be downloaded and installed using the instructions below. This course assumes that you brought your own laptop, or if not, that you can work together with someone else that does have a laptop.

## Course materials share

All course materials, data files and ParaView binaries can be found at https://edu.nl/k6ttu.

## Install ParaView

In this course we are going to use ParaView. ParaView is an open-source, multi-platform scientific visualization and data analysis application. It is available for 
Windows, MacOS X and Linux. We provide ParaView binaries for this course in the course materials share (see above).

This guide has been written for ParaView version **5.8**. Between ParaView versions small differences in GUI (and functionality) exist, but most of what is written in these notes should be easy to apply to other versions of ParaView. 

!!! Warning

    An important difference between ParaView version 5 and earlier versions is that the new ParaView version requires a GPU that supports OpenGL 3.2 or higher. Older PCs/laptops and systems with Intel Integrated graphics may not support this. There are two options to work around this limitation:

    1. Start ParaView (5.0) from the command line with the --mesa-llvm flag, e.g. paraview --mesa-llvm. This enables CPU-based software rendering (not using the GPU at all). This will be slower than rendering on the GPU, but should work on any system.

    2. Use an older version of ParaView, like 4.4 (available from http://www.paraview.org/download). In this case the GUI and menu options will be slightly different in naming, placement and look compared that what is described in these notes.


## Download and extract data

The ZIP files with data used in this workshop can be found in the course materials share (see above).

▶ Unzip the data file to a directory of your choice. 

This directory will now have 4 datasets:

* `headsq_masked.vtk`: This is a CT scan of a boy's head. The data consists of a regular grid of 255x255x93 voxels, containing scalar values for the density of the scanned tissue. (The original dataset consisted of 93 separate files containing binary data, unsigned shorts with connectivity bits. For this course, we pre-processed the file for easier use).
* `wervel.csv`: This is a Comma Separated Value file, containing a list of 3D points and their velocity vectors, representing a snapshot of a simulation of a tornado. 
* `ALT_PRPB001A.vtk`: This file contains the results of a simulation of a coral growth. The scalars in this file represent the time of growth of a coral (this data is provided courtesy of Jaap Kaandorp , Section Computational Science, UvA).
* `SMRX.vtk`: This is a flow simulation of a viscous fluid through a stationary mixer (this data is provided courtesy of Drona Kandhai, Section Computational Science, UvA).

The remainder of this document contains four exercises based on these datasets.