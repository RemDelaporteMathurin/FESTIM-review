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
zoom = 1.3
renderView1.CameraPosition = [
    zoom * 0.03037131659597036,
    zoom * 0.018874920820419597,
    zoom * -0.033570685008386496,
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

# create a new 'Xdmf3ReaderS'
retentionxdmf = Xdmf3ReaderS(
    registrationName="retention.xdmf", FileName=["./retention.xdmf"]
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from retentionxdmf
retentionxdmfDisplay = Show(
    retentionxdmf, renderView1, "UnstructuredGridRepresentation"
)

# go to last timestep
last_timestep = retentionxdmf.TimestepValues[-1]
retentionxdmf.UpdatePipeline(last_timestep)

animationScene1 = GetAnimationScene()
animationScene1.GoToLast()

# set scalar coloring
ColorBy(retentionxdmfDisplay, ("POINTS", "retention"))

# get min and max of Color
info = retentionxdmf.GetDataInformation().DataInformation
arrayInfo = info.GetArrayInformation(
    "retention", vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS
)
min_inv, max_inv = arrayInfo.GetComponentRange(0)
print(f"minimum: {min_inv}, maximum: {max_inv}")

comsol_max = 1.2506265243486008e22  # match the max from comsol for comparison

# get color transfer function/color map for 'Color'
colorLUT = GetColorTransferFunction("retention")

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
colorLUT.ApplyPreset("Viridis (matplotlib)", True)
colorLUT.RescaleTransferFunction(0, comsol_max)


op = GetOpacityTransferFunction("retention")
op.RescaleTransferFunction(0, comsol_max)

# setup the color legend parameters for each legend in this view

# get color legend/bar for colorLUT in view renderView1
colorLUTColorBar = GetScalarBar(colorLUT, renderView1)
colorLUTColorBar.WindowLocation = "Any Location"
colorLUTColorBar.HorizontalTitle = 1
colorLUTColorBar.Position = [0.60, 0.25]
colorLUTColorBar.Title = "H/m$^3$"
colorLUTColorBar.TitleJustification = "Left"
# colorLUTColorBar.ScalarBarLength = 0.5
colorLUTColorBar.ComponentTitle = ""
colorLUTColorBar.AutomaticLabelFormat = 0
colorLUTColorBar.LabelFormat = "%-#6.1e"
colorLUTColorBar.TitleFontSize = 32
colorLUTColorBar.LabelFontSize = 32
# colorLUTColorBar.UseCustomLabels = 1
# colorLUTColorBar.CustomLabels = [5e20, 6e20]
# set color bar visibility
colorLUTColorBar.Visibility = 1

# show color legend
retentionxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(retentionxdmf)
# ----------------------------------------------------------------

LoadPalette(paletteName="WhiteBackground")
ExportView("retention_festim.pdf", view=renderView1, Rendertextaspaths=0)
SaveScreenshot("retention_festim.png", renderView1)

if __name__ == "__main__":
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory="extracts")
