import meshio

mesh = meshio.read("mesh_3D_6mm.med")

cell_data = {"gmsh:geometrical": [
    -1 * mesh.cell_data_dict["cell_tags"]['line'],
    -1 * mesh.cell_data_dict["cell_tags"]['tetra'],
    -1 * mesh.cell_data_dict["cell_tags"]['triangle']
    ]
}

correspondance_dict = mesh.cell_tags
print(correspondance_dict)


# WRITE TO GMSH FORMAT

meshio.write_points_cells(
    "mesh.msh",
    mesh.points,
    mesh.cells,
    cell_data=cell_data,
    file_format='gmsh22'
)

# WRITE TO XDMF FORMAT

cell_data_types = mesh.cell_data_dict["cell_tags"].keys()

cell_type = "tetra"
facet_type = "triangle"
for mesh_block in mesh.cells:
    if mesh_block.type == cell_type:
        meshio.write_points_cells(
            "mesh_cells.xdmf",
            mesh.points,
            [mesh_block],
            cell_data={"f": [-1 * mesh.cell_data_dict["cell_tags"][cell_type]]},
        )
    elif mesh_block.type == facet_type:
        meshio.write_points_cells(
            "mesh_facets.xdmf",
            mesh.points,
            [mesh_block],
            cell_data={"f": [-1 * mesh.cell_data_dict["cell_tags"][facet_type]]},
        )
