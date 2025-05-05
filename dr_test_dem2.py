# dr_test_dem.py
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

from generator import make_polygon_from_edge_length, make_container_separate
from entities import Particle, Wall

# -- Parameters --
g = np.array([0, -9.81])  # gravity
dt = 0.01
steps = 100

# -- Create particle --
vertices = make_polygon_from_edge_length(radius=0.1, edge_length=0.07)
particle = Particle(com_pos=[1, 7], velocity=[0.0, 0.0], vertices=vertices, density=1000)
# Make walls
walls = make_container_separate(length=1.0, width=1.0, thickness=0.1)

# -- Simulation loop --
# positions = []

# for step in range(steps):
#     particle.reset_force()
#     particle.apply_force(particle.mass * g)
#     particle.integrate_explicit(dt)
#     positions.append(particle.pos.copy())

# # -- Plot result --
# positions = np.array(positions)
# # plt.plot(positions[:, 0], positions[:, 1], marker='o')
# plt.plot(range(steps), positions[:, 1], marker='o')
# plt.title("Particle Trajectory Under Gravity")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.axis("equal")
# plt.show()

# -- Visualization setup --
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 2)
ax.set_ylim(0, 10)

polygon_patch, = ax.fill([], [], 'skyblue', edgecolor='k')

# -- Animation update function --
def update(frame):
    particle.reset_force()
    particle.apply_force(particle.mass * g)
    particle.integrate_explicit(dt)

    polygon_patch.set_xy(particle.vertices)
    return polygon_patch,

# -- Run animation --
ani = animation.FuncAnimation(
    fig, update, frames=steps, interval=30, blit=True, repeat=False
)
plt.show()

