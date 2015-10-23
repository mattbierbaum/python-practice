import numpy as np

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
        num_intersects : int
            how many intersections these two objects have

        intersection : array_like
            A list of the intersections for the line with the circle,
            Can be as large as [2,2] and small as empty.  If no intersections,
            will return empty list.  Two intersections will be returned
            in the form [[x1, y1], [x2, y2]]

    Note: since this is example code, I will not be respecting floating-point
          issues introduced by loss of significance by quadratic formula
          (see https://en.wikipedia.org/wiki/Loss_of_significance)
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
        return 0, []

    elif np.allclose(dsc, np.finfo(float).eps):
        x0 = D*dy/dr2
        y0 = -D*dx/dr2
        return 1, np.array([x0, y0])

    else:
        x0 = (D*dy + np.sign(dy)*dx*np.sqrt(dsc)) / dr2
        y0 = (-D*dx + np.abs(dy)*np.sqrt(dsc))/dr2

        x1 = (D*dy - np.sign(dy)*dx*np.sqrt(dsc)) / dr2
        y1 = (-D*dx - np.abs(dy)*np.sqrt(dsc))/dr2

        return 2, np.array([[x0, y0], [x1, y1]])
