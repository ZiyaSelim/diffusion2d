import matplotlib.pyplot as plt

def create_plot(fig, fig_counter, u, n, dt, T_cold, T_hot):
  """
  Creates a single subplot for the diffusion data at a specific timestep.

  Args:
      fig (matplotlib.figure.Figure): The main figure object.
      fig_counter (int): The index for the subplot (1 to 4).
      u (numpy.ndarray): The 2D temperature array.
      n (int): The current timestep number.
      dt (float): The time step size.
      T_cold (float): The minimum temperature for the colormap.
      T_hot (float): The maximum temperature for the colormap.

  Returns:
      matplotlib.image.AxesImage: The 'im' object created by imshow, needed for the colorbar.
  """
  ax = fig.add_subplot(220 + fig_counter)
  # We plot u.copy() because u is modified in the main loop
  im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
  ax.set_axis_off()
  ax.set_title('{:.1f} ms'.format(n * dt * 1000))
  return im


def output_plots(fig, im):
  """
  Adds the final colorbar to the figure and saves it to a file.

  Args:
      fig (matplotlib.figure.Figure): The main figure object.
      im (matplotlib.image.AxesImage): The image object from the last plot, used for the colorbar.
      filename (str): The name of the output image file.
  """
  fig.subplots_adjust(right=0.85)
  cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
  cbar_ax.set_xlabel('$T$ / K', labelpad=20)
  fig.colorbar(im, cax=cbar_ax)
  plt.show()