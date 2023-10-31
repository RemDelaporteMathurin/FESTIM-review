# trace generated using paraview version 5.11.2
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


def extract_concentration_profile(filename, dataname, export_dataname=None):
    # create a new 'Xdmf3ReaderS'
    if filename.endswith(".xdmf"):
        source = Xdmf3ReaderS(FileName=[filename])

    # get animation scene
    animationScene1 = GetAnimationScene()

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    renderView1 = GetActiveViewOrCreate("RenderView")

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Plot Over Line'
    plotOverLine1 = PlotOverLine(registrationName="PlotOverLine1", Input=source)
    plotOverLine1.Point1 = [0.0, 0.006, 0.0]
    plotOverLine1.Point2 = [0.0, 0.0135, 0.0]
    plotOverLine1.Resolution = 10000

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, renderView1, "GeometryRepresentation")

    # Create a new 'Line Chart View'
    lineChartView1 = CreateView("XYChartView")

    # show data in view
    plotOverLine1Display_1 = Show(
        plotOverLine1, lineChartView1, "XYChartRepresentation"
    )

    animationScene1.GoToLast()

    if export_dataname is None:
        export_dataname = dataname

    # save data
    SaveData(
        f"{dataname}_profile.csv",
        proxy=plotOverLine1,
        PointDataArrays=["arc_length", export_dataname, "vtkValidPointMask"],
    )


extract_concentration_profile("./retention.xdmf", "retention")
extract_concentration_profile("./mobile_concentration.xdmf", "mobile_concentration")
