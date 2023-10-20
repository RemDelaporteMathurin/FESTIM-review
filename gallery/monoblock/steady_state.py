from main import my_model
import festim as F

my_model.settings.transient = False
my_model.dt = None


my_model.exports = F.Exports(
    [
        F.XDMFExport("T", folder="steady_state"),
        F.XDMFExport("solute", folder="steady_state", checkpoint=True),
        F.XDMFExport("retention", folder="steady_state", checkpoint=True),
        F.XDMFExport("1", folder="steady_state", checkpoint=True),
        F.XDMFExport("2", folder="steady_state", checkpoint=True),
    ]
)

my_model.initialise()
my_model.run()
