import numpy as np
import pyvista as pv
import pandas as pd

### This code visualizes the datapoints generated earlier and gives an interactive window to rotate the 3d model of the disk ###

data = pd.read_csv("disk_points.csv")
x = data['x'].values
y = data['y'].values
z = data['z'].values
r = data['r'].values

theta = [i*5 for i in range(0, 19)]

# Create point cloud and plot
points = np.column_stack((x, y, z))
cloud = pv.PolyData(points)
cloud['radius'] = r

plotter = pv.Plotter()
plotter.add_points(cloud, scalars='radius', cmap='viridis_r', point_size=2, opacity=0.5, show_scalar_bar=False)
plotter.set_scale(xscale=1.0, yscale=1.0, zscale=1.0)
plotter.show()