# state file generated using paraview version 5.11.2
import paraview
import vtk

paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView("RenderView")
renderView1.ViewSize = [3520, 1828]
renderView1.AxesGrid = "GridAxes3DActor"
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-0.00575, 0.001, 0.00175]
renderView1.StereoType = "Crystal Eyes"
renderView1.CameraPosition = [
    0.03037131659597036,
    0.018874920820419597,
    -0.033570685008386496,
]
renderView1.CameraFocalPoint = [
    -0.005750000000000002,
    0.0010000000000000022,
    0.0017499999999999992,
]
renderView1.CameraViewUp = [-0.2030164501449332, 0.9415375759855025, 0.2688704408779333]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.013869931506680198

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name="Layout #1")
layout1.AssignView(0, renderView1)
layout1.SetSize(3520, 1828)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
inventoryvtu = XMLUnstructuredGridReader(
    registrationName="inventory.vtu",
    FileName=["inventory.vtu"],
)
inventoryvtu.PointArrayStatus = ["Color"]
inventoryvtu.TimeArray = "None"

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from inventoryvtu
inventoryvtuDisplay = Show(inventoryvtu, renderView1, "UnstructuredGridRepresentation")

# set scalar coloring
ColorBy(inventoryvtuDisplay, ("POINTS", "Color"))

# get min and max of Color
info = inventoryvtu.GetDataInformation().DataInformation
arrayInfo = info.GetArrayInformation(
    "Color", vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS
)
min_inv, max_inv = arrayInfo.GetComponentRange(0)

# get color transfer function/color map for 'Color'
colorLUT = GetColorTransferFunction("Color")

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
colorLUT.ApplyPreset("Viridis (matplotlib)", True)
colorLUT.RescaleTransferFunction(0, max_inv)

op = GetOpacityTransferFunction("Color")
op.RescaleTransferFunction(0, max_inv)

# setup the color legend parameters for each legend in this view

# get color legend/bar for colorLUT in view renderView1
colorLUTColorBar = GetScalarBar(colorLUT, renderView1)
colorLUTColorBar.WindowLocation = "Any Location"
colorLUTColorBar.Position = [0.7769886363636364, 0.25547045951859954]
colorLUTColorBar.Title = "Color"
colorLUTColorBar.ComponentTitle = ""

# set color bar visibility
colorLUTColorBar.Visibility = 1

# show color legend
inventoryvtuDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(inventoryvtu)
# ----------------------------------------------------------------

if __name__ == "__main__":
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory="extracts")
