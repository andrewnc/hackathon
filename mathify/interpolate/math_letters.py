import numpy as np

"""Each character is drawn as if it was at the first character (0,0), shift will take care of all necessary modifications."""

def scale_coords(coords, x_scale, y_scale):
    np_coords = np.array(coords, dtype="float64")
    np_coords[:,::2] = np_coords[:,::2]*x_scale
    np_coords[:,1::2] = np_coords[:,1::2]*y_scale
    final_x = np.max(np_coords[:,::2])
    final_y = np.max(np_coords[:,1::2])
    return np_coords.tolist(), final_x, final_y

def shift_coords(x_shift, y_shift, coords):
    """Recall that coords are set up in this format: [x1,y1,x2,y2,x3,y3,x4,y4]"""
    for points in coords:
        points[0] += x_shift
        points[2] += x_shift
        points[4] += x_shift
        points[6] += x_shift

        points[1] += y_shift
        points[3] += y_shift
        points[5] += y_shift
        points[7] += y_shift
    return coords

def write_latex(x1,y1,x2,y2,x3,y3,x4,y4):
    return "\\\\left(\\\\left(" + str(x1) + "\\\\left(1-t\\\\right)^3+3*" + str(x2) + "\\\\left(1-t\\\\right)^2t+3*" + str(x3) + "\\\\left(1-t\\\\right)t^2+" + str(x4) + "t^3\\\\right),\\\\ " + str(y1) + "\\\\left(1-t\\\\right)^3+3*" + str(y2) + "\\\\left(1-t\\\\right)^2t+3*" + str(y3) + "\\\\left(1-t\\\\right)t^2+" + str(y4) + "t^3\\\\right)"

def template_letter(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[],[],[],[],[],[]]
    #T was extra special, it needs to be scaled up to 600/700
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    li = []
    for a in coords:
        if len(a) == 8:
            li.append(write_latex(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
        else:
            continue
    return li, final_x, final_y

def char(c, x_shift, y_shift=0):
    """NOTE: When building characters make sure that the coordinates are set up
    to have [x1,y1,x2,y2,x3,y3,x4,y4]
    Parameters:
    c (str): The character to be drawn
    x_shift (int): the amount of horizontal shift needed.
    y_shift (int): The amount of vertical shift needed.
    """
    if c == 'T':
        return T(x_shift, y_shift)
    else:
        return None, x_shift, y_shift

def A(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,260,700,0,0,260,700],[260,700,380,700,260,700,380,700],[380,700,635,0,380,700,635,0],[635,0,530,0,635,0,530,0],[],[]]
    #T was extra special, it needs to be scaled up to 600/700
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    li = []
    for a in coords:
        if len(a) == 8:
            li.append(write_latex(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
        else:
            continue
    return li, final_x, final_y

def T(x_shift=0, y_shift=0, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one."""
    coords = [[237,620,237,620,237,120,237,120],[237,120,237,35,226,24,143,19],[143,19,143,19,143,0,143,0],[143,0,143,0,435,0,435,0],[435,0,435,0,435,19,435,19],[435,19,353,23,339,36,339,109],[339,109,339,108,339,620,339,620],[339,620,339,620,393,620,393,620],[393,620,507,620,529,602,552,492],[552,492,552,492,576,492,576,492],[576,492,576,492,570,662,570,662],[570,662,570,662,6,662,6,662],[6,662,6,662,0,492,0,492],[0,492,0,492,24,492,24,492],[24,492,48,602,71,620,183,620],[183,620,183,620,237,620,237,620]]
    #T was extra special, it needs to be scaled up to 600/700
    coords, final_x, final_y = scale_coords(coords, 1.041666, 1.0574018)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    li = []
    for a in coords:
        if len(a) == 8:
            li.append(write_latex(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
        else:
            continue
    return li, final_x, final_y
