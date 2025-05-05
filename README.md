# porous_media_project

## Author
**Gamaliel Jeevan Dewanto**

---

## Description

This project focuses on the creation, manipulation, and analysis of 2D porous geometries, with the long-term goal of enabling fluid simulation through these media.

It currently includes functionality for:
- Polygonal particle and wall generation
- Basic DEM-style setup with gravity and motion
- Modular and extensible code structure using Python OOP

---

## Structure

- `geometry.py` — functions to generate particles and container walls
- `entities.py` — class definitions for `Particle`, `Wall`, and `RigidBody2D`
- `physics.py` — (planned) motion integration and collision physics
- `dr_*.py` — driver scripts to test and run different setups

---

## Requirements

- Python 3.8+
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
