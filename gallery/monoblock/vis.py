from paraview.simple import *

# Create a sphere of radius = 2, theta res. = 32
# This object becomes the active source.
ss = Sphere(Radius=2, ThetaResolution=32)
# Apply the shrink filter. The Input property is optional. If Input
# is not specified, the filter is applied to the active source.
shr = Shrink(Input=ss)
# Create a cone source.
cs = Cone()
# Append cone and shrink
app = AppendDatasets()
app.Input = [shr, cs]
# Show the output of the append filter. The argument is optional
# as the app filter is now the active object.
Show(app)
# Render the default view.
Render()

SaveScreenshot("out.png", OverrideColorPalette="WhiteBackground")
