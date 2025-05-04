# porosity.py

from shapely.ops import unary_union

def compute_porosity(domain, particles):
    total_area = domain.area
    solid_area = unary_union(particles).area
    porosity = 1.0 - solid_area / total_area
    return porosity
