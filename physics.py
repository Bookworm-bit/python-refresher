import numpy as np


def calculate_buoyancy(V, density_fluid):
    """
    Calculates and returns the buoyancy force on an object in newtons
    F_b = density * volume * gravitational acceleration

    Units
    - V: m^3
    - density_fluid: kg/m^3
    """

    return density_fluid * V * 9.81

def will_it_float(V, mass):
    