import numpy as np
import pyvista as pv
import pandas as pd

### This file generates the points to plot the model disk ###
# Data generation
num = 500000
theta = np.random.uniform(0, 2*np.pi, num)
r_raw = np.abs(np.random.uniform(0, 1, num)) + 0.25*np.abs(np.random.normal(0, 0.5, num))
x = r_raw * np.cos(theta)
y = r_raw * np.sin(theta)
r = np.sqrt(x**2 + y**2)
H = 0.005 * r**1.05
z = np.random.normal(0, 1, num) * H

# Save to CSV
df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'r': r})
df.to_csv('disk_points.csv', index=False)
print("Saved to disk_points.csv")

# Create point cloud and plot
points = np.column_stack((x, y, z))
cloud = pv.PolyData(points)
cloud['radius'] = r

plotter = pv.Plotter()
plotter.add_points(cloud, scalars='radius', cmap='viridis_r', point_size=2, opacity=0.5, show_scalar_bar=False)
plotter.set_scale(xscale=1.0, yscale=1.0, zscale=1.0)

# Set view along the XZ plane (i.e., look along Y axis)
plotter.camera_position = [
    (0, 5, 0),     # camera location along +Y
    (0, 0, 0),     # look at the origin
    (-2, 0, 10),     # Z is up
]

plotter.show_grid()
plotter.show()
