import numpy as np

def intersection_line_circle(line, circle):
    """
    Find the intersection between line and circle using standard quadratic
    solution (see http://mathworld.wolfram.com/Circle-LineIntersection.html).
    Applies to a single line and single circle as well as a collection. If
    either is a collection then the full comparison of all objects is performed.
    
    Parameters:
    -----------
        line : array_like -> [2,2] or [M,2,2]
            A single line or collection of lines described by [[x1, y1], [x2, y2]]
            points where (x1,y1) and (x2,y2) lay along the line

        circle : array_like -> [3] or [N,3]
            A single circle or collection of circles described by [x, y, r]

    Returns:
    --------
        num_intersects : array_like -> [M,N]
            how many intersections with each M lines with N circles

        intersection : array_like -> [M, N, 2, 2]
            A list of the intersections for each of M lines with N circles.
            Since there are two possible intersections with 2 coordinates
            each, we return 2,2 array on the last axis.  The number of
            intersections is given by num_intersects
    """
    if not isinstance(line, np.ndarray):
        line = np.array(line)
    if not isinstance(circle, np.ndarray):
        circle = np.array(circle)

    cx, cy = 
    x = line[...,
    dx,dy = line[...,

