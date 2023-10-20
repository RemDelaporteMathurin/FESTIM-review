import meshio

mesh = meshio.read("mesh_3D_6mm.med")

# ----------------------------- Convert to GMSH .msh ----------------------------- #

cell_data = {
    "gmsh:geometrical": [
        -1 * mesh.cell_data_dict["cell_tags"]["line"],
        -1 * mesh.cell_data_dict["cell_tags"]["tetra"],
        -1 * mesh.cell_data_dict["cell_tags"]["triangle"],
    ],
    "gmsh:physical": [
        -1 * mesh.cell_data_dict["cell_tags"]["line"],
        -1 * mesh.cell_data_dict["cell_tags"]["tetra"],
        -1 * mesh.cell_data_dict["cell_tags"]["triangle"],
    ],
}

meshio.write_points_cells(
    "mesh.msh",
    mesh.points,
    mesh.cells,
    cell_data=cell_data,
    file_format="gmsh22",
    binary=False,
)


# --------------------------- Convert to NASTRAN (.nas) --------------------------- #

import numpy as np


# monkey patching the function _float_to_nastran_string until PR nschloe/meshio/pull/1437 is merged
def new_float_to_nastran_string(value, length=16):
    """
    From
    <https://docs.plm.automation.siemens.com/data_services/resources/nxnastran/10/help/en_US/tdocExt/pdf/User.pdf>:

    Real numbers, including zero, must contain a decimal point. You can enter
    real numbers in a variety of formats. For example, the following are all
    acceptable versions of the real number, seven:
    ```
    7.0   .7E1  0.7+1
    .70+1 7.E+0 70.-1
    ```

    This methods converts a float value into the corresponding string. Choose
    the variant with `E` to make the file less ambigious when edited by a
    human. (`5.-1` looks like 4.0, not 5.0e-1 = 0.5.)

    Examples:
        1234.56789 --> "1.23456789E+3"
        -0.1234 --> "-1.234E-1"
        3.1415926535897932 --> "3.14159265359E+0"
    """
    out = np.format_float_scientific(value, exp_digits=1, precision=9).replace("e", "E")

    assert len(out) <= 16
    return out


meshio.nastran._nastran._float_to_nastran_string = new_float_to_nastran_string

meshio.write_points_cells(
    "mesh.nas",
    mesh.points,
    mesh.cells,
)


# ---------------------------- Convert to XDMF (.xdmf) ---------------------------- #

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

correspondance_dict = mesh.cell_tags

print(correspondance_dict)
