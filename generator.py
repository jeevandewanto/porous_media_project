# generator.py                         

import numpy as np
from entities import Wall

def make_polygon(radius:float, n_sides:int, centroid:list):
    # Generate polygon
    theta = np.linspace(0,2*np.pi,n_sides, endpoint=False)
    xver = radius*np.cos(theta) + centroid[0]
    yver = radius*np.sin(theta) + centroid[1]
    nver = len(xver)
    return xver, yver, nver

def make_polygon_from_edge_length(radius: float, edge_length: float, centroid: list):
    angle = np.arcsin(edge_length / (2 * radius))
    n_sides = int(np.round(np.pi / angle))

    theta = np.linspace(0, 2 * np.pi, n_sides, endpoint=False)  # exclude endpoint to avoid overlap
    xver = radius * np.cos(theta) + centroid[0]
    yver = radius * np.sin(theta) + centroid[1]

    vertices = np.column_stack((xver, yver))  # shape: (n_sides, 2)
    return vertices

def make_container(length: float, width: float, thickness: float):
    bottom = np.array([[0, length+2*thickness, length+2*thickness, 0],
                       [0, 0, thickness, thickness]])
    
    top = np.array([[0, length+2*thickness, length+2*thickness, 0],
                    [width+ thickness, width+ thickness, width + 2*thickness, width + 2*thickness]])
    
    left = np.array([[0, thickness, thickness, 0],
                     [thickness, thickness, width+thickness, width+thickness]])
    
    right = np.array([[length+thickness, length+2*thickness, length+2*thickness, length+thickness],
                      [thickness, thickness, width+thickness, width+thickness]])

    wall_xver = np.array([bottom[0], top[0], left[0], right[0]])-thickness
    wall_yver = np.array([bottom[1], top[1], left[1], right[1]])-thickness

    return np.column_stack((wall_xver, wall_yver))  # shape: (n_sides, 2)

def make_container_separate(length: float, width: float, thickness: float):
    bottom = Wall([
        [0, 0],
        [length + 2*thickness, 0],
        [length + 2*thickness, thickness],
        [0, thickness]
    ])

    top = Wall([
        [0, width + thickness],
        [length + 2*thickness, width + thickness],
        [length + 2*thickness, width + 2*thickness],
        [0, width + 2*thickness]
    ])

    left = Wall([
        [0, thickness],
        [thickness, thickness],
        [thickness, width + thickness],
        [0, width + thickness]
    ])

    right = Wall([
        [length + thickness, thickness],
        [length + 2*thickness, thickness],
        [length + 2*thickness, width + thickness],
        [length + thickness, width + thickness]
    ])

    return [bottom, top, left, right]

def generate_grid(length:float, width:float, radius:float):
    # generate grid
    dx = 2 * radius
    dy = 2 * radius

    x_vals = np.arange(0, length + dx, dx)
    y_vals = np.arange(0, width + dy, dy)
    xp, yp = np.meshgrid(x_vals, y_vals)
    return xp, yp

def generate_grid_stagger(length:float, width:float, radius:float):
    # generate grid
    dx = 2 * radius
    dy = 2 * radius

    x_vals = np.arange(0, length + dx, dx)
    y_vals = np.arange(0, width + dy, dy)
    xp , yp = np.meshgrid(x_vals, y_vals)
    xp = xp+dx/2
    return xp, yp

def generate_grid_hexagonal(length: float, width: float, radius: float):
    dx = 2 * radius
    dy = np.sqrt(3) * radius  # vertical spacing for hexagonal packing
    # dy = 2 * radius

    x_vals = np.arange(0, length + dx, dx)
    y_vals = np.arange(0, width + dy, dy)

    xp_list = []
    yp_list = []

    for i, y in enumerate(y_vals):
        # Offset every other row by dx/2
        if i % 2 == 0:
            x_row = x_vals
        else:
            x_row = x_vals + dx / 2

        # Filter x_row to keep within bounds
        x_row = x_row[x_row <= length]

        xp_list.append(x_row)
        yp_list.append(np.full_like(x_row, y))

    # Concatenate into arrays
    xp = np.concatenate(xp_list)
    yp = np.concatenate(yp_list)

    return xp, yp
