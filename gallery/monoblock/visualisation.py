# state file generated using paraview version 5.11.1
import paraview

paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
toroidal_view = CreateView("RenderView")
toroidal_view.ViewSize = [1920, 1440]
toroidal_view.InteractionMode = "2D"
toroidal_view.AxesGrid = "GridAxes3DActor"
toroidal_view.OrientationAxesVisibility = 0
toroidal_view.CenterOfRotation = [
    -9.999999717180685e-10,
    0.009902089601382613,
    0.0012499999720603228,
]
toroidal_view.UseLight = 0
toroidal_view.StereoType = "Crystal Eyes"
toroidal_view.CameraPosition = [
    0.013740840533351903,
    0.009678529307796436,
    -0.00048013618639282716,
]
toroidal_view.CameraFocalPoint = [
    -9.999999717180685e-10,
    0.009678529307796436,
    -0.00048013618639282716,
]
toroidal_view.CameraFocalDisk = 1.0
toroidal_view.CameraParallelScale = 0.005206912772554821
toroidal_view.BackEnd = "OSPRay raycaster"
toroidal_view.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
poloidal_view = CreateView("RenderView")
poloidal_view.ViewSize = [2892, 1545]
poloidal_view.InteractionMode = "2D"
poloidal_view.AxesGrid = "GridAxes3DActor"
poloidal_view.OrientationAxesVisibility = 0
poloidal_view.CenterOfRotation = [0.0, 0.0010000001639127731, 9.999999717180685e-10]
poloidal_view.UseLight = 0
poloidal_view.StereoType = "Crystal Eyes"
poloidal_view.CameraPosition = [0.0, 0.0010000001639127731, 0.06562611401245706]
poloidal_view.CameraFocalPoint = [0.0, 0.0010000001639127731, 9.999999717180685e-10]
poloidal_view.CameraFocalDisk = 1.0
poloidal_view.CameraParallelScale = 0.016985287903674255
poloidal_view.BackEnd = "OSPRay raycaster"
poloidal_view.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
retention_3d_view = CreateView("RenderView")
retention_3d_view.ViewSize = [1920, 1440]
retention_3d_view.AxesGrid = "GridAxes3DActor"
retention_3d_view.OrientationAxesVisibility = 0
retention_3d_view.CenterOfRotation = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]
retention_3d_view.StereoType = "Crystal Eyes"
retention_3d_view.CameraPosition = [
    0.029187531898639388,
    0.021267593211478808,
    -0.033650063037602,
]
retention_3d_view.CameraFocalPoint = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]
retention_3d_view.CameraViewUp = [
    -0.25512670601409737,
    0.9249482042923544,
    0.2817466650286133,
]
retention_3d_view.CameraFocalDisk = 1.0
retention_3d_view.CameraParallelScale = 0.013815752050297017
retention_3d_view.BackEnd = "OSPRay raycaster"
retention_3d_view.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
geometry_view = CreateView("RenderView")
geometry_view.ViewSize = [1920, 1440]
geometry_view.AxesGrid = "GridAxes3DActor"
geometry_view.OrientationAxesVisibility = 0
geometry_view.CenterOfRotation = [-0.00575, 0.001, 0.00175]
geometry_view.UseLight = 0
geometry_view.StereoType = "Crystal Eyes"
geometry_view.CameraPosition = [
    0.03527525163972251,
    0.028756112770091793,
    -0.04017562245348884,
]
geometry_view.CameraFocalPoint = [
    -0.0067691074961900195,
    -0.0002652169498046825,
    -0.00024248032049179464,
]
geometry_view.CameraViewUp = [
    -0.299472437450573,
    0.8936709499800797,
    0.3341683593177468,
]
geometry_view.CameraFocalDisk = 1.0
geometry_view.CameraParallelScale = 0.013869931506680198
geometry_view.BackEnd = "OSPRay raycaster"
geometry_view.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name="Layout #1")
layout1.AssignView(0, poloidal_view)
layout1.SetSize(2892, 1545)

# create new layout object 'Layout #2'
layout2 = CreateLayout(name="Layout #2")
layout2.AssignView(0, toroidal_view)
layout2.SetSize(1920, 1440)

# create new layout object 'Layout #3'
layout3 = CreateLayout(name="Layout #3")
layout3.AssignView(0, retention_3d_view)
layout3.SetSize(1920, 1440)

# create new layout object 'Layout #4'
layout4 = CreateLayout(name="Layout #4")
layout4.AssignView(0, geometry_view)
layout4.SetSize(1920, 1440)

# ----------------------------------------------------------------
# restore active view
SetActiveView(poloidal_view)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Xdmf3ReaderS'
mesh_cellsxdmf = Xdmf3ReaderS(
    registrationName="mesh_cells.xdmf", FileName=["./mesh/mesh_cells.xdmf"]
)
mesh_cellsxdmf.CellArrays = ["f"]

# create a new 'Slice'
slice2 = Slice(registrationName="Slice2", Input=mesh_cellsxdmf)
slice2.SliceType = "Plane"
slice2.HyperTreeGridSlicer = "Plane"
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.00575, 0.001, 0.00175]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [-0.00575, 0.001, 0.00175]

# create a new 'Xdmf3ReaderS'
temperaturexdmf = Xdmf3ReaderS(
    registrationName="temperature.xdmf",
    FileName=["./temperature.xdmf"],
)

# create a new 'Xdmf3ReaderS'
mobile_concentrationxdmf = Xdmf3ReaderS(
    registrationName="mobile_concentration.xdmf",
    FileName=["./mobile_concentration.xdmf"],
)

# create a new 'Slice'
poloidalsection = Slice(
    registrationName="Poloidal section", Input=mobile_concentrationxdmf
)
poloidalsection.SliceType = "Plane"
poloidalsection.HyperTreeGridSlicer = "Plane"
poloidalsection.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
poloidalsection.SliceType.Origin = [
    -1e-09,
    0.0010000001639127731,
    0.0012499999720603228,
]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
poloidalsection.HyperTreeGridSlicer.Origin = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]

# create a new 'Slice'
toroidalsection = Slice(
    registrationName="Toroidal section", Input=mobile_concentrationxdmf
)
toroidalsection.SliceType = "Plane"
toroidalsection.HyperTreeGridSlicer = "Plane"
toroidalsection.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
toroidalsection.SliceType.Origin = [-0.005750000011175871, 0.0010000001639127731, 1e-09]
toroidalsection.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
toroidalsection.HyperTreeGridSlicer.Origin = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]

# create a new 'Reflect'
reflect1 = Reflect(registrationName="Reflect1", Input=toroidalsection)
reflect1.Plane = "X Max"
reflect1.CopyInput = 0

# create a new 'Slice'
poloidalsection_1 = Slice(registrationName="Poloidal section", Input=temperaturexdmf)
poloidalsection_1.SliceType = "Plane"
poloidalsection_1.HyperTreeGridSlicer = "Plane"
poloidalsection_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
poloidalsection_1.SliceType.Origin = [
    -1e-09,
    0.0010000001639127731,
    0.0012499999720603228,
]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
poloidalsection_1.HyperTreeGridSlicer.Origin = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]

# create a new 'Gradient'
gradient1 = Gradient(registrationName="Gradient1", Input=reflect1)
gradient1.ScalarArray = ["POINTS", "mobile_concentration"]

# create a new 'Transform'
transform2 = Transform(registrationName="Transform2", Input=slice2)
transform2.Transform = "Transform"

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [0.0, 0.0, -0.003]

# create a new 'Contour'
contour2 = Contour(registrationName="Contour2", Input=poloidalsection_1)
contour2.ContourBy = ["POINTS", "temperature"]
contour2.Isosurfaces = [
    333.56124884246157,
    358.33621960453513,
    383.1111903666087,
    407.88616112868226,
    432.6611318907559,
    457.4361026528294,
    482.211073414903,
    506.9860441769766,
    531.7610149390501,
    556.5359857011238,
    581.3109564631973,
    606.0859272252708,
    630.8608979873445,
    655.635868749418,
    680.4108395114915,
    705.1858102735652,
    729.9607810356388,
    754.7357517977123,
    779.5107225597858,
    804.2856933218594,
    829.060664083933,
    853.8356348460065,
    878.61060560808,
    903.3855763701538,
    928.1605471322273,
    952.9355178943008,
    977.7104886563745,
    1002.485459418448,
    1027.2604301805216,
    1052.035400942595,
]
contour2.PointMergeMethod = "Uniform Binning"

# create a new 'Xdmf3ReaderS'
retentionxdmf = Xdmf3ReaderS(
    registrationName="retention.xdmf",
    FileName=["./retention.xdmf"],
)

# create a new 'Reflect'
reflect2 = Reflect(registrationName="Reflect2", Input=poloidalsection)
reflect2.Plane = "Z Min"
reflect2.CopyInput = 0

# create a new 'Gradient'
gradient2 = Gradient(registrationName="Gradient2", Input=reflect2)
gradient2.ScalarArray = ["POINTS", "mobile_concentration"]

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(
    registrationName="StreamTracer2", Input=gradient2, SeedType="Line"
)
streamTracer2.Vectors = ["POINTS", "Gradient"]
streamTracer2.MaximumStreamlineLength = 0.02500000037252903

# init the 'Line' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [-9.999999717180685e-10, 0.0135, -0.003]
streamTracer2.SeedType.Point2 = [-9.999999717180685e-10, 0.0135, 0.0]
streamTracer2.SeedType.Resolution = 10

# create a new 'Slice'
toroidalsection_1 = Slice(registrationName="Toroidal section", Input=temperaturexdmf)
toroidalsection_1.SliceType = "Plane"
toroidalsection_1.HyperTreeGridSlicer = "Plane"
toroidalsection_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
toroidalsection_1.SliceType.Origin = [
    -0.005750000011175871,
    0.0010000001639127731,
    1e-09,
]
toroidalsection_1.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
toroidalsection_1.HyperTreeGridSlicer.Origin = [
    -0.005750000011175871,
    0.0010000001639127731,
    0.0012499999720603228,
]

# create a new 'Contour'
contour1 = Contour(registrationName="Contour1", Input=toroidalsection_1)
contour1.ContourBy = ["POINTS", "temperature"]
contour1.Isosurfaces = [
    333.647216796875,
    361.6016969333412,
    389.55617706980735,
    417.51065720627355,
    445.46513734273975,
    473.41961747920595,
    501.3740976156721,
    529.3285777521382,
    557.2830578886045,
    585.2375380250706,
    613.1920181615369,
    641.146498298003,
    669.1009784344692,
    697.0554585709353,
    725.0099387074016,
    752.9644188438677,
    780.918898980334,
    808.8733791168002,
    836.8278592532663,
    864.7823393897326,
    892.7368195261987,
    920.6912996626648,
    948.6457797991311,
    976.6002599355973,
    1004.5547400720634,
    1032.5092202085298,
    1060.4637003449957,
    1088.418180481462,
    1116.3726606179282,
    1144.3271407543943,
]
contour1.PointMergeMethod = "Uniform Binning"

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(
    registrationName="StreamTracer1", Input=gradient1, SeedType="Line"
)
streamTracer1.Vectors = ["POINTS", "Gradient"]
streamTracer1.MaximumStreamlineLength = 0.02500000037252903

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [4.177790859835693e-05, 0.0135, 9.999999712843877e-10]
streamTracer1.SeedType.Point2 = [0.011541777930950098, 0.0135, 9.999999712843877e-10]
streamTracer1.SeedType.Resolution = 30

# create a new 'Slice'
slice1 = Slice(registrationName="Slice1", Input=mesh_cellsxdmf)
slice1.SliceType = "Plane"
slice1.HyperTreeGridSlicer = "Plane"
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-4.463157239375537e-06, 0.001, 0.00175]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [-0.00575, 0.001, 0.00175]

# create a new 'Clip'
clip1 = Clip(registrationName="Clip1", Input=slice1)
clip1.ClipType = "Plane"
clip1.HyperTreeGridClipper = "Plane"
clip1.Scalars = ["CELLS", "f"]
clip1.Value = 7.0
clip1.Invert = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-4.463157239375537e-06, 0.001, 0.00175]
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [-4.463157239375537e-06, 0.001, 0.00175]

# create a new 'Transform'
transform1 = Transform(registrationName="Transform1", Input=clip1)
transform1.Transform = "Transform"

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.001, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'toroidal_view'
# ----------------------------------------------------------------

# show data from contour2
contour2Display = Show(contour2, toroidal_view, "GeometryRepresentation")

