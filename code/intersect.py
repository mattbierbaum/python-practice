import numpy as np

def sgn(a):
    """
    Return the sign of the argument (in contrast to np.sign)
        -1 if a < 0
        +1 if a >= 0
        
    Parameters:
    -----------
        a : int, float
            the argument to check
    
    Examples:
    
    >>> sgn(-1)
    -1.0
    
    >>> sgn(0)
    1.0

    >>> sgn(1e9)
    1.0
    """
    return -1.0*(a < 0) + 1.0*(a >= 0)

def intersection_line_circle(pt0, pt1, radius):
    """
    Find the intersection between line defined by points pt0 and pt1
    and a circle of size radius at the origin (0,0) given by quadratic
    solution (see http://mathworld.wolfram.com/Circle-LineIntersection.html).
    
    Parameters:
    -----------
        pt0 : array_like -> [2]
            Beginning point for line of the form [x,y]

        pt1 : array_like -> [2]
            End point for line of the form [x,y]

        radius : float
            The radius of the circle at the origin (0,0) to intersect

    Returns:
    --------
        intersection : array_like
            A list of the intersections for the line with the circle,
            Can be as large as [2,2] and small as empty.  If no intersections,
            will return empty list.  Two intersections will be returned
            in the form [[x1, y1], [x2, y2]]

    Note: since this is example code, I will not be respecting floating-point
          issues introduced by loss of significance by quadratic formula
          (see https://en.wikipedia.org/wiki/Loss_of_significance)

    Examples:

    >>> intersection_line_circle([1.0, 0.0], [1.0, 1.0], 0.5)
    array([], dtype=float64)

    >>> intersection_line_circle([1.0, 0.0], [1.0, 1.0], 1-1e-14)
    array([], dtype=float64)

    >>> intersection_line_circle([0.5, 0.5], [0.0, 0.5], 0.5)
    array([[ 0. ,  0.5]])

    >>> intersection_line_circle([0.0, 1.0], [1.0, 0.0], np.sqrt(2)/2)
    array([[ 0.5,  0.5]])

    >>> intersection_line_circle([0.1, 0.0], [1.0, 0.0], 1)
    array([[ 1.,  0.],
           [-1., -0.]])

    >>> intersection_line_circle([0.0, 0.0], [0.0, 1.0], 1)
    array([[ 0.,  1.],
           [ 0., -1.]])

    >>> intersection_line_circle([0.0, 0.0], [1.0, 1.0], 1)
    array([[ 0.70710678,  0.70710678],
           [-0.70710678, -0.70710678]])
    """

    # convert to ndarray if not already
    if not isinstance(pt0, np.ndarray):
        pt0 = np.array(pt0).astype('float')
    if not isinstance(pt1, np.ndarray):
        pt1 = np.array(pt1).astype('float')

    # get the differences between positions
    dx,dy = pt1 - pt0

    # calculate parts of the formula given by the reference
    r2 = radius*radius
    dr2 = dx*dx + dy*dy
    D = np.cross(pt0, pt1)

    # calculate the descriminant telling how many intersections
    dsc = r2*dr2 - D*D

    # if the descriminant is less than zero, return appropriate nothings
    if dsc < 0:
        return np.array([])

    elif np.allclose(dsc, np.finfo(float).eps):
        x0 = D*dy/dr2
        y0 = -D*dx/dr2
        return np.array([[x0, y0]])

    else:
        x0 = (D*dy + sgn(dy)*dx*np.sqrt(dsc)) / dr2
        y0 = (-D*dx + np.abs(dy)*np.sqrt(dsc))/dr2

        x1 = (D*dy - sgn(dy)*dx*np.sqrt(dsc)) / dr2
        y1 = (-D*dx - np.abs(dy)*np.sqrt(dsc))/dr2

        return np.array([[x0, y0], [x1, y1]])
