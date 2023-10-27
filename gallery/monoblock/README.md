# 3D monoblock simulation

To run this example in transient:

```
python main.py
```

This should create several .xdmf and .h5 files.
To visualise them, open Paraview. Then `Files/load state` and select visualisation.py

You can also run paraview with python.
First create a paraview env:

```
conda create -n paraview
conda activate paraview
conda install -c conda-forge paraview
```
then run:
```
pvpython --force-offscreen-rendering visualisation.py
```

This will export the visualisation to pdf and png.

To run the steady-state version:

```
python steady_state.py
```

> **_NOTE:_** You will have to move the generated files to the level of visualisation.py in order to visualise them with the pre-made visualisations.