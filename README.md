
## Project Overview

Industrial Inspection Systems is a computer-vision project focused on detecting defects in printed circuit board (PCB) images. It uses the public DsPCBSD+ dataset and is intended to grow into an inspection workflow with defect localisation, measurement, a backend API, and stored inspection results.

The repository currently includes sample images, an exploratory image-analysis notebook, and an initial sample-image validation test. The complete application is under development; there is not yet a server entry point to launch.

## Run the Project

### Prerequisites

- Python 3.13 or newer
- [Poetry](https://python-poetry.org/docs/#installation)
- Visual Studio Code with the Python and Jupyter extensions to run the notebook in VS Code

### Set up the environment

From the repository root, create the Poetry environment and install the application, development, and notebook dependencies:

```powershell
poetry env use 3.13
poetry install --with dev,notebooks
```

Register the environment as a Jupyter kernel:

```powershell
poetry run python -m ipykernel install --user --name industrial-inspection-systems --display-name "Python (industrial-inspection-systems)"
```

### Run the image-analysis notebook

1. Open `notebooks/Image_related_exp.ipynb` in VS Code.
2. Select the **Python (industrial-inspection-systems)** kernel.
3. Run the notebook cells in order.

The notebook reads `data/image-samples/985_data.jpg`. Update the image path in the notebook if the sample is stored elsewhere on your machine.

### Run the tests

From the repository root, run:

```powershell
poetry run pytest
```


## Dataset & Attribution

This project uses the **DsPCBSD+ (PCB Surface Defect Dataset)** for developing and evaluating PCB defect detection models.

**Dataset:** [DsPCBSD+ – Figshare](https://doi.org/10.6084/m9.figshare.24970329)

**Research Paper:** [DsPCBSD+: A PCB surface defect dataset](https://doi.org/10.1038/s41597-024-03656-8)

**License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

The dataset contains 10,259 PCB images across nine defect categories, with 20,276 bounding-box annotations.

The complete dataset is not included in this repository. Users must download it separately from the original source. A small selection of sample images may be included for demonstration and testing purposes.

All credit for the original dataset belongs to its respective authors and contributors.
