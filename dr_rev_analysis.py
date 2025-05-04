# run_rev_analysis.py

import matplotlib.pyplot as plt
from src.geometry.generator import generate_polygon_pack
from src.analysis.porosity import compute_porosity

# Generate geometry
domain, particles = generate_polygon_pack(domain_size=(100, 100), n_particles=50)

# # Analyze
# porosity = compute_porosity(domain, particles)
# print(f"Porosity: {porosity:.3f}")

# Visualize
for poly in particles:
    x, y = poly.exterior.xy
    plt.plot(x, y, 'k-')
plt.gca().set_aspect('equal')
# plt.title(f"Generated Geometry (Porosity: {porosity:.2f})")
plt.show()
