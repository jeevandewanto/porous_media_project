# entities.py
import numpy as np

class RigidBody2D:
    def __init__(self, vertices):
        self.vertices = np.array(vertices, dtype=float)
        self.area = self._compute_area()
    
    def _compute_area(self):
        x, y = self.vertices[:, 0], self.vertices[:, 1]
        return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

class Particle(RigidBody2D):
    def __init__(self, com_pos, velocity, vertices, density):
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
