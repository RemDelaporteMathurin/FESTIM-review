import meshio

mesh = meshio.read("mesh_3D_6mm.med")

cell_data = {"gmsh:geometrical": [
    -1 * mesh.cell_data_dict["cell_tags"]['line'],
    -1 * mesh.cell_data_dict["cell_tags"]['tetra'],
    -1 * mesh.cell_data_dict["cell_tags"]['triangle']
    ]
}
meshio.write_points_cells(
    "mesh.msh",
    mesh.points,
    mesh.cells,
    cell_data=cell_data,
    file_format='gmsh22'
)