# 3D monoblock simulation

To run this example in transient:

```
python main.py
```

This should create several .xdmf and .h5 files.
To visualise them, open Paraview. Then `Files/load state` and select visualisation.pvsm

To run the steady-state version:

```
python steady_state.py
```

> **_NOTE:_** You will have to move the generated files to the level of visualisation.pvsm in order to visualise them with the pre-made visualisations.