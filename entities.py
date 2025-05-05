# entities.py
import numpy as np

class RigidBody2D:
    def __init__(self, vertices):
        self.vertices = np.array(vertices, dtype=float)
        self.area = self._compute_area()
        self.force = np.zeros(2)
        self.is_static = True  # By default, assume static

    def _compute_area(self):
        x, y = self.vertices[:, 0], self.vertices[:, 1]
        return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

    def apply_force(self, force):
        if not self.is_static:
            self.force += force

    def reset_force(self):
        self.force[:] = 0.0

    def integrate_explicit(self, dt):
        if not self.is_static:
            acc = self.force / self.mass
            self.vel += acc * dt
            self.pos += self.vel * dt
            self.vertices += self.vel * dt  # shift polygon
            self.reset_force()

class Particle(RigidBody2D):
    def __init__(self, com_pos, velocity, vertices, density):
        vertices = np.array(vertices, dtype=float)
        centroid = np.mean(vertices, axis=0)
        shift = np.array(com_pos) - centroid
        vertices += shift  # Move polygon so its centroid matches com_pos

        super().__init__(vertices)
        self.pos = np.array(com_pos, dtype=float)
        self.vel = np.array(velocity, dtype=float)
        self.mass = self.area * density
        self.is_static = False

class Wall(RigidBody2D):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.mass = np.inf
        self.is_static = True
