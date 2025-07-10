import numpy as np
from math import degrees, radians


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

    return F_magnitude * r * np.sin(radians(F_direction))


def calculate_moment_of_inertia(m, r):
    """
    Returns the moment of inertia of an object

    Moment of Inertia = sum for each particle of mass * distance from axis of rotation squared

    Params
    - m: kg, mass of the object
    - r: meters, distance from the axis of rotation
    """
    return m * (r**2)


def calculate_auv_acceleration(F_magnitude, F_angle, mass=100):
    """
    Returns the acceleration in meters per second squared of an AUV with a thruster that can rotate +- 30 degrees

    Params
    - F_magnitude: Newtons, magnitude of the force applied by the thruster
    - F_angle: radians, the direction of the force applied by the thruster
    - mass: kg, mass of the AUV, default is 100kg
    """

    return -F_magnitude * np.array([np.cos(F_angle) / mass, np.sin(F_angle) / mass])


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """
    Returns the angular acceleration in radians per second sqaured of an AUV with a thruster that can rotate +- 30 degrees

    Params
    - F_magnitude: Newtons, the magnitude of the force applied by the thruster
    - F_angle: radians, the direction of the force applied by the thruster
    - inertia: kg*m^2, the moment of inertia, default is 1 kg*m^2
    - thruster_distance: meters, the distance fom the thruster to the center of mass, default is 0.5m
    """

    return calculate_angular_acceleration(
        calculate_torque(F_magnitude, degrees(F_angle), thruster_distance), inertia
    )


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """
    Returns the acceleration in meters per second squared of the 4 thruster AUV

    Params
    - T: np.ndarray of Newtons, magnitudes of the forces applied by the thrusters
    - alpha: radians, angle of the thrusters
    - theta: radians, the angle of the AUV
    - mass: kg, the mass of the AUV, default is 100kg
    """

    T1 = theta + alpha
    T2 = theta - alpha
    T3 = theta + np.pi + alpha
    T4 = theta + np.pi - alpha

    acceleration1 = calculate_auv_acceleration(T[0], T1, mass)
    acceleration2 = calculate_auv_acceleration(T[1], T2, mass)
    acceleration3 = calculate_auv_acceleration(T[2], T3, mass)
    acceleration4 = calculate_auv_acceleration(T[3], T4, mass)

    return acceleration1 + acceleration2 + acceleration3 + acceleration4


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """
    Returns the angular acceleration in radians per second squared of the 4 thruster AUV

    Params
    - T: np.ndarray of Newtons, magnitudes of the forces applied by the thrusters
    - alpha: radians, angle of the thrusters
    - L: distance from the center of mass to the thruster
    - l: duplicate of L
    - inertia: kg*m^2, moment of inertia of the AUV, default is 100 kg*m^2
    """

    T1 = alpha
    T2 = -alpha
    T3 = np.pi + alpha
    T4 = np.pi - alpha

    acceleration1 = calculate_auv_angular_acceleration(T[0], T1, inertia, L)
    acceleration2 = calculate_auv_angular_acceleration(T[1], T2, inertia, L)
    acceleration3 = calculate_auv_angular_acceleration(T[2], T3, inertia, L)
    acceleration4 = calculate_auv_angular_acceleration(T[3], T4, inertia, L)

    return acceleration1 + acceleration2 + acceleration3 + acceleration4
