# -*- coding: utf-8 -*-
""" A module containing simplification functions.
    A work in progress.

By Samuel Londner

TODO:
    * For module TODOs
    * Add functions

"""

import shapely.geometry

def simplify_pts(pts, max_pts_number, max_tolerance, keep_bigger = False):
    """Simplifies a polygon to a given number of points.

    Args:
        pts (double): A Nx2 array containing the points of the polygon.
        max_pts_number (int): The required number of points.
        max_tolerance (double): The maximum allowed error.
        keep_bigger (bool, optional): If True the returned polygon will contain the original polygon.


    Returns:
        simplified_pts: A pts_numberx2 array containing the points of the simplified polygon.

    Notes:
        The algorithm used is an iterative Douglas-Peucker simplification.
        If the `keep_bigger` flag is `True`, the simplification is preceded by buffering.
        If the algorithm fails to converge it issues an error.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """

    #TODO: validate input
    #TODO: returns final error
    #TODO: make output format like input
    #TODO: correct doc (from "array" to list/NumPy array)
    
    poly0 = shapely.geometry.Polygon(pts)
    initial_tolerance = max_tolerance/10
    max_steps_number = 90
    tolerance_step = (max_tolerance-initial_tolerance)/max_steps_number

    steps_number = 1
    tolerance = initial_tolerance
    simplified_pts_number = len(poly0.exterior.coords)

    while tolerance > max_tolerance or simplified_pts_number > max_pts_number:
        if steps_number > max_steps_number:
            raise Exception('simplify_pts: The algorithm could not converge. Use more points or increase tolerance.')
        if keep_bigger:
            buffered_poly = poly0.buffer(tolerance)
        else:
            buffered_poly = poly0
        simplified_poly = buffered_poly.simplify(tolerance, preserve_topology=False)
        simplified_pts_number = len(simplified_poly.exterior.coords)
        tolerance = tolerance + tolerance_step
    
    x,y = simplified_poly.exterior.xy
    return list(zip(x,y))
        
