from heat_transfer_parameters import my_heat_transfer_model
import fenics as fe
import festim as F

# run heat transfer model
my_heat_transfer_model.initialise()

# export temperature field
T = my_heat_transfer_model.T.T
fe.XDMFFile("Results/temperature_field_3D.xdmf").write_checkpoint(
    T, "T", 0, fe.XDMFFile.Encoding.HDF5, append=False
)

# take slice from centre
class slicer(fe.UserExpression):
    def eval(self, value, x):

        value[0] = T(x[0], x[1], 0.116 / 2)

    def value_shape(self):
        return ()

# read 2D mesh
mesh_2D = F.MeshFromXDMF(
    volume_file="meshes/mesh_domains_2D.xdmf",
    boundary_file="meshes/mesh_boundaries_2D.xdmf",
)

# project slice onto 2D mesh
V_2D = fe.FunctionSpace(mesh_2D.mesh, "CG", 1)
T.set_allow_extrapolation(True)
print("Projecting onto 2D mesh")
T_sl = fe.interpolate(slicer(), V_2D)

# export slice
fe.XDMFFile("Results/temperature_field_slice.xdmf").write_checkpoint(
        T_sl, "T", 0, fe.XDMFFile.Encoding.HDF5, append=False
    )