# trace defaults for the display properties.
contour2Display.Representation = "Surface"
contour2Display.ColorArrayName = ["POINTS", ""]
contour2Display.LineWidth = 1.5
contour2Display.SelectTCoordArray = "None"
contour2Display.SelectNormalArray = "None"
contour2Display.SelectTangentArray = "None"
contour2Display.OSPRayScaleArray = "temperature"
contour2Display.OSPRayScaleFunction = "PiecewiseFunction"
contour2Display.SelectOrientationVectors = "None"
contour2Display.ScaleFactor = 0.000692738825455308
contour2Display.SelectScaleArray = "temperature"
contour2Display.GlyphType = "Arrow"
contour2Display.GlyphTableIndexArray = "temperature"
contour2Display.GaussianRadius = 3.46369412727654e-05
contour2Display.SetScaleArray = ["POINTS", "temperature"]
contour2Display.ScaleTransferFunction = "PiecewiseFunction"
contour2Display.OpacityArray = ["POINTS", "temperature"]
contour2Display.OpacityTransferFunction = "PiecewiseFunction"
contour2Display.DataAxesGrid = "GridAxesRepresentation"
contour2Display.PolarAxes = "PolarAxesRepresentation"
contour2Display.SelectInputVectors = [None, ""]
contour2Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [
    506.9860441769766,
    0.0,
    0.5,
    0.0,
    1052.035400942595,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [
    506.9860441769766,
    0.0,
    0.5,
    0.0,
    1052.035400942595,
    1.0,
    0.5,
    0.0,
]

# show data from poloidalsection_1
poloidalsection_1Display = Show(
    poloidalsection_1, toroidal_view, "GeometryRepresentation"
)

# get 2D transfer function for 'temperature'
temperatureTF2D = GetTransferFunction2D("temperature")

# get color transfer function/color map for 'temperature'
temperatureLUT = GetColorTransferFunction("temperature")
temperatureLUT.TransferFunction2D = temperatureTF2D
temperatureLUT.RGBPoints = [
    333.5612487792969,
    0.001462,
    0.000466,
    0.013866,
    336.7910594655797,
    0.002267,
    0.00127,
    0.01857,
    340.02004664072376,
    0.003299,
    0.002249,
    0.024239,
    343.24985732700657,
    0.004547,
    0.003392,
    0.030909,
    346.47884450215065,
    0.006006,
    0.004692,
    0.038558,
    349.70865518843345,
    0.007676,
    0.006136,
    0.046836,
    352.93764236357754,
    0.009561,
    0.007713,
    0.055143,
    356.16745304986034,
    0.011663,
    0.009417,
    0.06346,
    359.3972637361432,
    0.013995,
    0.011225,
    0.071862,
    362.62625091128723,
    0.016561,
    0.013136,
    0.080282,
    365.85606159757003,
    0.019373,
    0.015133,
    0.088767,
    369.0850487727141,
    0.022447,
    0.017199,
    0.097327,
    372.3148594589969,
    0.025793,
    0.019331,
    0.10593,
    375.54384663414095,
    0.029432,
    0.021503,
    0.114621,
    378.77365732042375,
    0.033385,
    0.023702,
    0.123397,
    382.0034680067066,
    0.037668,
    0.025921,
    0.132232,
    385.23245518185064,
    0.042253,
    0.028139,
    0.141141,
    388.4622658681335,
    0.046915,
    0.030324,
    0.150164,
    391.6912530432775,
    0.051644,
    0.032474,
    0.159254,
    394.9210637295604,
    0.056449,
    0.034569,
    0.168414,
    398.1500509047044,
    0.06134,
    0.03659,
    0.177642,
    401.3798615909872,
    0.066331,
    0.038504,
    0.186962,
    404.6096722772701,
    0.071429,
    0.040294,
    0.196354,
    407.8386594524141,
    0.076637,
    0.041905,
    0.205799,
    411.06847013869697,
    0.081962,
    0.043328,
    0.215289,
    414.297457313841,
    0.087411,
    0.044556,
    0.224813,
    417.52726800012385,
    0.09299,
    0.045583,
    0.234358,
    420.7562551752679,
    0.098702,
    0.046402,
    0.243904,
    423.9860658615507,
    0.104551,
    0.047008,
    0.25343,
    427.21505303669477,
    0.110536,
    0.047399,
    0.262912,
    430.44486372297763,
    0.116656,
    0.047574,
    0.272321,
    433.67467440926043,
    0.122908,
    0.047536,
    0.281624,
    436.9036615844044,
    0.129285,
    0.047293,
    0.290788,
    440.1334722706873,
    0.135778,
    0.046856,
    0.299776,
    443.36245944583135,
    0.142378,
    0.046242,
    0.308553,
    446.5922701321141,
    0.149073,
    0.045468,
    0.317085,
    449.8212573072582,
    0.15585,
    0.044559,
    0.325338,
    453.0510679935411,
    0.162689,
    0.043554,
    0.333277,
    456.28087867982384,
    0.169575,
    0.042489,
    0.340874,
    459.50986585496787,
    0.176493,
    0.041402,
    0.348111,
    462.7396765412508,
    0.183429,
    0.040329,
    0.354971,
    465.9686637163949,
    0.190367,
    0.039309,
    0.361447,
    469.1984744026776,
    0.197297,
    0.0384,
    0.367535,
    472.42746157782165,
    0.204209,
    0.037632,
    0.373238,
    475.6572722641045,
    0.211095,
    0.03703,
    0.378563,
    478.8870829503873,
    0.217949,
    0.036615,
    0.383522,
    482.11607012553134,
    0.224763,
    0.036405,
    0.388129,
    485.3458808118142,
    0.231538,
    0.036405,
    0.3924,
    488.5748679869583,
    0.238273,
    0.036621,
    0.396353,
    491.8046786732411,
    0.244967,
    0.037055,
    0.400007,
    495.0336658483851,
    0.25162,
    0.037705,
    0.403378,
    498.263476534668,
    0.258234,
    0.038571,
    0.406485,
    501.49328722095083,
    0.26481,
    0.039647,
    0.409345,
    504.7222743960948,
    0.271347,
    0.040922,
    0.411976,
    507.95208508237766,
    0.27785,
    0.042353,
    0.414392,
    511.1810722575217,
    0.284321,
    0.043933,
    0.416608,
    514.4108829438045,
    0.290763,
    0.045644,
    0.418637,
    517.6398701189486,
    0.297178,
    0.04747,
    0.420491,
    520.8696808052314,
    0.303568,
    0.049396,
    0.422182,
    524.0994914915143,
    0.309935,
    0.051407,
    0.423721,
    527.3284786666584,
    0.316282,
    0.05349,
    0.425116,
    530.5582893529411,
    0.32261,
    0.055634,
    0.426377,
    533.7872765280852,
    0.328921,
    0.057827,
    0.427511,
    537.0170872143681,
    0.335217,
    0.06006,
    0.428524,
    540.2460743895119,
    0.3415,
    0.062325,
    0.429425,
    543.4758850757948,
    0.347771,
    0.064616,
    0.430217,
    546.7056957620778,
    0.354032,
    0.066925,
    0.430906,
    549.9346829372219,
    0.360284,
    0.069247,
    0.431497,
    553.1644936235045,
    0.366529,
    0.071579,
    0.431994,
    556.3934807986486,
    0.372768,
    0.073915,
    0.4324,
    559.6232914849313,
    0.379001,
    0.076253,
    0.432719,
    562.8522786600754,
    0.385228,
    0.078591,
    0.432955,
    566.0820893463583,
    0.391453,
    0.080927,
    0.433109,
    569.3119000326412,
    0.397674,
    0.083257,
    0.433183,
    572.5408872077853,
    0.403894,
    0.08558,
    0.433179,
    575.770697894068,
    0.410113,
    0.087896,
    0.433098,
    578.9996850692121,
    0.416331,
    0.090203,
    0.432943,
    582.229495755495,
    0.422549,
    0.092501,
    0.432714,
    585.4584829306389,
    0.428768,
    0.09479,
    0.432412,
    588.6882936169218,
    0.434987,
    0.097069,
    0.432039,
    591.9172807920659,
    0.441207,
    0.099338,
    0.431594,
    595.1470914783487,
    0.447428,
    0.101597,
    0.43108,
    598.3769021646315,
    0.453651,
    0.103848,
    0.430498,
    601.6058893397756,
    0.459875,
    0.106089,
    0.429846,
    604.8357000260584,
    0.4661,
    0.108322,
    0.429125,
    608.0646872012023,
    0.472328,
    0.110547,
    0.428334,
    611.2944978874852,
    0.478558,
    0.112764,
    0.427475,
    614.5234850626293,
    0.484789,
    0.114974,
    0.426548,
    617.7532957489121,
    0.491022,
    0.117179,
    0.425552,
    620.9831064351949,
    0.497257,
    0.119379,
    0.424488,
    624.212093610339,
    0.503493,
    0.121575,
    0.423356,
    627.4419042966218,
    0.50973,
    0.123769,
    0.422156,
    630.6708914717658,
    0.515967,
    0.12596,
    0.420887,
    633.9007021580487,
    0.522206,
    0.12815,
    0.419549,
    637.1296893331928,
    0.528444,
    0.130341,
    0.418142,
    640.3595000194756,
    0.534683,
    0.132534,
    0.416667,
    643.5893107057584,
    0.54092,
    0.134729,
    0.415123,
    646.8182978809025,
    0.547157,
    0.136929,
    0.413511,
    650.0481085671853,
    0.553392,
    0.139134,
    0.411829,
    653.2770957423293,
    0.559624,
    0.141346,
    0.410078,
    656.5069064286122,
    0.565854,
    0.143567,
    0.408258,
    659.7358936037563,
    0.572081,
    0.145797,
    0.406369,
    662.9657042900391,
    0.578304,
    0.148039,
    0.404411,
    666.1955149763219,
    0.584521,
    0.150294,
    0.402385,
    669.424502151466,
    0.590734,
    0.152563,
    0.40029,
    672.6543128377488,
    0.59694,
    0.154848,
    0.398125,
    675.8833000128927,
    0.603139,
    0.157151,
    0.395891,
    679.1131106991756,
    0.60933,
    0.159474,
    0.393589,
    682.3420978743196,
    0.615513,
    0.161817,
    0.391219,
    685.5719085606024,
    0.621685,
    0.164184,
    0.388781,
    688.8017192468853,
    0.627847,
    0.166575,
    0.386276,
    692.0307064220294,
    0.633998,
    0.168992,
    0.383704,
    695.2605171083121,
    0.640135,
    0.171438,
    0.381065,
    698.4895042834562,
    0.64626,
    0.173914,
    0.378359,
    701.719314969739,
    0.652369,
    0.176421,
    0.375586,
    704.9483021448831,
    0.658463,
    0.178962,
    0.372748,
    708.1781128311659,
    0.66454,
    0.181539,
    0.369846,
    711.4079235174488,
    0.670599,
    0.184153,
    0.366879,
    714.6369106925929,
    0.676638,
    0.186807,
    0.363849,
    717.8667213788758,
    0.682656,
    0.189501,
    0.360757,
    721.0957085540197,
    0.688653,
    0.192239,
    0.357603,
    724.3255192403025,
    0.694627,
    0.195021,
    0.354388,
    727.5545064154466,
    0.700576,
    0.197851,
    0.351113,
    730.7843171017294,
    0.7065,
    0.200728,
    0.347777,
    734.0141277880123,
    0.712396,
    0.203656,
    0.344383,
    737.2431149631564,
    0.718264,
    0.206636,
    0.340931,
    740.4729256494393,
    0.724103,
    0.20967,
    0.337424,
    743.7019128245831,
    0.729909,
    0.212759,
    0.333861,
    746.931723510866,
    0.735683,
    0.215906,
    0.330245,
    750.1607106860101,
    0.741423,
    0.219112,
    0.326576,
    753.3905213722928,
    0.747127,
    0.222378,
    0.322856,
    756.6195085474369,
    0.752794,
    0.225706,
    0.319085,
    759.8493192337198,
    0.758422,
    0.229097,
    0.315266,
    763.0791299200025,
    0.76401,
    0.232554,
    0.311399,
    766.3081170951467,
    0.769556,
    0.236077,
    0.307485,
    769.5379277814295,
    0.775059,
    0.239667,
    0.303526,
    772.7669149565735,
    0.780517,
    0.243327,
    0.299523,
    775.9967256428563,
    0.785929,
    0.247056,
    0.295477,
    779.2257128180004,
    0.791293,
    0.250856,
    0.29139,
    782.4555235042832,
    0.796607,
    0.254728,
    0.287264,
    785.685334190566,
    0.801871,
    0.258674,
    0.283099,
    788.9143213657102,
    0.807082,
    0.262692,
    0.278898,
    792.144132051993,
    0.812239,
    0.266786,
    0.274661,
    795.3731192271368,
    0.817341,
    0.270954,
    0.27039,
    798.6029299134198,
    0.822386,
    0.275197,
    0.266085,
    801.8319170885638,
    0.827372,
    0.279517,
    0.26175,
    805.0617277748466,
    0.832299,
    0.283913,
    0.257383,
    808.2915384611296,
    0.837165,
    0.288385,
    0.252988,
    811.5205256362736,
    0.841969,
    0.292933,
    0.248564,
    814.7503363225564,
    0.846709,
    0.297559,
    0.244113,
    817.9793234977003,
    0.851384,
    0.30226,
    0.239636,
    821.2091341839832,
    0.855992,
    0.307038,
    0.235133,
    824.4381213591273,
    0.860533,
    0.311892,
    0.230606,
    827.6679320454101,
    0.865006,
    0.316822,
    0.226055,
    830.897742731693,
    0.869409,
    0.321827,
    0.221482,
    834.126729906837,
    0.873741,
    0.326906,
    0.216886,
    837.3565405931199,
    0.878001,
    0.33206,
    0.212268,
    840.5855277682638,
    0.882188,
    0.337287,
    0.207628,
    843.8153384545467,
    0.886302,
    0.342586,
    0.202968,
    847.0443256296908,
    0.890341,
    0.347957,
    0.198286,
    850.2741363159736,
    0.894305,
    0.353399,
    0.193584,
    853.5039470022565,
    0.898192,
    0.358911,
    0.18886,
    856.7329341774005,
    0.902003,
    0.364492,
    0.184116,
    859.9627448636833,
    0.905735,
    0.37014,
    0.17935,
    863.1917320388274,
    0.90939,
    0.375856,
    0.174563,
    866.4215427251103,
    0.912966,
    0.381636,
    0.169755,
    869.6505299002541,
    0.916462,
    0.387481,
    0.164924,
    872.880340586537,
    0.919879,
    0.393389,
    0.16007,
    876.1101512728198,
    0.923215,
    0.399359,
    0.155193,
    879.3391384479639,
    0.92647,
    0.405389,
    0.150292,
    882.5689491342467,
    0.929644,
    0.411479,
    0.145367,
    885.7979363093908,
    0.932737,
    0.417627,
    0.140417,
    889.0277469956736,
    0.935747,
    0.423831,
    0.13544,
    892.2567341708178,
    0.938675,
    0.430091,
    0.130438,
    895.4865448571005,
    0.941521,
    0.436405,
    0.125409,
    898.7163555433833,
    0.944285,
    0.442772,
    0.120354,
    901.9453427185274,
    0.946965,
    0.449191,
    0.115272,
    905.1751534048101,
    0.949562,
    0.45566,
    0.110164,
    908.4041405799543,
    0.952075,
    0.462178,
    0.105031,
    911.633951266237,
    0.954506,
    0.468744,
    0.099874,
    914.8629384413812,
    0.956852,
    0.475356,
    0.094695,
    918.092749127664,
    0.959114,
    0.482014,
    0.089499,
    921.321736302808,
    0.961293,
    0.488716,
    0.084289,
    924.5515469890909,
    0.963387,
    0.495462,
    0.079073,
    927.7813576753738,
    0.965397,
    0.502249,
    0.073859,
    931.0103448505176,
    0.967322,
    0.509078,
    0.068659,
    934.2401555368006,
    0.969163,
    0.515946,
    0.063488,
    937.4691427119446,
    0.970919,
    0.522853,
    0.058367,
    940.6989533982274,
    0.97259,
    0.529798,
    0.053324,
    943.9279405733714,
    0.974176,
    0.53678,
    0.048392,
    947.1577512596543,
    0.975677,
    0.543798,
    0.043618,
    950.3875619459371,
    0.977092,
    0.55085,
    0.03905,
    953.6165491210811,
    0.978422,
    0.557937,
    0.034931,
    956.846359807364,
    0.979666,
    0.565057,
    0.031409,
    960.0753469825081,
    0.980824,
    0.572209,
    0.028508,
    963.3051576687908,
    0.981895,
    0.579392,
    0.02625,
    966.5341448439349,
    0.982881,
    0.586606,
    0.024661,
    969.7639555302178,
    0.983779,
    0.593849,
    0.02377,
    972.9937662165006,
    0.984591,
    0.601122,
    0.023606,
    976.2227533916446,
    0.985315,
    0.608422,
    0.024202,
    979.4525640779274,
    0.985952,
    0.61575,
    0.025592,
    982.6815512530716,
    0.986502,
    0.623105,
    0.027814,
    985.9113619393544,
    0.986964,
    0.630485,
    0.030908,
    989.1403491144983,
    0.987337,
    0.63789,
    0.034916,
    992.3701598007813,
    0.987622,
    0.64532,
    0.039886,
    995.5999704870641,
    0.987819,
    0.652773,
    0.045581,
    998.828957662208,
    0.987926,
    0.66025,
    0.05175,
    1002.0587683484908,
    0.987945,
    0.667748,
    0.058329,
    1005.287755523635,
    0.987874,
    0.675267,
    0.065257,
    1008.5175662099178,
    0.987714,
    0.682807,
    0.072489,
    1011.7465533850618,
    0.987464,
    0.690366,
    0.07999,
    1014.9763640713446,
    0.987124,
    0.697944,
    0.087731,
    1018.2061747576275,
    0.986694,
    0.70554,
    0.095694,
    1021.4351619327714,
    0.986175,
    0.713153,
    0.103863,
    1024.6649726190544,
    0.985566,
    0.720782,
    0.112229,
    1027.8939597941985,
    0.984865,
    0.728427,
    0.120785,
    1031.1237704804812,
    0.984075,
    0.736087,
    0.129527,
    1034.3527576556253,
    0.983196,
    0.743758,
    0.138453,
    1037.582568341908,
    0.982228,
    0.751442,
    0.147565,
    1040.8123790281911,
    0.981173,
    0.759135,
    0.156863,
    1044.0413662033347,
    0.980032,
    0.766837,
    0.166353,
    1047.271176889618,
    0.978806,
    0.774545,
    0.176037,
    1050.500164064762,
    0.977497,
    0.782258,
    0.185923,
    1053.7299747510447,
    0.976108,
    0.789974,
    0.196018,
    1056.9589619261887,
    0.974638,
    0.797692,
    0.206332,
    1060.188772612472,
    0.973088,
    0.805409,
    0.216877,
    1063.4185832987546,
    0.971468,
    0.813122,
    0.227658,
    1066.6475704738987,
    0.969783,
    0.820825,
    0.238686,
    1069.8773811601811,
    0.968041,
    0.828515,
    0.249972,
    1073.1063683353252,
    0.966243,
    0.836191,
    0.261534,
    1076.3361790216081,
    0.964394,
    0.843848,
    0.273391,
    1079.5651661967522,
    0.962517,
    0.851476,
    0.285546,
    1082.794976883035,
    0.960626,
    0.859069,
    0.29801,
    1086.023964058179,
    0.95872,
    0.866624,
    0.31082,
    1089.253774744462,
    0.956834,
    0.874129,
    0.323974,
    1092.4835854307448,
    0.954997,
    0.881569,
    0.337475,
    1095.712572605889,
    0.953215,
    0.888942,
    0.351369,
    1098.9423832921716,
    0.951546,
    0.896226,
    0.365627,
    1102.1713704673157,
    0.950018,
    0.903409,
    0.380271,
    1105.4011811535984,
    0.948683,
    0.910473,
    0.395289,
    1108.6301683287425,
    0.947594,
    0.917399,
    0.410665,
    1111.8599790150254,
    0.946809,
    0.924168,
    0.426373,
    1115.089789701308,
    0.946392,
    0.930761,
    0.442367,
    1118.3187768764524,
    0.946403,
    0.937159,
    0.458592,
    1121.548587562735,
    0.946903,
    0.943348,
    0.47497,
    1124.7775747378791,
    0.947937,
    0.949318,
    0.491426,
    1128.0073854241618,
    0.949545,
    0.955063,
    0.50786,
    1131.236372599306,
    0.95174,
    0.960587,
    0.524203,
    1134.4661832855888,
    0.954529,
    0.965896,
    0.540361,
    1137.6959939718718,
    0.957896,
    0.971003,
    0.556275,
    1140.9249811470158,
    0.961812,
    0.975924,
    0.571925,
    1144.1547918332985,
    0.966249,
    0.980678,
    0.587206,
    1147.3837790084426,
    0.971162,
    0.985282,
    0.602154,
    1150.6135896947253,
    0.976511,
    0.989753,
    0.61676,
    1153.8425768698694,
    0.982257,
    0.994109,
    0.631017,
    1157.0723875561523,
    0.988362,
    0.998364,
    0.644924,
]
temperatureLUT.NanColor = [0.0, 1.0, 0.0]
temperatureLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
poloidalsection_1Display.Representation = "Surface"
poloidalsection_1Display.ColorArrayName = ["POINTS", "temperature"]
poloidalsection_1Display.LookupTable = temperatureLUT
poloidalsection_1Display.SelectTCoordArray = "None"
poloidalsection_1Display.SelectNormalArray = "None"
poloidalsection_1Display.SelectTangentArray = "None"
poloidalsection_1Display.OSPRayScaleArray = "temperature"
poloidalsection_1Display.OSPRayScaleFunction = "PiecewiseFunction"
poloidalsection_1Display.SelectOrientationVectors = "None"
poloidalsection_1Display.ScaleFactor = 0.002500000037252903
poloidalsection_1Display.SelectScaleArray = "temperature"
poloidalsection_1Display.GlyphType = "Arrow"
poloidalsection_1Display.GlyphTableIndexArray = "temperature"
poloidalsection_1Display.GaussianRadius = 0.00012500000186264516
poloidalsection_1Display.SetScaleArray = ["POINTS", "temperature"]
poloidalsection_1Display.ScaleTransferFunction = "PiecewiseFunction"
poloidalsection_1Display.OpacityArray = ["POINTS", "temperature"]
poloidalsection_1Display.OpacityTransferFunction = "PiecewiseFunction"
poloidalsection_1Display.DataAxesGrid = "GridAxesRepresentation"
poloidalsection_1Display.PolarAxes = "PolarAxesRepresentation"
poloidalsection_1Display.SelectInputVectors = [None, ""]
poloidalsection_1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
poloidalsection_1Display.ScaleTransferFunction.Points = [
    333.56124884246157,
    0.0,
    0.5,
    0.0,
    1052.035400942595,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
poloidalsection_1Display.OpacityTransferFunction.Points = [
    333.56124884246157,
    0.0,
    0.5,
    0.0,
    1052.035400942595,
    1.0,
    0.5,
    0.0,
]

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, toroidal_view, "GeometryRepresentation")

# trace defaults for the display properties.
streamTracer2Display.Representation = "Surface"
streamTracer2Display.ColorArrayName = ["POINTS", ""]
streamTracer2Display.LineWidth = 1.5
streamTracer2Display.SelectTCoordArray = "None"
streamTracer2Display.SelectNormalArray = "None"
streamTracer2Display.SelectTangentArray = "None"
streamTracer2Display.OSPRayScaleArray = "mobile_concentration"
streamTracer2Display.OSPRayScaleFunction = "PiecewiseFunction"
streamTracer2Display.SelectOrientationVectors = "Normals"
streamTracer2Display.ScaleFactor = 0.00037417989224195484
streamTracer2Display.SelectScaleArray = "mobile_concentration"
streamTracer2Display.GlyphType = "Arrow"
streamTracer2Display.GlyphTableIndexArray = "mobile_concentration"
streamTracer2Display.GaussianRadius = 1.870899461209774e-05
streamTracer2Display.SetScaleArray = ["POINTS", "mobile_concentration"]
streamTracer2Display.ScaleTransferFunction = "PiecewiseFunction"
streamTracer2Display.OpacityArray = ["POINTS", "mobile_concentration"]
streamTracer2Display.OpacityTransferFunction = "PiecewiseFunction"
streamTracer2Display.DataAxesGrid = "GridAxesRepresentation"
streamTracer2Display.PolarAxes = "PolarAxesRepresentation"
streamTracer2Display.SelectInputVectors = ["POINTS", "Normals"]
streamTracer2Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [
    3.1379971912340086e18,
    0.0,
    0.5,
    0.0,
    2.764749169409316e21,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [
    3.1379971912340086e18,
    0.0,
    0.5,
    0.0,
    2.764749169409316e21,
    1.0,
    0.5,
    0.0,
]

# show data from reflect2
reflect2Display = Show(reflect2, toroidal_view, "UnstructuredGridRepresentation")

# get 2D transfer function for 'mobile_concentration'
mobile_concentrationTF2D = GetTransferFunction2D("mobile_concentration")
mobile_concentrationTF2D.ScalarRangeInitialized = 1
mobile_concentrationTF2D.Range = [0.0, 5.244316037733545e21, 0.0, 1.0]

# get color transfer function/color map for 'mobile_concentration'
mobile_concentrationLUT = GetColorTransferFunction("mobile_concentration")
mobile_concentrationLUT.AutomaticRescaleRangeMode = "Never"
mobile_concentrationLUT.TransferFunction2D = mobile_concentrationTF2D
mobile_concentrationLUT.RGBPoints = [
    0.0,
    0.267004,
    0.004874,
    0.329415,
    2.0568207499990946e19,
    0.26851,
    0.009605,
    0.335427,
    4.113117068394417e19,
    0.269944,
    0.014625,
    0.341379,
    6.169937818393516e19,
    0.271305,
    0.019942,
    0.347269,
    8.22623413678884e19,
    0.272594,
    0.025563,
    0.353093,
    1.0283054886787935e20,
    0.273809,
    0.031497,
    0.358853,
    1.2339351205183259e20,
    0.274952,
    0.037752,
    0.364543,
    1.4396171955182354e20,
    0.276022,
    0.044167,
    0.370164,
    1.645299270518145e20,
    0.277018,
    0.050344,
    0.375715,
    1.8509289023576772e20,
    0.277941,
    0.056324,
    0.381191,
    2.056610977357587e20,
    0.278791,
    0.062145,
    0.386592,
    2.2622406091971192e20,
    0.279566,
    0.067836,
    0.391917,
    2.4679226841970285e20,
    0.280267,
    0.073417,
    0.397163,
    2.6735523160365613e20,
    0.280894,
    0.078907,
    0.402329,
    2.879234391036471e20,
    0.281446,
    0.08432,
    0.407414,
    3.08491646603638e20,
    0.281924,
    0.089666,
    0.412415,
    3.2905460978759126e20,
    0.282327,
    0.094955,
    0.417331,
    3.4962281728758225e20,
    0.282656,
    0.100196,
    0.42216,
    3.7018578047153544e20,
    0.28291,
    0.105393,
    0.426902,
    3.907539879715265e20,
    0.283091,
    0.110553,
    0.431554,
    4.1131695115547974e20,
    0.283197,
    0.11568,
    0.436115,
    4.318851586554706e20,
    0.283229,
    0.120777,
    0.440584,
    4.5245336615546166e20,
    0.283187,
    0.125848,
    0.44496,
    4.730163293394148e20,
    0.283072,
    0.130895,
    0.449241,
    4.935845368394058e20,
    0.282884,
    0.13592,
    0.453427,
    5.141475000233591e20,
    0.282623,
    0.140926,
    0.457517,
    5.3471570752334994e20,
    0.28229,
    0.145912,
    0.46151,
    5.5527867070730325e20,
    0.281887,
    0.150881,
    0.465405,
    5.758468782072942e20,
    0.281412,
    0.155834,
    0.469201,
    5.964098413912473e20,
    0.280868,
    0.160771,
    0.472899,
    6.169780488912385e20,
    0.280255,
    0.165693,
    0.476498,
    6.375462563912291e20,
    0.279574,
    0.170599,
    0.479997,
    6.581092195751825e20,
    0.278826,
    0.17549,
    0.483397,
    6.786774270751734e20,
    0.278012,
    0.180367,
    0.486697,
    6.992403902591268e20,
    0.277134,
    0.185228,
    0.489898,
    7.198085977591176e20,
    0.276194,
    0.190074,
    0.493001,
    7.403715609430709e20,
    0.275191,
    0.194905,
    0.496005,
    7.609397684430619e20,
    0.274128,
    0.199721,
    0.498911,
    7.81507975943053e20,
    0.273006,
    0.20452,
    0.501721,
    8.020709391270061e20,
    0.271828,
    0.209303,
    0.504434,
    8.22639146626997e20,
    0.270595,
    0.214069,
    0.507052,
    8.432021098109503e20,
    0.269308,
    0.218818,
    0.509577,
    8.637703173109412e20,
    0.267968,
    0.223549,
    0.512008,
    8.843332804948944e20,
    0.26658,
    0.228262,
    0.514349,
    9.049014879948855e20,
    0.265145,
    0.232956,
    0.516599,
    9.254696954948763e20,
    0.263663,
    0.237631,
    0.518762,
    9.460326586788295e20,
    0.262138,
    0.242286,
    0.520837,
    9.666008661788206e20,
    0.260571,
    0.246922,
    0.522828,
    9.871638293627739e20,
    0.258965,
    0.251537,
    0.524736,
    1.0077320368627648e21,
    0.257322,
    0.25613,
    0.526563,
    1.028295000046718e21,
    0.255645,
    0.260703,
    0.528312,
    1.0488632075467091e21,
    0.253935,
    0.265254,
    0.529983,
    1.0694314150466997e21,
    0.252194,
    0.269783,
    0.531579,
    1.0899943782306531e21,
    0.250425,
    0.27429,
    0.533103,
    1.1105625857306442e21,
    0.248629,
    0.278775,
    0.534556,
    1.1311255489145973e21,
    0.246811,
    0.283237,
    0.535941,
    1.1516937564145884e21,
    0.244972,
    0.287675,
    0.53726,
    1.1722567195985416e21,
    0.243113,
    0.292092,
    0.538516,
    1.1928249270985328e21,
    0.241237,
    0.296485,
    0.539709,
    1.2133931345985237e21,
    0.239346,
    0.300855,
    0.540844,
    1.233956097782477e21,
    0.237441,
    0.305202,
    0.541921,
    1.2545243052824674e21,
    0.235526,
    0.309527,
    0.542944,
    1.2750872684664206e21,
    0.233603,
    0.313828,
    0.543914,
    1.2956554759664115e21,
    0.231674,
    0.318106,
    0.544834,
    1.316218439150365e21,
    0.229739,
    0.322361,
    0.545706,
    1.3367866466503562e21,
    0.227802,
    0.326594,
    0.546532,
    1.357354854150347e21,
    0.225863,
    0.330805,
    0.547314,
    1.3779178173343004e21,
    0.223925,
    0.334994,
    0.548053,
    1.398486024834291e21,
    0.221989,
    0.339161,
    0.548752,
    1.4190489880182443e21,
    0.220057,
    0.343307,
    0.549413,
    1.4396171955182352e21,
    0.21813,
    0.347432,
    0.550038,
    1.4601801587021885e21,
    0.21621,
    0.351535,
    0.550627,
    1.4807483662021797e21,
    0.214298,
    0.355619,
    0.551184,
    1.5013165737021706e21,
    0.212395,
    0.359683,
    0.55171,
    1.5218795368861239e21,
    0.210503,
    0.363727,
    0.552206,
    1.5424477443861148e21,
    0.208623,
    0.367752,
    0.552675,
    1.563010707570068e21,
    0.206756,
    0.371758,
    0.553117,
    1.583578915070059e21,
    0.204903,
    0.375746,
    0.553533,
    1.6041418782540122e21,
    0.203063,
    0.379716,
    0.553925,
    1.6247100857540034e21,
    0.201239,
    0.38367,
    0.554294,
    1.645273048937956e21,
    0.19943,
    0.387607,
    0.554642,
    1.6658412564379473e21,
    0.197636,
    0.391528,
    0.554969,
    1.6864094639379382e21,
    0.19586,
    0.395433,
    0.555276,
    1.7069724271218915e21,
    0.1941,
    0.399323,
    0.555565,
    1.7275406346218824e21,
    0.192357,
    0.403199,
    0.555836,
    1.7481035978058356e21,
    0.190631,
    0.407061,
    0.556089,
    1.7686718053058268e21,
    0.188923,
    0.41091,
    0.556326,
    1.7892347684897798e21,
    0.187231,
    0.414746,
    0.556547,
    1.809802975989771e21,
    0.185556,
    0.41857,
    0.556753,
    1.830371183489762e21,
    0.183898,
    0.422383,
    0.556944,
    1.8509341466737152e21,
    0.182256,
    0.426184,
    0.55712,
    1.8715023541737058e21,
    0.180629,
    0.429975,
    0.557282,
    1.892065317357659e21,
    0.179019,
    0.433756,
    0.55743,
    1.91263352485765e21,
    0.177423,
    0.437527,
    0.557565,
    1.9331964880416033e21,
    0.175841,
    0.44129,
    0.557685,
    1.9537646955415945e21,
    0.174274,
    0.445044,
    0.557792,
    1.9743329030415854e21,
    0.172719,
    0.448791,
    0.557885,
    1.9948958662255386e21,
    0.171176,
    0.45253,
    0.557965,
    2.0154640737255296e21,
    0.169646,
    0.456262,
    0.55803,
    2.0360270369094828e21,
    0.168126,
    0.459988,
    0.558082,
    2.0565952444094737e21,
    0.166617,
    0.463708,
    0.558119,
    2.077158207593427e21,
    0.165117,
    0.467423,
    0.558141,
    2.0977264150934182e21,
    0.163625,
    0.471133,
    0.558148,
    2.1182946225934088e21,
    0.162142,
    0.474838,
    0.55814,
    2.138857585777362e21,
    0.160665,
    0.47854,
    0.558115,
    2.1594257932773533e21,
    0.159194,
    0.482237,
    0.558073,
    2.1799887564613062e21,
    0.157729,
    0.485932,
    0.558013,
    2.2005569639612972e21,
    0.15627,
    0.489624,
    0.557936,
    2.2211199271452504e21,
    0.154815,
    0.493313,
    0.55784,
    2.2416881346452416e21,
    0.153364,
    0.497,
    0.557724,
    2.2622563421452323e21,
    0.151918,
    0.500685,
    0.557587,
    2.2828193053291858e21,
    0.150476,
    0.504369,
    0.55743,
    2.3033875128291767e21,
    0.149039,
    0.508051,
    0.55725,
    2.3239504760131302e21,
    0.147607,
    0.511733,
    0.557049,
    2.344518683513121e21,
    0.14618,
    0.515413,
    0.556823,
    2.365081646697074e21,
    0.144759,
    0.519093,
    0.556572,
    2.3856498541970656e21,
    0.143343,
    0.522773,
    0.556295,
    2.406218061697056e21,
    0.141935,
    0.526453,
    0.555991,
    2.4267810248810095e21,
    0.140536,
    0.530132,
    0.555659,
    2.447349232381e21,
    0.139147,
    0.533812,
    0.555298,
    2.467912195564954e21,
    0.13777,
    0.537492,
    0.554906,
    2.4884804030649435e21,
    0.136408,
    0.541173,
    0.554483,
    2.5090433662488973e21,
    0.135066,
    0.544853,
    0.554029,
    2.5296115737488885e21,
    0.133743,
    0.548535,
    0.553541,
    2.550179781248879e21,
    0.132444,
    0.552216,
    0.553018,
    2.5707427444328324e21,
    0.131172,
    0.555899,
    0.552459,
    2.591310951932823e21,
    0.129933,
    0.559582,
    0.551864,
    2.611873915116777e21,
    0.128729,
    0.563265,
    0.551229,
    2.632442122616768e21,
    0.127568,
    0.566949,
    0.550556,
    2.6530050858007213e21,
    0.126453,
    0.570633,
    0.549841,
    2.6735732933007125e21,
    0.125394,
    0.574318,
    0.549086,
    2.694136256484665e21,
    0.124395,
    0.578002,
    0.548287,
    2.7147044639846564e21,
    0.123463,
    0.581687,
    0.547445,
    2.735272671484647e21,
    0.122606,
    0.585371,
    0.546557,
    2.755835634668601e21,
    0.121831,
    0.589055,
    0.545623,
    2.7764038421685915e21,
    0.121148,
    0.592739,
    0.544641,
    2.796966805352544e21,
    0.120565,
    0.596422,
    0.543611,
    2.817535012852536e21,
    0.120092,
    0.600104,
    0.54253,
    2.8380979760364886e21,
    0.119738,
    0.603785,
    0.5414,
    2.85866618353648e21,
    0.119512,
    0.607464,
    0.540218,
    2.8792343910364705e21,
    0.119423,
    0.611141,
    0.538982,
    2.8997973542204243e21,
    0.119483,
    0.614817,
    0.537692,
    2.920365561720415e21,
    0.119699,
    0.61849,
    0.536347,
    2.940928524904368e21,
    0.120081,
    0.622161,
    0.534946,
    2.9614967324043594e21,
    0.120638,
    0.625828,
    0.533488,
    2.9820596955883126e21,
    0.12138,
    0.629492,
    0.531973,
    3.0026279030883033e21,
    0.122312,
    0.633153,
    0.530398,
    3.023196110588294e21,
    0.123444,
    0.636809,
    0.528763,
    3.0437590737722477e21,
    0.12478,
    0.640461,
    0.527068,
    3.0643272812722384e21,
    0.126326,
    0.644107,
    0.525311,
    3.0848902444561916e21,
    0.128087,
    0.647749,
    0.523491,
    3.105458451956183e21,
    0.130067,
    0.651384,
    0.521608,
    3.126021415140136e21,
    0.132268,
    0.655014,
    0.519661,
    3.1465896226401267e21,
    0.134692,
    0.658636,
    0.517649,
    3.167157830140118e21,
    0.137339,
    0.662252,
    0.515571,
    3.187720793324071e21,
    0.14021,
    0.665859,
    0.513427,
    3.2082890008240623e21,
    0.143303,
    0.669459,
    0.511215,
    3.228851964008015e21,
    0.146616,
    0.67305,
    0.508936,
    3.249420171508007e21,
    0.150148,
    0.676631,
    0.506589,
    3.2699831346919595e21,
    0.153894,
    0.680203,
    0.504172,
    3.29055134219195e21,
    0.157851,
    0.683765,
    0.501686,
    3.3111195496919414e21,
    0.162016,
    0.687316,
    0.499129,
    3.3316825128758946e21,
    0.166383,
    0.690856,
    0.496502,
    3.352250720375886e21,
    0.170948,
    0.694384,
    0.493803,
    3.3728136835598385e21,
    0.175707,
    0.6979,
    0.491033,
    3.39338189105983e21,
    0.180653,
    0.701402,
    0.488189,
    3.413944854243783e21,
    0.185783,
    0.704891,
    0.485273,
    3.434513061743774e21,
    0.19109,
    0.708366,
    0.482284,
    3.455081269243765e21,
    0.196571,
    0.711827,
    0.479221,
    3.4756442324277186e21,
    0.202219,
    0.715272,
    0.476084,
    3.496212439927709e21,
    0.20803,
    0.718701,
    0.472873,
    3.516775403111662e21,
    0.214,
    0.722114,
    0.469588,
    3.5373436106116537e21,
    0.220124,
    0.725509,
    0.466226,
    3.5579065737956064e21,
    0.226397,
    0.728888,
    0.462789,
    3.5784747812955976e21,
    0.232815,
    0.732247,
    0.459277,
    3.599042988795588e21,
    0.239374,
    0.735588,
    0.455688,
    3.619605951979542e21,
    0.24607,
    0.73891,
    0.452024,
    3.6401741594795327e21,
    0.252899,
    0.742211,
    0.448284,
    3.660737122663486e21,
    0.259857,
    0.745492,
    0.444467,
    3.6813053301634766e21,
    0.266941,
    0.748751,
    0.440573,
    3.7018682933474304e21,
    0.274149,
    0.751988,
    0.436601,
    3.722436500847421e21,
    0.281477,
    0.755203,
    0.432552,
    3.742999464031375e21,
    0.288921,
    0.758394,
    0.428426,
    3.7635676715313655e21,
    0.296479,
    0.761561,
    0.424223,
    3.784135879031356e21,
    0.304148,
    0.764704,
    0.419943,
    3.8046988422153094e21,
    0.311925,
    0.767822,
    0.415586,
    3.8252670497153e21,
    0.319809,
    0.770914,
    0.411152,
    3.845830012899254e21,
    0.327796,
    0.77398,
    0.40664,
    3.8663982203992445e21,
    0.335885,
    0.777018,
    0.402049,
    3.8869611835831977e21,
    0.344074,
    0.780029,
    0.397381,
    3.907529391083189e21,
    0.35236,
    0.783011,
    0.392636,
    3.92809759858318e21,
    0.360741,
    0.785964,
    0.387814,
    3.948660561767133e21,
    0.369214,
    0.788888,
    0.382914,
    3.9692287692671235e21,
    0.377779,
    0.791781,
    0.377939,
    3.989791732451077e21,
    0.386433,
    0.794644,
    0.372886,
    4.010359939951068e21,
    0.395174,
    0.797475,
    0.367757,
    4.030922903135021e21,
    0.404001,
    0.800275,
    0.362552,
    4.0514911106350124e21,
    0.412913,
    0.803041,
    0.357269,
    4.0720593181350035e21,
    0.421908,
    0.805774,
    0.35191,
    4.0926222813189563e21,
    0.430983,
    0.808473,
    0.346476,
    4.1131904888189475e21,
    0.440137,
    0.811138,
    0.340967,
    4.1337534520029007e21,
    0.449368,
    0.813768,
    0.335384,
    4.154321659502892e21,
    0.458674,
    0.816363,
    0.329727,
    4.1748846226868446e21,
    0.468053,
    0.818921,
    0.323998,
    4.1954528301868363e21,
    0.477504,
    0.821444,
    0.318195,
    4.2160210376868275e21,
    0.487026,
    0.823929,
    0.312321,
    4.23658400087078e21,
    0.496615,
    0.826376,
    0.306377,
    4.2571522083707704e21,
    0.506271,
    0.828786,
    0.300362,
    4.277715171554724e21,
    0.515992,
    0.831158,
    0.294279,
    4.2982833790547153e21,
    0.525776,
    0.833491,
    0.288127,
    4.318846342238668e21,
    0.535621,
    0.835785,
    0.281908,
    4.339414549738659e21,
    0.545524,
    0.838039,
    0.275626,
    4.3599827572386504e21,
    0.555484,
    0.840254,
    0.269281,
    4.380545720422603e21,
    0.565498,
    0.84243,
    0.262877,
    4.4011139279225943e21,
    0.575563,
    0.844566,
    0.256415,
    4.421676891106548e21,
    0.585678,
    0.846661,
    0.249897,
    4.4422450986065393e21,
    0.595839,
    0.848717,
    0.243329,
    4.4628080617904926e21,
    0.606045,
    0.850733,
    0.236712,
    4.483376269290483e21,
    0.616293,
    0.852709,
    0.230052,
    4.503944476790474e21,
    0.626579,
    0.854645,
    0.223353,
    4.5245074399744266e21,
    0.636902,
    0.856542,
    0.21662,
    4.5450756474744183e21,
    0.647257,
    0.8584,
    0.209861,
    4.5656386106583716e21,
    0.657642,
    0.860219,
    0.203082,
    4.586206818158362e21,
    0.668054,
    0.861999,
    0.196293,
    4.606769781342315e21,
    0.678489,
    0.863742,
    0.189503,
    4.6273379888423067e21,
    0.688944,
    0.865448,
    0.182725,
    4.6479061963422963e21,
    0.699415,
    0.867117,
    0.175971,
    4.668469159526252e21,
    0.709898,
    0.868751,
    0.169257,
    4.689037367026242e21,
    0.720391,
    0.87035,
    0.162603,
    4.7096003302101945e21,
    0.730889,
    0.871916,
    0.156029,
    4.730168537710186e21,
    0.741388,
    0.873449,
    0.149561,
    4.750731500894138e21,
    0.751884,
    0.874951,
    0.143228,
    4.771299708394131e21,
    0.762373,
    0.876424,
    0.137064,
    4.791862671578085e21,
    0.772852,
    0.877868,
    0.131109,
    4.812430879078073e21,
    0.783315,
    0.879285,
    0.125405,
    4.832999086578066e21,
    0.79376,
    0.880678,
    0.120005,
    4.853562049762019e21,
    0.804182,
    0.882046,
    0.114965,
    4.874130257262008e21,
    0.814576,
    0.883393,
    0.110347,
    4.894693220445963e21,
    0.82494,
    0.88472,
    0.106217,
    4.915261427945953e21,
    0.83527,
    0.886029,
    0.102646,
    4.935824391129908e21,
    0.845561,
    0.887322,
    0.099702,
    4.956392598629898e21,
    0.85581,
    0.888601,
    0.097452,
    4.976960806129887e21,
    0.866013,
    0.889868,
    0.095953,
    4.997523769313842e21,
    0.876168,
    0.891125,
    0.09525,
    5.018091976813833e21,
    0.886271,
    0.892374,
    0.095374,
    5.038654939997788e21,
    0.89632,
    0.893616,
    0.096335,
    5.059223147497777e21,
    0.906311,
    0.894855,
    0.098125,
    5.07978611068173e21,
    0.916242,
    0.896091,
    0.100717,
    5.100354318181723e21,
    0.926106,
    0.89733,
    0.104071,
    5.120922525681711e21,
    0.935904,
    0.89857,
    0.108131,
    5.141485488865665e21,
    0.945636,
    0.899815,
    0.112838,
    5.162053696365658e21,
    0.9553,
    0.901065,
    0.118128,
    5.182616659549609e21,
    0.964894,
    0.902323,
    0.123941,
    5.203184867049601e21,
    0.974417,
    0.90359,
    0.130215,
    5.223747830233554e21,
    0.983868,
    0.904867,
    0.136897,
    5.244316037733545e21,
    0.993248,
    0.906157,
    0.143936,
]
mobile_concentrationLUT.NanColor = [1.0, 0.0, 0.0]
mobile_concentrationLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'mobile_concentration'
mobile_concentrationPWF = GetOpacityTransferFunction("mobile_concentration")
mobile_concentrationPWF.Points = [
    0.0,
    0.0,
    0.5,
    0.0,
    5.244316037733545e21,
    1.0,
    0.5,
    0.0,
]
mobile_concentrationPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
reflect2Display.Representation = "Surface"
reflect2Display.ColorArrayName = ["POINTS", "mobile_concentration"]
reflect2Display.LookupTable = mobile_concentrationLUT
reflect2Display.SelectTCoordArray = "None"
reflect2Display.SelectNormalArray = "None"
reflect2Display.SelectTangentArray = "None"
reflect2Display.OSPRayScaleArray = "mobile_concentration"
reflect2Display.OSPRayScaleFunction = "PiecewiseFunction"
reflect2Display.SelectOrientationVectors = "None"
reflect2Display.ScaleFactor = 0.002500000037252903
reflect2Display.SelectScaleArray = "mobile_concentration"
reflect2Display.GlyphType = "Arrow"
reflect2Display.GlyphTableIndexArray = "mobile_concentration"
reflect2Display.GaussianRadius = 0.00012500000186264516
reflect2Display.SetScaleArray = ["POINTS", "mobile_concentration"]
reflect2Display.ScaleTransferFunction = "PiecewiseFunction"
reflect2Display.OpacityArray = ["POINTS", "mobile_concentration"]
reflect2Display.OpacityTransferFunction = "PiecewiseFunction"
reflect2Display.DataAxesGrid = "GridAxesRepresentation"
reflect2Display.PolarAxes = "PolarAxesRepresentation"
reflect2Display.ScalarOpacityFunction = mobile_concentrationPWF
reflect2Display.ScalarOpacityUnitDistance = 0.0017554132813757091
reflect2Display.OpacityArrayName = ["POINTS", "mobile_concentration"]
reflect2Display.SelectInputVectors = [None, ""]
reflect2Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
reflect2Display.ScaleTransferFunction.Points = [
    -8.381392038351567e19,
    0.0,
    0.5,
    0.0,
    2.7725800279755063e21,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
reflect2Display.OpacityTransferFunction.Points = [
    -8.381392038351567e19,
    0.0,
    0.5,
    0.0,
    2.7725800279755063e21,
    1.0,
    0.5,
    0.0,
]

# ----------------------------------------------------------------
# setup the visualization in view 'poloidal_view'
# ----------------------------------------------------------------

# show data from toroidalsection_1
toroidalsection_1Display = Show(
    toroidalsection_1, poloidal_view, "GeometryRepresentation"
)

# trace defaults for the display properties.
toroidalsection_1Display.Representation = "Surface"
toroidalsection_1Display.ColorArrayName = ["POINTS", "temperature"]
toroidalsection_1Display.LookupTable = temperatureLUT
toroidalsection_1Display.SelectTCoordArray = "None"
toroidalsection_1Display.SelectNormalArray = "None"
toroidalsection_1Display.SelectTangentArray = "None"
toroidalsection_1Display.OSPRayScaleArray = "temperature"
toroidalsection_1Display.OSPRayScaleFunction = "PiecewiseFunction"
toroidalsection_1Display.SelectOrientationVectors = "None"
toroidalsection_1Display.ScaleFactor = 0.002500000037252903
toroidalsection_1Display.SelectScaleArray = "temperature"
toroidalsection_1Display.GlyphType = "Arrow"
toroidalsection_1Display.GlyphTableIndexArray = "temperature"
toroidalsection_1Display.GaussianRadius = 0.00012500000186264516
toroidalsection_1Display.SetScaleArray = ["POINTS", "temperature"]
toroidalsection_1Display.ScaleTransferFunction = "PiecewiseFunction"
toroidalsection_1Display.OpacityArray = ["POINTS", "temperature"]
toroidalsection_1Display.OpacityTransferFunction = "PiecewiseFunction"
toroidalsection_1Display.DataAxesGrid = "GridAxesRepresentation"
toroidalsection_1Display.PolarAxes = "PolarAxesRepresentation"
toroidalsection_1Display.SelectInputVectors = [None, ""]
toroidalsection_1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
toroidalsection_1Display.ScaleTransferFunction.Points = [
    333.647216796875,
    0.0,
    0.5,
    0.0,
    1144.3271407543943,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
toroidalsection_1Display.OpacityTransferFunction.Points = [
    333.647216796875,
    0.0,
    0.5,
    0.0,
    1144.3271407543943,
    1.0,
    0.5,
    0.0,
]

# show data from contour1
contour1Display = Show(contour1, poloidal_view, "GeometryRepresentation")

# trace defaults for the display properties.
contour1Display.Representation = "Surface"
contour1Display.ColorArrayName = ["POINTS", ""]
contour1Display.LineWidth = 1.5
contour1Display.SelectTCoordArray = "None"
contour1Display.SelectNormalArray = "None"
contour1Display.SelectTangentArray = "None"
contour1Display.OSPRayScaleArray = "temperature"
contour1Display.OSPRayScaleFunction = "PiecewiseFunction"
contour1Display.SelectOrientationVectors = "None"
contour1Display.ScaleFactor = 0.0012617368949577213
contour1Display.SelectScaleArray = "temperature"
contour1Display.GlyphType = "Arrow"
contour1Display.GlyphTableIndexArray = "temperature"
contour1Display.GaussianRadius = 6.308684474788606e-05
contour1Display.SetScaleArray = ["POINTS", "temperature"]
contour1Display.ScaleTransferFunction = "PiecewiseFunction"
contour1Display.OpacityArray = ["POINTS", "temperature"]
contour1Display.OpacityTransferFunction = "PiecewiseFunction"
contour1Display.DataAxesGrid = "GridAxesRepresentation"
contour1Display.PolarAxes = "PolarAxesRepresentation"
contour1Display.SelectInputVectors = [None, ""]
contour1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [
    423.722763903266,
    0.0,
    0.5,
    0.0,
    1144.3271407543943,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [
    423.722763903266,
    0.0,
    0.5,
    0.0,
    1144.3271407543943,
    1.0,
    0.5,
    0.0,
]

# show data from reflect1
reflect1Display = Show(reflect1, poloidal_view, "UnstructuredGridRepresentation")

# trace defaults for the display properties.
reflect1Display.Representation = "Surface"
reflect1Display.ColorArrayName = ["POINTS", "mobile_concentration"]
reflect1Display.LookupTable = mobile_concentrationLUT
reflect1Display.SelectTCoordArray = "None"
reflect1Display.SelectNormalArray = "None"
reflect1Display.SelectTangentArray = "None"
reflect1Display.OSPRayScaleArray = "mobile_concentration"
reflect1Display.OSPRayScaleFunction = "PiecewiseFunction"
reflect1Display.SelectOrientationVectors = "None"
reflect1Display.ScaleFactor = 0.002500000037252903
reflect1Display.SelectScaleArray = "mobile_concentration"
reflect1Display.GlyphType = "Arrow"
reflect1Display.GlyphTableIndexArray = "mobile_concentration"
reflect1Display.GaussianRadius = 0.00012500000186264516
reflect1Display.SetScaleArray = ["POINTS", "mobile_concentration"]
reflect1Display.ScaleTransferFunction = "PiecewiseFunction"
reflect1Display.OpacityArray = ["POINTS", "mobile_concentration"]
reflect1Display.OpacityTransferFunction = "PiecewiseFunction"
reflect1Display.DataAxesGrid = "GridAxesRepresentation"
reflect1Display.PolarAxes = "PolarAxesRepresentation"
reflect1Display.ScalarOpacityFunction = mobile_concentrationPWF
reflect1Display.ScalarOpacityUnitDistance = 0.0009823918233765564
reflect1Display.OpacityArrayName = ["POINTS", "mobile_concentration"]
reflect1Display.SelectInputVectors = [None, ""]
reflect1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
reflect1Display.ScaleTransferFunction.Points = [
    -3.0256512294605857e19,
    0.0,
    0.5,
    0.0,
    2.773391519655764e21,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
reflect1Display.OpacityTransferFunction.Points = [
    -3.0256512294605857e19,
    0.0,
    0.5,
    0.0,
    2.773391519655764e21,
    1.0,
    0.5,
    0.0,
]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, poloidal_view, "GeometryRepresentation")

# trace defaults for the display properties.
streamTracer1Display.Representation = "Surface"
streamTracer1Display.ColorArrayName = ["POINTS", ""]
streamTracer1Display.LineWidth = 1.5
streamTracer1Display.SelectTCoordArray = "None"
streamTracer1Display.SelectNormalArray = "None"
streamTracer1Display.SelectTangentArray = "None"
streamTracer1Display.OSPRayScaleArray = "mobile_concentration"
streamTracer1Display.OSPRayScaleFunction = "PiecewiseFunction"
streamTracer1Display.SelectOrientationVectors = "Normals"
streamTracer1Display.ScaleFactor = 0.0016392120392993094
streamTracer1Display.SelectScaleArray = "mobile_concentration"
streamTracer1Display.GlyphType = "Arrow"
streamTracer1Display.GlyphTableIndexArray = "mobile_concentration"
streamTracer1Display.GaussianRadius = 8.196060196496546e-05
streamTracer1Display.SetScaleArray = ["POINTS", "mobile_concentration"]
streamTracer1Display.ScaleTransferFunction = "PiecewiseFunction"
streamTracer1Display.OpacityArray = ["POINTS", "mobile_concentration"]
streamTracer1Display.OpacityTransferFunction = "PiecewiseFunction"
streamTracer1Display.DataAxesGrid = "GridAxesRepresentation"
streamTracer1Display.PolarAxes = "PolarAxesRepresentation"
streamTracer1Display.SelectInputVectors = ["POINTS", "Normals"]
streamTracer1Display.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [
    -1.1030529057060119e19,
    0.0,
    0.5,
    0.0,
    2.7646304107046806e21,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [
    -1.1030529057060119e19,
    0.0,
    0.5,
    0.0,
    2.7646304107046806e21,
    1.0,
    0.5,
    0.0,
]

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view poloidal_view
temperatureLUTColorBar = GetScalarBar(temperatureLUT, poloidal_view)
temperatureLUTColorBar.WindowLocation = "Any Location"
temperatureLUTColorBar.Position = [0.21051854633499967, 0.33388349514563104]
temperatureLUTColorBar.Title = "Temperature (K)"
temperatureLUTColorBar.ComponentTitle = ""
temperatureLUTColorBar.TitleJustification = "Right"
temperatureLUTColorBar.HorizontalTitle = 1
temperatureLUTColorBar.ScalarBarLength = 0.33000000000000046
temperatureLUTColorBar.AutomaticLabelFormat = 0
temperatureLUTColorBar.LabelFormat = "%-6.f"
temperatureLUTColorBar.UseCustomLabels = 1
temperatureLUTColorBar.CustomLabels = [
    400.0,
    500.0,
    600.0,
    700.0,
    800.0,
    900.0,
    1000.0,
    1100.0,
]
temperatureLUTColorBar.RangeLabelFormat = "%-6.0f"
temperatureLUTColorBar.DataRangeLabelFormat = "%-#6.1f"

# set color bar visibility
temperatureLUTColorBar.Visibility = 1

# get color legend/bar for mobile_concentrationLUT in view poloidal_view
mobile_concentrationLUTColorBar = GetScalarBar(mobile_concentrationLUT, poloidal_view)
mobile_concentrationLUTColorBar.WindowLocation = "Any Location"
mobile_concentrationLUTColorBar.Position = [0.7103025630943388, 0.3164077669902913]
mobile_concentrationLUTColorBar.Title = "Mobile concentration (H/m$^3$)"
mobile_concentrationLUTColorBar.ComponentTitle = ""
mobile_concentrationLUTColorBar.TitleJustification = "Left"
mobile_concentrationLUTColorBar.HorizontalTitle = 1
mobile_concentrationLUTColorBar.ScalarBarLength = 0.3299999999999996
mobile_concentrationLUTColorBar.AutomaticLabelFormat = 0
mobile_concentrationLUTColorBar.LabelFormat = "%-#6.1e"

# set color bar visibility
mobile_concentrationLUTColorBar.Visibility = 1

# show color legend
toroidalsection_1Display.SetScalarBarVisibility(poloidal_view, True)

# show color legend
reflect1Display.SetScalarBarVisibility(poloidal_view, True)

# ----------------------------------------------------------------
# setup the visualization in view 'retention_3d_view'
# ----------------------------------------------------------------

# show data from retentionxdmf
retentionxdmfDisplay = Show(
    retentionxdmf, retention_3d_view, "UnstructuredGridRepresentation"
)

# get 2D transfer function for 'retention'
retentionTF2D = GetTransferFunction2D("retention")
retentionTF2D.ScalarRangeInitialized = 1
retentionTF2D.Range = [0.0, 1.1536987133125404e22, 0.0, 1.0]

# get color transfer function/color map for 'retention'
retentionLUT = GetColorTransferFunction("retention")
retentionLUT.AutomaticRescaleRangeMode = "Never"
retentionLUT.TransferFunction2D = retentionTF2D
retentionLUT.RGBPoints = [
    0.0,
    0.267004,
    0.004874,
    0.329415,
    4.5248063536117916e19,
    0.26851,
    0.009605,
    0.335427,
    9.04845900851026e19,
    0.269944,
    0.014625,
    0.341379,
    1.357326536212203e20,
    0.271305,
    0.019942,
    0.347269,
    1.809691801702052e20,
    0.272594,
    0.025563,
    0.353093,
    2.2621724370632288e20,
    0.273809,
    0.031497,
    0.358853,
    2.7145377025530757e20,
    0.274952,
    0.037752,
    0.364543,
    3.167018337914255e20,
    0.276022,
    0.044167,
    0.370164,
    3.619498973275434e20,
    0.277018,
    0.050344,
    0.375715,
    4.071864238765281e20,
    0.277941,
    0.056324,
    0.381191,
    4.5243448741264576e20,
    0.278791,
    0.062145,
    0.386592,
    4.976710139616307e20,
    0.279566,
    0.067836,
    0.391917,
    5.429190774977484e20,
    0.280267,
    0.073417,
    0.397163,
    5.881556040467331e20,
    0.280894,
    0.078907,
    0.402329,
    6.33403667582851e20,
    0.281446,
    0.08432,
    0.407414,
    6.786517311189689e20,
    0.281924,
    0.089666,
    0.412415,
    7.238882576679533e20,
    0.282327,
    0.094955,
    0.417331,
    7.691363212040712e20,
    0.282656,
    0.100196,
    0.42216,
    8.143728477530562e20,
    0.28291,
    0.105393,
    0.426902,
    8.59620911289174e20,
    0.283091,
    0.110553,
    0.431554,
    9.048574378381586e20,
    0.283197,
    0.11568,
    0.436115,
    9.501055013742764e20,
    0.283229,
    0.120777,
    0.440584,
    9.953535649103943e20,
    0.283187,
    0.125848,
    0.44496,
    1.0405900914593791e21,
    0.283072,
    0.130895,
    0.449241,
    1.0858381549954968e21,
    0.282884,
    0.13592,
    0.453427,
    1.1310746815444814e21,
    0.282623,
    0.140926,
    0.457517,
    1.1763227450805993e21,
    0.28229,
    0.145912,
    0.46151,
    1.221559271629584e21,
    0.281887,
    0.150881,
    0.465405,
    1.266807335165702e21,
    0.281412,
    0.155834,
    0.469201,
    1.3120438617146867e21,
    0.280868,
    0.160771,
    0.472899,
    1.3572919252508045e21,
    0.280255,
    0.165693,
    0.476498,
    1.402539988786922e21,
    0.279574,
    0.170599,
    0.479997,
    1.447776515335907e21,
    0.278826,
    0.17549,
    0.483397,
    1.4930245788720248e21,
    0.278012,
    0.180367,
    0.486697,
    1.5382611054210096e21,
    0.277134,
    0.185228,
    0.489898,
    1.5835091689571271e21,
    0.276194,
    0.190074,
    0.493001,
    1.628745695506112e21,
    0.275191,
    0.194905,
    0.496005,
    1.67399375904223e21,
    0.274128,
    0.199721,
    0.498911,
    1.7192418225783479e21,
    0.273006,
    0.20452,
    0.501721,
    1.7644783491273324e21,
    0.271828,
    0.209303,
    0.504434,
    1.8097264126634502e21,
    0.270595,
    0.214069,
    0.507052,
    1.854962939212435e21,
    0.269308,
    0.218818,
    0.509577,
    1.900211002748553e21,
    0.267968,
    0.223549,
    0.512008,
    1.9454475292975377e21,
    0.26658,
    0.228262,
    0.514349,
    1.9906955928336552e21,
    0.265145,
    0.232956,
    0.516599,
    2.035943656369773e21,
    0.263663,
    0.237631,
    0.518762,
    2.0811801829187581e21,
    0.262138,
    0.242286,
    0.520837,
    2.1264282464548762e21,
    0.260571,
    0.246922,
    0.522828,
    2.1716647730038608e21,
    0.258965,
    0.251537,
    0.524736,
    2.2169128365399784e21,
    0.257322,
    0.25613,
    0.526563,
    2.262149363088963e21,
    0.255645,
    0.260703,
    0.528312,
    2.3073974266250807e21,
    0.253935,
    0.265254,
    0.529983,
    2.3526454901611986e21,
    0.252194,
    0.269783,
    0.531579,
    2.3978820167101836e21,
    0.250425,
    0.27429,
    0.533103,
    2.4431300802463017e21,
    0.248629,
    0.278775,
    0.534556,
    2.4883666067952857e21,
    0.246811,
    0.283237,
    0.535941,
    2.533614670331404e21,
    0.244972,
    0.287675,
    0.53726,
    2.578851196880389e21,
    0.243113,
    0.292092,
    0.538516,
    2.624099260416506e21,
    0.241237,
    0.296485,
    0.539709,
    2.669347323952624e21,
    0.239346,
    0.300855,
    0.540844,
    2.714583850501609e21,
    0.237441,
    0.305202,
    0.541921,
    2.7598319140377267e21,
    0.235526,
    0.309527,
    0.542944,
    2.805068440586711e21,
    0.233603,
    0.313828,
    0.543914,
    2.850316504122829e21,
    0.231674,
    0.318106,
    0.544834,
    2.895553030671814e21,
    0.229739,
    0.322361,
    0.545706,
    2.940801094207932e21,
    0.227802,
    0.326594,
    0.546532,
    2.9860491577440495e21,
    0.225863,
    0.330805,
    0.547314,
    3.0312856842930346e21,
    0.223925,
    0.334994,
    0.548053,
    3.076533747829152e21,
    0.221989,
    0.339161,
    0.548752,
    3.1217702743781367e21,
    0.220057,
    0.343307,
    0.549413,
    3.1670183379142543e21,
    0.21813,
    0.347432,
    0.550038,
    3.2122548644632393e21,
    0.21621,
    0.351535,
    0.550627,
    3.2575029279993574e21,
    0.214298,
    0.355619,
    0.551184,
    3.302750991535475e21,
    0.212395,
    0.359683,
    0.55171,
    3.34798751808446e21,
    0.210503,
    0.363727,
    0.552206,
    3.3932355816205776e21,
    0.208623,
    0.367752,
    0.552675,
    3.438472108169562e21,
    0.206756,
    0.371758,
    0.553117,
    3.48372017170568e21,
    0.204903,
    0.375746,
    0.553533,
    3.528956698254665e21,
    0.203063,
    0.379716,
    0.553925,
    3.574204761790783e21,
    0.201239,
    0.38367,
    0.554294,
    3.6194412883397674e21,
    0.19943,
    0.387607,
    0.554642,
    3.6646893518758855e21,
    0.197636,
    0.391528,
    0.554969,
    3.709937415412003e21,
    0.19586,
    0.395433,
    0.555276,
    3.7551739419609876e21,
    0.1941,
    0.399323,
    0.555565,
    3.800422005497106e21,
    0.192357,
    0.403199,
    0.555836,
    3.8456585320460903e21,
    0.190631,
    0.407061,
    0.556089,
    3.8909065955822084e21,
    0.188923,
    0.41091,
    0.556326,
    3.936143122131193e21,
    0.187231,
    0.414746,
    0.556547,
    3.9813911856673105e21,
    0.185556,
    0.41857,
    0.556753,
    4.0266392492034286e21,
    0.183898,
    0.422383,
    0.556944,
    4.0718757757524136e21,
    0.182256,
    0.426184,
    0.55712,
    4.117123839288531e21,
    0.180629,
    0.429975,
    0.557282,
    4.1623603658375163e21,
    0.179019,
    0.433756,
    0.55743,
    4.2076084293736333e21,
    0.177423,
    0.437527,
    0.557565,
    4.2528449559226184e21,
    0.175841,
    0.44129,
    0.557685,
    4.298093019458736e21,
    0.174274,
    0.445044,
    0.557792,
    4.343341082994854e21,
    0.172719,
    0.448791,
    0.557885,
    4.388577609543839e21,
    0.171176,
    0.45253,
    0.557965,
    4.4338256730799567e21,
    0.169646,
    0.456262,
    0.55803,
    4.479062199628942e21,
    0.168126,
    0.459988,
    0.558082,
    4.524310263165059e21,
    0.166617,
    0.463708,
    0.558119,
    4.569546789714044e21,
    0.165117,
    0.467423,
    0.558141,
    4.6147948532501614e21,
    0.163625,
    0.471133,
    0.558148,
    4.6600429167862795e21,
    0.162142,
    0.474838,
    0.55814,
    4.7052794433352646e21,
    0.160665,
    0.47854,
    0.558115,
    4.750527506871382e21,
    0.159194,
    0.482237,
    0.558073,
    4.795764033420367e21,
    0.157729,
    0.485932,
    0.558013,
    4.841012096956484e21,
    0.15627,
    0.489624,
    0.557936,
    4.886248623505468e21,
    0.154815,
    0.493313,
    0.55784,
    4.931496687041588e21,
    0.153364,
    0.497,
    0.557724,
    4.976744750577705e21,
    0.151918,
    0.500685,
    0.557587,
    5.02198127712669e21,
    0.150476,
    0.504369,
    0.55743,
    5.067229340662808e21,
    0.149039,
    0.508051,
    0.55725,
    5.112465867211793e21,
    0.147607,
    0.511733,
    0.557049,
    5.15771393074791e21,
    0.14618,
    0.515413,
    0.556823,
    5.202950457296895e21,
    0.144759,
    0.519093,
    0.556572,
    5.248198520833012e21,
    0.143343,
    0.522773,
    0.556295,
    5.293446584369131e21,
    0.141935,
    0.526453,
    0.555991,
    5.338683110918118e21,
    0.140536,
    0.530132,
    0.555659,
    5.383931174454233e21,
    0.139147,
    0.533812,
    0.555298,
    5.429167701003218e21,
    0.13777,
    0.537492,
    0.554906,
    5.474415764539335e21,
    0.136408,
    0.541173,
    0.554483,
    5.519652291088319e21,
    0.135066,
    0.544853,
    0.554029,
    5.564900354624436e21,
    0.133743,
    0.548535,
    0.553541,
    5.610148418160556e21,
    0.132444,
    0.552216,
    0.553018,
    5.655384944709539e21,
    0.131172,
    0.555899,
    0.552459,
    5.700633008245658e21,
    0.129933,
    0.559582,
    0.551864,
    5.745869534794643e21,
    0.128729,
    0.563265,
    0.551229,
    5.791117598330761e21,
    0.127568,
    0.566949,
    0.550556,
    5.836354124879747e21,
    0.126453,
    0.570633,
    0.549841,
    5.881602188415864e21,
    0.125394,
    0.574318,
    0.549086,
    5.926838714964848e21,
    0.124395,
    0.578002,
    0.548287,
    5.972086778500965e21,
    0.123463,
    0.581687,
    0.547445,
    6.017334842037084e21,
    0.122606,
    0.585371,
    0.546557,
    6.062571368586069e21,
    0.121831,
    0.589055,
    0.545623,
    6.107819432122186e21,
    0.121148,
    0.592739,
    0.544641,
    6.153055958671171e21,
    0.120565,
    0.596422,
    0.543611,
    6.19830402220729e21,
    0.120092,
    0.600104,
    0.54253,
    6.243540548756273e21,
    0.119738,
    0.603785,
    0.5414,
    6.288788612292391e21,
    0.119512,
    0.607464,
    0.540218,
    6.334036675828509e21,
    0.119423,
    0.611141,
    0.538982,
    6.379273202377494e21,
    0.119483,
    0.614817,
    0.537692,
    6.424521265913612e21,
    0.119699,
    0.61849,
    0.536347,
    6.469757792462596e21,
    0.120081,
    0.622161,
    0.534946,
    6.515005855998715e21,
    0.120638,
    0.625828,
    0.533488,
    6.560242382547699e21,
    0.12138,
    0.629492,
    0.531973,
    6.605490446083816e21,
    0.122312,
    0.633153,
    0.530398,
    6.650738509619935e21,
    0.123444,
    0.636809,
    0.528763,
    6.69597503616892e21,
    0.12478,
    0.640461,
    0.527068,
    6.741223099705037e21,
    0.126326,
    0.644107,
    0.525311,
    6.786459626254022e21,
    0.128087,
    0.647749,
    0.523491,
    6.831707689790141e21,
    0.130067,
    0.651384,
    0.521608,
    6.876944216339124e21,
    0.132268,
    0.655014,
    0.519661,
    6.922192279875242e21,
    0.134692,
    0.658636,
    0.517649,
    6.96744034341136e21,
    0.137339,
    0.662252,
    0.515571,
    7.012676869960345e21,
    0.14021,
    0.665859,
    0.513427,
    7.057924933496463e21,
    0.143303,
    0.669459,
    0.511215,
    7.103161460045448e21,
    0.146616,
    0.67305,
    0.508936,
    7.148409523581566e21,
    0.150148,
    0.676631,
    0.506589,
    7.19364605013055e21,
    0.153894,
    0.680203,
    0.504172,
    7.238894113666667e21,
    0.157851,
    0.683765,
    0.501686,
    7.284142177202785e21,
    0.162016,
    0.687316,
    0.499129,
    7.329378703751771e21,
    0.166383,
    0.690856,
    0.496502,
    7.374626767287888e21,
    0.170948,
    0.694384,
    0.493803,
    7.419863293836873e21,
    0.175707,
    0.6979,
    0.491033,
    7.465111357372992e21,
    0.180653,
    0.701402,
    0.488189,
    7.510347883921975e21,
    0.185783,
    0.704891,
    0.485273,
    7.555595947458093e21,
    0.19109,
    0.708366,
    0.482284,
    7.600844010994211e21,
    0.196571,
    0.711827,
    0.479221,
    7.646080537543196e21,
    0.202219,
    0.715272,
    0.476084,
    7.691328601079314e21,
    0.20803,
    0.718701,
    0.472873,
    7.736565127628299e21,
    0.214,
    0.722114,
    0.469588,
    7.781813191164417e21,
    0.220124,
    0.725509,
    0.466226,
    7.827049717713401e21,
    0.226397,
    0.728888,
    0.462789,
    7.872297781249519e21,
    0.232815,
    0.732247,
    0.459277,
    7.917545844785637e21,
    0.239374,
    0.735588,
    0.455688,
    7.962782371334621e21,
    0.24607,
    0.73891,
    0.452024,
    8.008030434870739e21,
    0.252899,
    0.742211,
    0.448284,
    8.053266961419724e21,
    0.259857,
    0.745492,
    0.444467,
    8.098515024955842e21,
    0.266941,
    0.748751,
    0.440573,
    8.143751551504827e21,
    0.274149,
    0.751988,
    0.436601,
    8.188999615040944e21,
    0.281477,
    0.755203,
    0.432552,
    8.23423614158993e21,
    0.288921,
    0.758394,
    0.428426,
    8.279484205126046e21,
    0.296479,
    0.761561,
    0.424223,
    8.324732268662165e21,
    0.304148,
    0.764704,
    0.419943,
    8.36996879521115e21,
    0.311925,
    0.767822,
    0.415586,
    8.415216858747267e21,
    0.319809,
    0.770914,
    0.411152,
    8.460453385296252e21,
    0.327796,
    0.77398,
    0.40664,
    8.50570144883237e21,
    0.335885,
    0.777018,
    0.402049,
    8.550937975381353e21,
    0.344074,
    0.780029,
    0.397381,
    8.596186038917472e21,
    0.35236,
    0.783011,
    0.392636,
    8.641434102453591e21,
    0.360741,
    0.785964,
    0.387814,
    8.686670629002575e21,
    0.369214,
    0.788888,
    0.382914,
    8.731918692538693e21,
    0.377779,
    0.791781,
    0.377939,
    8.777155219087678e21,
    0.386433,
    0.794644,
    0.372886,
    8.822403282623795e21,
    0.395174,
    0.797475,
    0.367757,
    8.867639809172779e21,
    0.404001,
    0.800275,
    0.362552,
    8.912887872708897e21,
    0.412913,
    0.803041,
    0.357269,
    8.958135936245016e21,
    0.421908,
    0.805774,
    0.35191,
    9.003372462794001e21,
    0.430983,
    0.808473,
    0.346476,
    9.048620526330118e21,
    0.440137,
    0.811138,
    0.340967,
    9.093857052879103e21,
    0.449368,
    0.813768,
    0.335384,
    9.139105116415221e21,
    0.458674,
    0.816363,
    0.329727,
    9.184341642964204e21,
    0.468053,
    0.818921,
    0.323998,
    9.229589706500323e21,
    0.477504,
    0.821444,
    0.318195,
    9.274837770036442e21,
    0.487026,
    0.823929,
    0.312321,
    9.320074296585426e21,
    0.496615,
    0.826376,
    0.306377,
    9.365322360121544e21,
    0.506271,
    0.828786,
    0.300362,
    9.410558886670529e21,
    0.515992,
    0.831158,
    0.294279,
    9.455806950206645e21,
    0.525776,
    0.833491,
    0.288127,
    9.50104347675563e21,
    0.535621,
    0.835785,
    0.281908,
    9.54629154029175e21,
    0.545524,
    0.838039,
    0.275626,
    9.59153960382787e21,
    0.555484,
    0.840254,
    0.269281,
    9.63677613037685e21,
    0.565498,
    0.84243,
    0.262877,
    9.682024193912969e21,
    0.575563,
    0.844566,
    0.256415,
    9.727260720461955e21,
    0.585678,
    0.846661,
    0.249897,
    9.772508783998071e21,
    0.595839,
    0.848717,
    0.243329,
    9.817745310547056e21,
    0.606045,
    0.850733,
    0.236712,
    9.862993374083176e21,
    0.616293,
    0.852709,
    0.230052,
    9.908241437619292e21,
    0.626579,
    0.854645,
    0.223353,
    9.953477964168276e21,
    0.636902,
    0.856542,
    0.21662,
    9.998726027704395e21,
    0.647257,
    0.8584,
    0.209861,
    1.004396255425338e22,
    0.657642,
    0.860219,
    0.203082,
    1.0089210617789497e22,
    0.668054,
    0.861999,
    0.196293,
    1.013444714433848e22,
    0.678489,
    0.863742,
    0.189503,
    1.0179695207874602e22,
    0.688944,
    0.865448,
    0.182725,
    1.0224943271410718e22,
    0.699415,
    0.867117,
    0.175971,
    1.0270179797959702e22,
    0.709898,
    0.868751,
    0.169257,
    1.031542786149582e22,
    0.720391,
    0.87035,
    0.162603,
    1.0360664388044805e22,
    0.730889,
    0.871916,
    0.156029,
    1.0405912451580921e22,
    0.741388,
    0.873449,
    0.149561,
    1.0451148978129906e22,
    0.751884,
    0.874951,
    0.143228,
    1.0496397041666024e22,
    0.762373,
    0.876424,
    0.137064,
    1.0541633568215012e22,
    0.772852,
    0.877868,
    0.131109,
    1.0586881631751128e22,
    0.783315,
    0.879285,
    0.125405,
    1.0632129695287244e22,
    0.79376,
    0.880678,
    0.120005,
    1.0677366221836235e22,
    0.804182,
    0.882046,
    0.114965,
    1.0722614285372347e22,
    0.814576,
    0.883393,
    0.110347,
    1.0767850811921334e22,
    0.82494,
    0.88472,
    0.106217,
    1.0813098875457452e22,
    0.83527,
    0.886029,
    0.102646,
    1.0858335402006436e22,
    0.845561,
    0.887322,
    0.099702,
    1.0903583465542554e22,
    0.85581,
    0.888601,
    0.097452,
    1.094883152907867e22,
    0.866013,
    0.889868,
    0.095953,
    1.0994068055627653e22,
    0.876168,
    0.891125,
    0.09525,
    1.1039316119163773e22,
    0.886271,
    0.892374,
    0.095374,
    1.108455264571276e22,
    0.89632,
    0.893616,
    0.096335,
    1.1129800709248872e22,
    0.906311,
    0.894855,
    0.098125,
    1.117503723579786e22,
    0.916242,
    0.896091,
    0.100717,
    1.1220285299333978e22,
    0.926106,
    0.89733,
    0.104071,
    1.1265533362870096e22,
    0.935904,
    0.89857,
    0.108131,
    1.1310769889419079e22,
    0.945636,
    0.899815,
    0.112838,
    1.13560179529552e22,
    0.9553,
    0.901065,
    0.118128,
    1.1401254479504182e22,
    0.964894,
    0.902323,
    0.123941,
    1.1446502543040302e22,
    0.974417,
    0.90359,
    0.130215,
    1.1491739069589286e22,
    0.983868,
    0.904867,
    0.136897,
    1.1536987133125404e22,
    0.993248,
    0.906157,
    0.143936,
]
retentionLUT.NanColor = [1.0, 0.0, 0.0]
retentionLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'retention'
retentionPWF = GetOpacityTransferFunction("retention")
retentionPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1536987133125404e22, 1.0, 0.5, 0.0]
retentionPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
retentionxdmfDisplay.Representation = "Surface"
retentionxdmfDisplay.ColorArrayName = ["POINTS", "retention"]
retentionxdmfDisplay.LookupTable = retentionLUT
retentionxdmfDisplay.SelectTCoordArray = "None"
retentionxdmfDisplay.SelectNormalArray = "None"
retentionxdmfDisplay.SelectTangentArray = "None"
retentionxdmfDisplay.OSPRayScaleArray = "retention"
retentionxdmfDisplay.OSPRayScaleFunction = "PiecewiseFunction"
retentionxdmfDisplay.SelectOrientationVectors = "None"
retentionxdmfDisplay.ScaleFactor = 0.002500000037252903
retentionxdmfDisplay.SelectScaleArray = "retention"
retentionxdmfDisplay.GlyphType = "Arrow"
retentionxdmfDisplay.GlyphTableIndexArray = "retention"
retentionxdmfDisplay.GaussianRadius = 0.00012500000186264516
retentionxdmfDisplay.SetScaleArray = ["POINTS", "retention"]
retentionxdmfDisplay.ScaleTransferFunction = "PiecewiseFunction"
retentionxdmfDisplay.OpacityArray = ["POINTS", "retention"]
retentionxdmfDisplay.OpacityTransferFunction = "PiecewiseFunction"
retentionxdmfDisplay.DataAxesGrid = "GridAxesRepresentation"
retentionxdmfDisplay.PolarAxes = "PolarAxesRepresentation"
retentionxdmfDisplay.ScalarOpacityFunction = retentionPWF
retentionxdmfDisplay.ScalarOpacityUnitDistance = 0.0006034795097162568
retentionxdmfDisplay.OpacityArrayName = ["POINTS", "retention"]
retentionxdmfDisplay.SelectInputVectors = [None, ""]
retentionxdmfDisplay.WriteLog = ""

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
retentionxdmfDisplay.ScaleTransferFunction.Points = [
    -1.0142164766896024e21,
    0.0,
    0.5,
    0.0,
    5.176970525305538e21,
    1.0,
    0.5,
    0.0,
]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
retentionxdmfDisplay.OpacityTransferFunction.Points = [
    -1.0142164766896024e21,
    0.0,
    0.5,
    0.0,
    5.176970525305538e21,
    1.0,
    0.5,
    0.0,
]

# setup the color legend parameters for each legend in this view

# get color legend/bar for retentionLUT in view retention_3d_view
retentionLUTColorBar = GetScalarBar(retentionLUT, retention_3d_view)
retentionLUTColorBar.WindowLocation = "Any Location"
retentionLUTColorBar.Position = [0.65, 0.320625]
retentionLUTColorBar.Title = "H retention (H/m$^3$)"
retentionLUTColorBar.ComponentTitle = ""
retentionLUTColorBar.TitleJustification = "Left"
retentionLUTColorBar.HorizontalTitle = 1
retentionLUTColorBar.ScalarBarLength = 0.3299999999999999
retentionLUTColorBar.AutomaticLabelFormat = 0
retentionLUTColorBar.LabelFormat = "%-#6.1e"
retentionLUTColorBar.TitleFontSize = 25
retentionLUTColorBar.LabelFontSize = 25

# set color bar visibility
retentionLUTColorBar.Visibility = 1

# show color legend
retentionxdmfDisplay.SetScalarBarVisibility(retention_3d_view, True)

# ----------------------------------------------------------------
# setup the visualization in view 'geometry_view'
# ----------------------------------------------------------------

# show data from mesh_cellsxdmf
mesh_cellsxdmfDisplay = Show(
    mesh_cellsxdmf, geometry_view, "UnstructuredGridRepresentation"
)

# get 2D transfer function for 'f'
fTF2D = GetTransferFunction2D("f")

# get color transfer function/color map for 'f'
fLUT = GetColorTransferFunction("f")
fLUT.TransferFunction2D = fTF2D
fLUT.RGBPoints = [6.0, 0.7, 0.7, 0.7, 7.1, 0.89, 0.57, 0.278, 8.0, 0.698, 0.38, 0.121]
fLUT.ColorSpace = "Step"
fLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'f'
fPWF = GetOpacityTransferFunction("f")
fPWF.Points = [6.0, 0.0, 0.5, 0.0, 8.0, 1.0, 0.5, 0.0]
fPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
mesh_cellsxdmfDisplay.Representation = "Surface With Edges"
mesh_cellsxdmfDisplay.ColorArrayName = ["CELLS", "f"]
mesh_cellsxdmfDisplay.LookupTable = fLUT
mesh_cellsxdmfDisplay.SelectTCoordArray = "None"
mesh_cellsxdmfDisplay.SelectNormalArray = "None"
mesh_cellsxdmfDisplay.SelectTangentArray = "None"
mesh_cellsxdmfDisplay.EdgeColor = [
    0.34509803921568627,
    0.34509803921568627,
    0.34509803921568627,
]
mesh_cellsxdmfDisplay.OSPRayScaleFunction = "PiecewiseFunction"
mesh_cellsxdmfDisplay.SelectOrientationVectors = "None"
mesh_cellsxdmfDisplay.ScaleFactor = 0.0025000000000000005
mesh_cellsxdmfDisplay.SelectScaleArray = "f"
mesh_cellsxdmfDisplay.GlyphType = "Arrow"
mesh_cellsxdmfDisplay.GlyphTableIndexArray = "f"
mesh_cellsxdmfDisplay.GaussianRadius = 0.000125
mesh_cellsxdmfDisplay.SetScaleArray = [None, ""]
mesh_cellsxdmfDisplay.ScaleTransferFunction = "PiecewiseFunction"
mesh_cellsxdmfDisplay.OpacityArray = [None, ""]
mesh_cellsxdmfDisplay.OpacityTransferFunction = "PiecewiseFunction"
mesh_cellsxdmfDisplay.DataAxesGrid = "GridAxesRepresentation"
mesh_cellsxdmfDisplay.PolarAxes = "PolarAxesRepresentation"
mesh_cellsxdmfDisplay.ScalarOpacityFunction = fPWF
mesh_cellsxdmfDisplay.ScalarOpacityUnitDistance = 0.0005173787484846768
mesh_cellsxdmfDisplay.OpacityArrayName = ["CELLS", "f"]
mesh_cellsxdmfDisplay.SelectInputVectors = [None, ""]
mesh_cellsxdmfDisplay.WriteLog = ""

# show data from transform1
transform1Display = Show(transform1, geometry_view, "UnstructuredGridRepresentation")

# trace defaults for the display properties.
transform1Display.Representation = "Surface"
transform1Display.ColorArrayName = ["CELLS", "f"]
transform1Display.LookupTable = fLUT
transform1Display.SelectTCoordArray = "None"
transform1Display.SelectNormalArray = "None"
transform1Display.SelectTangentArray = "None"
transform1Display.OSPRayScaleFunction = "PiecewiseFunction"
transform1Display.SelectOrientationVectors = "None"
transform1Display.ScaleFactor = 0.0007500152745974708
transform1Display.SelectScaleArray = "None"
transform1Display.GlyphType = "Arrow"
transform1Display.GlyphTableIndexArray = "None"
transform1Display.GaussianRadius = 3.750076372987354e-05
transform1Display.SetScaleArray = [None, ""]
transform1Display.ScaleTransferFunction = "PiecewiseFunction"
transform1Display.OpacityArray = [None, ""]
transform1Display.OpacityTransferFunction = "PiecewiseFunction"
transform1Display.DataAxesGrid = "GridAxesRepresentation"
transform1Display.PolarAxes = "PolarAxesRepresentation"
transform1Display.ScalarOpacityFunction = fPWF
transform1Display.ScalarOpacityUnitDistance = 0.0006079671753747626
transform1Display.OpacityArrayName = ["CELLS", "f"]
transform1Display.SelectInputVectors = [None, ""]
transform1Display.WriteLog = ""

# show data from transform2
transform2Display = Show(transform2, geometry_view, "GeometryRepresentation")

# trace defaults for the display properties.
transform2Display.Representation = "Surface"
transform2Display.ColorArrayName = ["CELLS", "f"]
transform2Display.LookupTable = fLUT
transform2Display.SelectTCoordArray = "None"
transform2Display.SelectNormalArray = "None"
transform2Display.SelectTangentArray = "None"
transform2Display.OSPRayScaleFunction = "PiecewiseFunction"
transform2Display.SelectOrientationVectors = "None"
transform2Display.ScaleFactor = 0.0025000000000000005
transform2Display.SelectScaleArray = "None"
transform2Display.GlyphType = "Arrow"
transform2Display.GlyphTableIndexArray = "None"
transform2Display.GaussianRadius = 0.000125
transform2Display.SetScaleArray = [None, ""]
transform2Display.ScaleTransferFunction = "PiecewiseFunction"
transform2Display.OpacityArray = [None, ""]
transform2Display.OpacityTransferFunction = "PiecewiseFunction"
transform2Display.DataAxesGrid = "GridAxesRepresentation"
transform2Display.PolarAxes = "PolarAxesRepresentation"
transform2Display.SelectInputVectors = [None, ""]
transform2Display.WriteLog = ""

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'temperature'
temperaturePWF = GetOpacityTransferFunction("temperature")
temperaturePWF.Points = [
    333.5612487792969,
    0.0,
    0.5,
    0.0,
    1157.0723875561523,
    1.0,
    0.5,
    0.0,
]
temperaturePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

for view in [toroidal_view, poloidal_view, retention_3d_view, geometry_view]:
    view.ViewTime = retentionxdmf.TimestepValues[-1]
    SetActiveView(view)
    LoadPalette(paletteName="WhiteBackground")

# ----------------------------------------------------------------
# export views
# ----------------------------------------------------------------
ExportView("toroidal.pdf", view=toroidal_view)
SaveScreenshot("toroidal.png", toroidal_view, OverrideColorPalette="WhiteBackground")

ExportView("poloidal.pdf", view=poloidal_view)
SaveScreenshot("poloidal.png", poloidal_view, OverrideColorPalette="WhiteBackground")

ExportView("retention_3d.pdf", view=retention_3d_view)
SaveScreenshot(
    "retention_3d.png", retention_3d_view, OverrideColorPalette="WhiteBackground"
)

ExportView("geometry.pdf", view=geometry_view)
SaveScreenshot("geometry.png", geometry_view, OverrideColorPalette="WhiteBackground")

if __name__ == "__main__":
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory="extracts")
