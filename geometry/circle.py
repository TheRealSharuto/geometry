from math import pi

def calculate_area(r):
    """
    Calculates the area of a circle.

    Parameters
    ----------
    r : numerical
        The radius of a circle

    Returns
    -------
    area : numerical
        The calculated area
    """
    area = pi * r **2
    return area


def calculate_circ(r):
    """
    Calculates the circumference of a circle.

    Parameters
    ----------
    r : numerical
        The radius of a circle

    Returns
    -------
    circ : float or array
        The calculated circumference
    """
    circ = 2 * pi * r
    return circ