from paraview.simple import *

ss = Sphere(Radius=2, ThetaResolution=32)
shr = Shrink(Input=ss)
cs = Cone()
app = AppendDatasets()
app.Input = [shr, cs]
Show(app)
Render()

# SaveScreenshot("out.png", OverrideColorPalette="WhiteBackground")
