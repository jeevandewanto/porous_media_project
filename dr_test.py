# testing script
import numpy as np
from matplotlib import pyplot as plt
from src.geometry.generator import make_polygon_from_edge_length, generate_grid_hexagonal, make_container
from src.plot.plotter import plot_container


xp, yp = generate_grid_hexagonal(length = 10, width = 10, radius = 0.5)
xver_wall, yver_wall = make_container(10,10,1)

polygons = []
minRadius = 0.2
maxRadius = 0.45
    
for x0, y0 in zip(xp.ravel(), yp.ravel()):
    radiusRand = minRadius + (maxRadius-minRadius) * np.random.rand()
    xver, yver, nver = make_polygon_from_edge_length(radius=radiusRand, edge_length=0.2, centroid=[x0, y0])
    polygons.append((xver, yver))


fig1, ax1 = plt.subplots()
ax1.plot(xp,yp,'xr')
for xver, yver in polygons:
    ax1.plot(xver, yver, 'k-')
ax1.set_aspect('equal'); ax1.grid()

# Plot wall
for i in range(xver_wall.shape[0]):
        ax1.fill(xver_wall[i], yver_wall[i], color='gray', alpha=0.7, edgecolor='black')

# plt.ion()
plt.gca().set_aspect('equal')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("DEM Container with Wall Thickness")
plt.grid(False)
plt.show()