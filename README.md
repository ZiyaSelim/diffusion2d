# diffusion2d

## Instructions for students

This repository contains a simple 2D diffusion solver, packaged as an exercise for the Simulation Software Engineering course.

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

This package provides a solver for the 2D diffusion equation over a square domain. The simulation starts with a domain at a constant `T_cold` temperature and a central circular disc at a higher `T_hot` temperature.

The equation is solved using the **finite-difference method** (FDM). The code then generates a plot showing the state of the diffusion at four different timepoints.

## Installing the package

This package is hosted on **TestPyPI**. You can install it using `pip`.

Because the package dependencies (`numpy`, `matplotlib`) are on the main PyPI, you must tell `pip` to look in both indexes:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ canselza_diffusion2d
```

## Running this package

Once installed, you can run the simulation in two ways:

#### 1. As a Command-Line Script

The package installs a runnable script called solve-diffusion2d. Simply run this in your terminal:

```bash
solve-diffusion2d
```

This will run the simulation with default parameters.

#### 2. By Importing in Python

You can also import and use the `solve()` function directly within a Python script or shell. This allows you to pass custom parameters.

```python
from canselza_diffusion2d.diffusion2d import solve

# Run the simulation with default parameters
solve()

# Or run with custom parameters
# solve(dx=0.05, dy=0.05, D=5.0)
```

## Citing

If you use this code, please cite the authors.
