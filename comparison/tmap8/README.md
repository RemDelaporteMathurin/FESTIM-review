## Install TMAP8

### 1. Install MOOSE in dev mode

https://mooseframework.inl.gov/getting_started/installation/conda.html
When creating the moose environment, use the 2023.11.30 version for reproductibility.

```
conda create -n moose moose-dev=2023.11.30
```

### 2. Install TMAP8

https://mooseframework.inl.gov/TMAP8/getting_started/installation.html

When cloning TMAP8, use this commit in order to maintain reproductibility https://github.com/idaholab/TMAP8/tree/b84d41b1280e6abfb5874aaf297ea827401e2ba8

```
git clone https://github.com/idaholab/TMAP8.git
cd TMAP8
git checkout b84d41b
```

This will create a `tmap-opt` executable file in the cloned `comparison/tmap8/TMAP8` directory.
Copy it and place it at the root of the `comparison/tmap8` directory.

## Run cases

To run FESTIM cases, activate the `festim-review-env` environment and run

```
python runner_festim.py
```

Then run TMAP8 cases with

```
python runner_tmap.py
```