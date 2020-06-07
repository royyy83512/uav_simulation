# -*- coding: UTF-8 -*-
"""
uav_math package includes geometries such as shapes, lines and points
"""


def dis(a, b):
    """
    return distance between pointA and pointB
    """
    dx = b[0]-a[0]
    dy = b[1]-a[1]
    return (dx**2 + dy**2)**0.5


def vector(a, b):
    """
    return vector form pointA to pointB
    """
    return b[0]-a[0], b[1]-a[1]


def vector_product(vector_a, vector_b):
    """
    return vector product between vectorA and vectorB
    """
    return vector_a[0]*vector_b[1] - vector_b[0]*vector_a[1]


def vector_dot(vector_a, vector_b):
    """
    return vector dot between vectorA and vectorB
    """
    return vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]


def unit_vector(a, b):
    """
    return unit vector between pointA and pointB
    """
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    distance = (dx**2 + dy**2)**0.5
    if distance == 0:
        distance = 0.1
    return [dx/distance, dy/distance]


def displacement(a, b, vel):
    """
    return displacement vector
    """
    return [unit_vector(a, b)[0] * vel, unit_vector(a, b)[1] * vel]


def is_intersected(a, b, c, d):
    """
    return whether is intersected between line(a,b) and line(c,d)
    """
    zero = 1e-9
    a_c = vector(a, c)
    a_d = vector(a, d)
    b_c = vector(b, c)
    b_d = vector(b, d)
    return (vector_product(a_c, a_d) * vector_product(b_c, b_d) <= zero) and (
                vector_product(a_c, b_c) * vector_product(a_d, b_d) <= zero)

# end of file
