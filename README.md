# FESTIM-review

## Overview

This repository contains Python scripts for the FESTIM review paper.

## Contents

1. [Gallery](#gallery)
    - [TDS](#tds)
    - [Monoblock](#monoblock)
2. [Comparison](#comparison)
    - [COMSOL](#comsol)
    - [TMAP8](#tmap8)
3. [Verification](#verification)
4. [How to Use](#how-to-use)

## Gallery

The `gallery` folder contains FESTIM scripts for simulating different scenarios. 

### TDS

Scripts in this subfolder simulate a Thermal Desorption Spectroscopy (TDS) experiment using the FESTIM model.

### Monoblock

This subfolder contains scripts for simulating a monoblock model using FESTIM.

## Comparison

The `comparison` folder includes scripts for comparing FESTIM results with other models.

### COMSOL

Scripts in this subfolder are used for comparing FESTIM simulations with results obtained using COMSOL 6.1.

### TMAP8

This subfolder contains scripts for comparing FESTIM simulations with results obtained using the TMAP8 model.

## Verification

The `verification` folder contains scripts for verifying the accuracy of FESTIM using the method of manufactured solutions.

## How to Use

1. Clone this repository to your local machine.
2. Create a Conda environment using the provided `environment.yml` file:

    ```bash
    conda env create -f environment.yml
    ```

   This will set up a Conda environment named `festim-review-env` with all the required dependencies for running the FESTIM scripts and visualisation scripts.

3. Activate the Conda environment:

    ```bash
    conda activate festim-review-env
    ```

4. Execute the Python scripts using the activated Conda environment and ensure compatibility with FESTIM requirements.

5. Navigate to the desired folder based on the simulation or comparison you are interested in.

**Note**: TMAP8 isn't included in this conda environment. In order to run the TMAP8 scripts, refer to the [TMAP8 installation instructions in this repo](https://github.com/RemDelaporteMathurin/FESTIM-review/tree/main/comparison/tmap8#readme).

**Note**: Since COMSOL is proprietary, a license is required to run the model.

## Contact

For any questions or issues, please contact remidm@mit.edu.
