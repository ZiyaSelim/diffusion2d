"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt
from .output import create_plot, output_plots


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
            (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
            + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

    u_nm1 = u.copy()
    return u_nm1, u


def solve(dx=0.1, dy=0.1, D=4.0):
    """
    Runs the 2D diffusion simulation.

    Args:
        dx (float): Interval in x-direction (mm).
        dy (float): Interval in y-direction (mm).
        D (float): Thermal diffusivity of steel (mm^2/s).
    """
    w = h = 10.
    T_cold = 300
    T_hot = 700

    nx, ny = int(w / dx), int(h / dy)
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    print("dt = {}".format(dt))

    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    r = min(h, w) / 4.0
    cx = w / 2.0
    cy = h / 2.0
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    nsteps = 101
    n_output = [0, 10, 50, 100]
    fig_counter = 0
    fig = plt.figure()
    im = None  
    
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

        if n in n_output:
            fig_counter += 1
            im = create_plot(fig, fig_counter, u, n, dt, T_cold, T_hot)

    if im:
        output_plots(fig, im)
    else:
        print("Error: No plots were generated.")

if __name__ == "__main__":
    solve()