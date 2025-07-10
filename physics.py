import numpy as np


def calculate_buoyancy(V, density_fluid):
    """
    Calculates and returns the buoyancy force on an object in newtons
    F_b = density * volume * gravitational acceleration

    Params
    - V: m^3, volume
    - density_fluid: kg/m^3, density of the fluid
    """

    return density_fluid * V * 9.81


def will_it_float(V, mass):
    """
    Returns a boolean regarding whether or not an object will sink or float in water

    Params
    - V: m^3, volume
    - mass: kg, mass of the object

    Assuming that the density of water is 1000 kg/m^3
    """

    return mass / V >= 1


def calculate_pressure(depth):
    """
    Calculates the pressure at a depth in water in pascals
    Pressure = density * gravitational acceleration * depth

    Params
    - depth: meters, depth in the water
    """

    return 1000 * 9.81 * depth


def calculate_acceleration(F, m):
    """
    Calculates the acceleration of an object
    F = ma

    Params
    - F: newtons, force on the object
    - m: kg, mass of the object
    """

    return F / m


def calculate_angular_acceleration(tau, I):
    """
    Returns the angular acceleration of an object given torque and moment of inertia
    Torque = moment of inertia * angular acceleration

    Params
    - tau: Newton-meters, torque on the object
    - I: kg * m^2, moment of inertia of the object
    """

    return tau / I


def calculate_torque(F_magnitude, F_direction, r):
    """
    Returns the calculated torque

    Torque = distance from axis of rotation * force

    Params
    - F_magnitude: magnitude of the force on the object
    - F_direction: direction of the force on the object in degrees
    - r: distance of the object from the axis of rotation
    """

    return F_magnitude * r * np.sin(F_direction * np.pi / 180)


def calculate_moment_of_inertia(m, r):
    """
    Returns the moment of inertia of an object

    Moment of Inertia = sum for each particle of mass * distance from axis of rotation squared

    Params
    - m: kg, mass of the object
    - r: meters, distance from the axis of rotation
    """
    return m * (r**2)


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    """
    Returns the acceleration in radians per second squared of an AUV with a 100N thruster

    Params
    - F_magnitude: Newtons, magnitude of the force applied to the AUV
    - F_angle: radians, the direction of the force applied to the AUV
    - mass: kg, mass of the AUV, default is 100kg
    - volume: m^3, volume of the AUV, default is 0.1m^3
    - thruster_distance: meters, distance from the center of mass of the AUV to thruster, default is 0.5m
    """
