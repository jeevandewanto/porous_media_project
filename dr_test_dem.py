# main script for dem sim

import numpy as np
from matplotlib import pyplot as plt
from generator import make_polygon_from_edge_length, make_container_separate
from entities import Particle


def plot_polygon(vertices, color='blue', fill=True, alpha=0.4):
    # Close the polygon by appending the first vertex at the end
    closed_vertices = np.vstack([vertices, vertices[0]])
    x, y = closed_vertices[:, 0], closed_vertices[:, 1]
    
    if fill:
        plt.fill(x, y, color=color, alpha=alpha)
    else:
        plt.plot(x, y, color=color)

    plt.axis('equal')

centroid = [1.0, 2.0]
radius = 0.5
edge_length = 0.3
rho = 2.0

vertices = make_polygon_from_edge_length(radius=0.1, edge_length=0.05, centroid=[0.5, 0.5])
particle = Particle(com_pos=[0.5, 0.5], velocity=[0.0, 0.0], vertices=vertices, density=1000)
walls = make_container_separate(length=1.0, width=1.0, thickness=0.1)

print("Area:", particle.area)
print("Mass:", particle.mass)

# Plot everything
plot_polygon(particle.vertices, color='red')
for wall in walls:
    plot_polygon(wall.vertices, color='black', alpha=0.3)
plt.scatter(*particle.pos, color='k')
plt.title("DEM Setup")
plt.show()

		