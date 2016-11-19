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

def write_letter(coords, final_x, final_y):
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
    if c == 'A':
        return A(x_shift, y_shift)
    elif c == 'B':
        return B(x_shift, y_shift)
    elif c == 'C':
        return C(x_shift, y_shift)
    elif c == 'D':
        return D(x_shift, y_shift)
    elif c == 'E':
        return E(x_shift, y_shift)
    elif c == 'F':
        return F(x_shift, y_shift)
    elif c == 'G':
        return G(x_shift, y_shift)
    elif c == 'H':
        return H(x_shift, y_shift)
    elif c == 'I':
        return I(x_shift, y_shift)
    elif c == 'J':
        return J(x_shift, y_shift)
    elif c == 'K':
        return K(x_shift, y_shift)
    elif c == 'L':
        return L(x_shift, y_shift)
    elif c == 'M':
        return M(x_shift, y_shift)
    elif c == 'N':
        return N(x_shift, y_shift)
    elif c == 'O':
        return O(x_shift, y_shift)
    elif c == 'P':
        return P(x_shift, y_shift)
    elif c == 'Q':
        return Q(x_shift, y_shift)
    elif c == 'R':
        return R(x_shift, y_shift)
    elif c == 'S':
        return S(x_shift, y_shift)
    elif c == 'T':
        return T(x_shift, y_shift)
    elif c == 'U':
        return U(x_shift, y_shift)
    elif c == 'V':
        return V(x_shift, y_shift)
    elif c == 'W':
        return W(x_shift, y_shift)
    elif c == 'X':
        return X(x_shift, y_shift)
    elif c == 'Y':
        return Y(x_shift, y_shift)
    elif c == 'Z':
        return Z(x_shift, y_shift)
    else:
        return None, x_shift, y_shift

def template_letter(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def A(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,260,700,0,0,260,700],[260,700,380,700,260,700,380,700],[380,700,635,0,380,700,635,0],[635,0,535,0,635,0,535,0],[535,0,455,200,535,0,455,200],[455,200,175,200,455,200,175,200],[175,200,100,0,175,200,100,0],[100,0,0,0,100,0,0,0],[211,300,322,600,211,300,322,600],[322,600,433,300,322,600,433,300],[211,300,422,300,211,300,422,300]]
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def B(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[35.28225806451616, 0.2604166666666856, 35.28225806451616, 449.99999999999994, 35.28225806451616, 3.1250000000000284, 35.28225806451616, 449.99999999999994], [35.28225806451616, 449.99999999999994, 188.3064516129033, 449.99999999999994, 39.7177419354839, 452.8645833333333, 186.0887096774194, 449.99999999999994], [186.0887096774194, 449.99999999999994, 245.9677419354839, 432.81249999999994, 186.0887096774194, 449.99999999999994, 248.1854838709678, 435.6770833333333], [248.1854838709678, 435.6770833333333, 290.32258064516134, 366.9270833333333, 257.0564516129033, 429.9479166666667, 290.32258064516134, 378.3854166666667], [290.32258064516134, 375.5208333333333, 281.45161290322585, 280.9895833333333, 292.54032258064524, 361.1979166666667, 277.01612903225816, 283.8541666666667], [277.01612903225816, 283.8541666666667, 245.9677419354839, 246.61458333333331, 281.45161290322585, 280.9895833333333, 245.9677419354839, 240.88541666666669], [245.9677419354839, 240.88541666666669, 301.4112903225807, 183.59375, 245.9677419354839, 243.75, 296.9758064516129, 197.91666666666669], [299.1935483870968, 192.1875, 308.0645161290323, 152.08333333333337, 299.1935483870968, 192.1875, 308.0645161290323, 154.94791666666669], [308.0645161290323, 149.21875, 308.0645161290323, 103.38541666666669, 312.5, 137.76041666666669, 305.8467741935484, 97.65625], [305.8467741935484, 97.65625, 283.66935483870975, 43.229166666666686, 303.6290322580645, 86.19791666666669, 281.45161290322585, 43.229166666666686], [281.45161290322585, 43.229166666666686, 239.3145161290323, 5.989583333333371, 290.32258064516134, 57.55208333333337, 250.4032258064517, 14.583333333333371], [250.4032258064517, 14.583333333333371, 197.17741935483878, -5.468749999999972, 252.6209677419355, 14.583333333333371, 210.483870967742, -2.6041666666666288], [210.483870967742, -2.6041666666666288, 37.50000000000006, -2.6041666666666288, 188.3064516129033, -5.468749999999972, 35.28225806451616, -5.468749999999972], [84.07258064516134, 258.0729166666667, 84.07258064516134, 395.5729166666667, 84.07258064516134, 266.6666666666667, 84.07258064516134, 395.5729166666667], [84.07258064516134, 395.5729166666667, 183.87096774193554, 401.3020833333333, 81.85483870967744, 407.03124999999994, 192.74193548387103, 398.43749999999994], [192.74193548387103, 398.43749999999994, 221.57258064516134, 386.9791666666667, 188.3064516129033, 407.03124999999994, 226.00806451612908, 378.3854166666667], [226.00806451612908, 378.3854166666667, 237.0967741935484, 312.50000000000006, 237.0967741935484, 378.3854166666667, 241.5322580645162, 321.09374999999994], [241.5322580645162, 321.09374999999994, 217.1370967741936, 275.2604166666667, 234.8790322580645, 298.1770833333333, 214.91935483870975, 266.6666666666667], [214.91935483870975, 266.6666666666667, 170.5645161290323, 266.6666666666667, 214.91935483870975, 272.3958333333333, 172.78225806451616, 260.9375], [172.78225806451616, 260.9375, 81.85483870967744, 263.8020833333333, 170.5645161290323, 260.9375, 84.07258064516134, 258.0729166666667], [84.07258064516134, 46.09375, 84.07258064516134, 209.375, 81.85483870967744, 54.6875, 84.07258064516134, 212.23958333333337], [84.07258064516134, 206.51041666666669, 177.2177419354839, 209.375, 86.29032258064518, 209.375, 183.87096774193554, 212.23958333333337], [183.87096774193554, 212.23958333333337, 221.57258064516134, 200.78125, 192.74193548387103, 212.23958333333337, 223.79032258064518, 197.91666666666669], [223.79032258064518, 197.91666666666669, 252.6209677419355, 169.27083333333337, 228.22580645161293, 206.51041666666669, 257.0564516129033, 160.67708333333337], [257.0564516129033, 160.67708333333337, 248.1854838709678, 80.46875, 261.491935483871, 132.03125, 250.4032258064517, 86.19791666666669], [250.4032258064517, 86.19791666666669, 210.483870967742, 46.09375, 243.75, 80.46875, 210.483870967742, 54.6875], [210.483870967742, 54.6875, 132.86290322580652, 54.6875, 206.04838709677426, 51.822916666666686, 141.733870967742, 51.822916666666686], [141.733870967742, 51.822916666666686, 84.07258064516134, 48.95833333333337, 150.60483870967744, 48.95833333333337, 86.29032258064518, 48.95833333333337]]
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def C(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[576.4112903225807, 329.68749999999994, 571.9758064516129, 298.1770833333333, 576.4112903225807, 329.68749999999994, 571.9758064516129, 301.0416666666667], [571.9758064516129, 301.0416666666667, 563.1048387096774, 266.6666666666667, 569.7580645161291, 298.1770833333333, 563.1048387096774, 269.53125], [563.1048387096774, 269.53125, 549.7983870967743, 223.69791666666669, 563.1048387096774, 266.6666666666667, 552.0161290322582, 226.5625], [552.0161290322582, 226.5625, 529.8387096774194, 177.86458333333337, 549.7983870967743, 223.69791666666669, 525.4032258064517, 169.27083333333337], [525.4032258064517, 169.27083333333337, 483.26612903225816, 117.70833333333337, 514.3145161290323, 157.8125, 478.83064516129036, 120.57291666666669], [478.83064516129036, 120.57291666666669, 412.29838709677426, 89.0625, 476.61290322580646, 117.70833333333337, 410.08064516129036, 91.92708333333337], [410.08064516129036, 91.92708333333337, 328.0241935483872, 86.19791666666669, 392.3387096774194, 86.19791666666669, 330.241935483871, 86.19791666666669], [330.241935483871, 86.19791666666669, 248.1854838709678, 123.4375, 321.3709677419355, 91.92708333333337, 245.9677419354839, 126.30208333333337], [245.9677419354839, 126.30208333333337, 197.17741935483878, 177.86458333333337, 241.5322580645162, 129.16666666666669, 194.95967741935488, 180.72916666666669], [194.95967741935488, 180.72916666666669, 168.3467741935484, 249.47916666666669, 190.52419354838713, 203.64583333333337, 166.12903225806457, 258.0729166666667], [166.12903225806457, 258.0729166666667, 148.3870967741936, 344.0104166666667, 161.69354838709683, 272.3958333333333, 146.16935483870975, 341.1458333333333], [146.16935483870975, 341.1458333333333, 163.91129032258067, 278.12500000000006, 146.16935483870975, 341.1458333333333, 159.47580645161293, 283.8541666666667], [146.16935483870975, 344.0104166666667, 141.733870967742, 441.40624999999994, 146.16935483870975, 366.9270833333333, 139.5161290322581, 470.0520833333333], [139.5161290322581, 470.0520833333333, 146.16935483870975, 544.53125, 141.733870967742, 464.3229166666667, 148.3870967741936, 553.125], [148.3870967741936, 553.125, 166.12903225806457, 647.65625, 143.95161290322585, 533.0729166666667, 168.3467741935484, 639.0625], [166.12903225806457, 639.0625, 199.39516129032262, 719.2708333333333, 159.47580645161293, 624.7395833333333, 190.52419354838713, 704.9479166666665], [190.52419354838713, 704.9479166666665, 226.00806451612908, 759.375, 192.74193548387103, 710.6770833333333, 228.22580645161293, 765.1041666666665], [228.22580645161293, 765.1041666666665, 292.54032258064524, 808.0729166666665, 243.75, 776.5625, 294.758064516129, 805.2083333333333], [294.758064516129, 805.2083333333333, 367.9435483870968, 825.2604166666665, 294.758064516129, 810.9375, 376.8145161290323, 830.9895833333333], [376.8145161290323, 830.9895833333333, 447.7822580645162, 813.8020833333333, 374.5967741935484, 830.9895833333333, 458.8709677419355, 805.2083333333333], [461.0887096774194, 808.0729166666665, 512.0967741935484, 770.8333333333333, 461.0887096774194, 808.0729166666665, 507.6612903225807, 776.5625], [507.6612903225807, 776.5625, 536.491935483871, 727.8645833333333, 509.8790322580645, 765.1041666666665, 540.9274193548388, 725.0], [540.9274193548388, 725.0, 556.4516129032259, 679.1666666666665, 538.7096774193549, 722.1354166666665, 556.4516129032259, 684.8958333333333], [556.4516129032259, 684.8958333333333, 567.5403225806452, 641.9270833333333, 556.4516129032259, 679.1666666666665, 569.7580645161291, 639.0625], [569.7580645161291, 639.0625, 662.9032258064517, 636.1979166666667, 571.9758064516129, 636.1979166666667, 662.9032258064517, 639.0625], [665.1209677419355, 636.1979166666667, 645.1612903225807, 722.1354166666665, 662.9032258064517, 636.1979166666667, 649.5967741935484, 716.40625], [649.5967741935484, 716.40625, 611.8951612903227, 802.34375, 642.9435483870968, 736.4583333333333, 594.1532258064517, 819.53125], [594.1532258064517, 819.53125, 538.7096774193549, 885.4166666666665, 587.5, 833.8541666666665, 540.9274193548388, 882.5520833333333], [540.9274193548388, 882.5520833333333, 463.3064516129033, 922.6562499999998, 538.7096774193549, 882.5520833333333, 476.61290322580646, 919.7916666666665], [476.61290322580646, 919.7916666666665, 401.2096774193549, 931.2499999999998, 465.5241935483872, 919.7916666666665, 403.4274193548388, 931.2499999999998], [403.4274193548388, 931.2499999999998, 316.9354838709678, 931.2499999999998, 390.1209677419355, 931.2499999999998, 319.1532258064517, 931.2499999999998], [319.1532258064517, 931.2499999999998, 241.5322580645162, 908.3333333333333, 308.0645161290323, 928.3854166666665, 252.6209677419355, 911.1979166666665], [252.6209677419355, 911.1979166666665, 194.95967741935488, 873.9583333333333, 237.0967741935484, 899.7395833333333, 199.39516129032262, 873.9583333333333], [199.39516129032262, 873.9583333333333, 126.20967741935488, 793.75, 199.39516129032262, 873.9583333333333, 135.08064516129036, 805.2083333333333], [135.08064516129036, 805.2083333333333, 84.07258064516134, 730.7291666666665, 123.99193548387103, 793.75, 84.07258064516134, 725.0], [84.07258064516134, 725.0, 57.459677419354875, 656.25, 81.85483870967744, 716.40625, 61.89516129032262, 644.7916666666667], [61.89516129032262, 644.7916666666667, 44.153225806451644, 544.53125, 59.677419354838776, 624.7395833333333, 46.370967741935544, 547.3958333333333], [46.370967741935544, 547.3958333333333, 41.9354838709678, 452.8645833333333, 44.153225806451644, 544.53125, 44.153225806451644, 447.1354166666667], [44.153225806451644, 447.1354166666667, 48.58870967741939, 364.06249999999994, 39.7177419354839, 444.2708333333333, 44.153225806451644, 352.6041666666667], [44.153225806451644, 352.6041666666667, 61.89516129032262, 263.8020833333333, 48.58870967741939, 355.46874999999994, 64.11290322580652, 269.53125], [64.11290322580652, 269.53125, 90.72580645161293, 177.86458333333337, 59.677419354838776, 255.20833333333331, 97.37903225806457, 154.94791666666669], [97.37903225806457, 154.94791666666669, 146.16935483870975, 80.46875, 97.37903225806457, 154.94791666666669, 146.16935483870975, 80.46875], [146.16935483870975, 80.46875, 201.61290322580652, 17.447916666666686, 143.95161290322585, 77.60416666666669, 199.39516129032262, 23.17708333333337], [199.39516129032262, 23.17708333333337, 263.7096774193549, -16.927083333333286, 206.04838709677426, 17.447916666666686, 281.45161290322585, -19.79166666666663], [281.45161290322585, -19.79166666666663, 359.07258064516134, -34.114583333333286, 292.54032258064524, -19.79166666666663, 372.3790322580645, -34.114583333333286], [372.3790322580645, -34.114583333333286, 472.1774193548388, -2.6041666666666288, 383.4677419354839, -28.38541666666663, 476.61290322580646, 0.2604166666666856], [476.61290322580646, 0.2604166666666856, 538.7096774193549, 43.229166666666686, 487.70161290322585, 5.989583333333371, 556.4516129032259, 48.95833333333337], [556.4516129032259, 48.95833333333337, 609.6774193548388, 120.57291666666669, 571.9758064516129, 63.28125, 614.1129032258065, 120.57291666666669], [614.1129032258065, 120.57291666666669, 642.9435483870968, 180.72916666666669, 611.8951612903227, 120.57291666666669, 642.9435483870968, 189.32291666666669], [642.9435483870968, 189.32291666666669, 656.25, 243.75, 638.5080645161291, 186.45833333333337, 658.4677419354839, 246.61458333333331], [656.25, 243.75, 671.7741935483872, 329.68749999999994, 656.25, 240.88541666666669, 669.5564516129033, 326.8229166666667], [669.5564516129033, 326.8229166666667, 576.4112903225807, 326.8229166666667, 667.3387096774194, 332.5520833333333, 578.6290322580645, 332.5520833333333]]
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    print final_x, final_y

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def D(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[79.6370967741936, -2.6041666666666288, 75.20161290322585, 911.1979166666665, 79.6370967741936, -5.468749999999972, 75.20161290322585, 914.0624999999998], [75.20161290322585, 914.0624999999998, 330.241935483871, 911.1979166666665, 81.85483870967744, 911.1979166666665, 356.85483870967744, 911.1979166666665], [356.85483870967744, 911.1979166666665, 454.4354838709678, 891.1458333333333, 387.9032258064517, 905.4687499999998, 443.3467741935484, 899.7395833333333], [443.3467741935484, 899.7395833333333, 518.75, 859.6354166666665, 456.6532258064517, 891.1458333333333, 520.9677419354839, 862.5], [520.9677419354839, 862.5, 583.0645161290323, 796.6145833333333, 529.8387096774194, 848.1770833333333, 591.9354838709678, 779.4270833333333], [591.9354838709678, 779.4270833333333, 638.5080645161291, 682.03125, 591.9354838709678, 776.5625, 636.2903225806452, 673.4375], [636.2903225806452, 673.4375, 654.0322580645162, 598.9583333333333, 640.7258064516129, 664.84375, 660.6854838709678, 576.0416666666667], [660.6854838709678, 576.0416666666667, 662.9032258064517, 472.9166666666667, 658.4677419354839, 558.8541666666667, 667.3387096774194, 472.9166666666667], [667.3387096774194, 472.9166666666667, 656.25, 346.87499999999994, 662.9032258064517, 438.5416666666667, 658.4677419354839, 358.3333333333333], [658.4677419354839, 358.3333333333333, 642.9435483870968, 269.53125, 658.4677419354839, 366.9270833333333, 638.5080645161291, 260.9375], [638.5080645161291, 260.9375, 603.0241935483872, 160.67708333333337, 634.0725806451613, 240.88541666666669, 607.4596774193549, 172.13541666666669], [607.4596774193549, 172.13541666666669, 574.1935483870968, 103.38541666666669, 614.1129032258065, 175.0, 574.1935483870968, 106.25], [574.1935483870968, 106.25, 534.2741935483872, 60.416666666666686, 585.2822580645162, 117.70833333333337, 534.2741935483872, 54.6875], [534.2741935483872, 54.6875, 481.04838709677426, 23.17708333333337, 527.6209677419355, 54.6875, 481.04838709677426, 17.447916666666686], [481.04838709677426, 17.447916666666686, 401.2096774193549, -2.6041666666666288, 476.61290322580646, 26.041666666666686, 407.86290322580646, -5.468749999999972], [407.86290322580646, -5.468749999999972, 81.85483870967744, -5.468749999999972, 401.2096774193549, 0.2604166666666856, 77.41935483870975, -5.468749999999972], [177.2177419354839, 103.38541666666669, 177.2177419354839, 802.34375, 175.00000000000006, 100.52083333333337, 177.2177419354839, 802.34375], [177.2177419354839, 802.34375, 374.5967741935484, 802.34375, 177.2177419354839, 799.4791666666665, 363.508064516129, 799.4791666666665], [363.508064516129, 799.4791666666665, 412.29838709677426, 790.8854166666665, 374.5967741935484, 802.34375, 416.73387096774195, 788.0208333333333], [416.73387096774195, 788.0208333333333, 452.2177419354839, 773.6979166666665, 421.16935483870975, 790.8854166666665, 456.6532258064517, 770.8333333333333], [456.6532258064517, 770.8333333333333, 496.57258064516134, 730.7291666666665, 463.3064516129033, 765.1041666666665, 501.00806451612914, 727.8645833333333], [501.00806451612914, 727.8645833333333, 532.0564516129033, 670.5729166666667, 505.4435483870968, 722.1354166666665, 527.6209677419355, 673.4375], [527.6209677419355, 673.4375, 549.7983870967743, 604.6875, 534.2741935483872, 661.9791666666667, 547.5806451612904, 610.4166666666667], [547.5806451612904, 610.4166666666667, 558.6693548387098, 555.9895833333333, 547.5806451612904, 610.4166666666667, 558.6693548387098, 558.8541666666667], [558.6693548387098, 558.8541666666667, 563.1048387096774, 470.0520833333333, 560.8870967741937, 555.9895833333333, 569.7580645161291, 444.2708333333333], [569.7580645161291, 444.2708333333333, 554.233870967742, 338.28124999999994, 560.8870967741937, 421.3541666666667, 549.7983870967743, 321.09374999999994], [549.7983870967743, 321.09374999999994, 525.4032258064517, 229.42708333333331, 549.7983870967743, 312.50000000000006, 514.3145161290323, 206.51041666666669], [514.3145161290323, 206.51041666666669, 492.13709677419365, 175.0, 518.75, 212.23958333333337, 494.35483870967744, 169.27083333333337], [494.35483870967744, 169.27083333333337, 465.5241935483872, 137.76041666666669, 489.91935483870975, 166.40625, 465.5241935483872, 140.625], [465.5241935483872, 140.625, 416.73387096774195, 114.84375, 465.5241935483872, 140.625, 412.29838709677426, 114.84375], [412.29838709677426, 114.84375, 365.7258064516129, 114.84375, 410.08064516129036, 114.84375, 367.9435483870968, 109.11458333333337], [367.9435483870968, 109.11458333333337, 175.00000000000006, 103.38541666666669, 367.9435483870968, 100.52083333333337, 177.2177419354839, 103.38541666666669]]
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def E(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,0,700,0,0,0,700],[0,700,450,700,0,700,450,700],[450,700,450,600,450,700,450,600],[450,600,100,600,450,600,100,600],[100,600,100,400,100,600,100,400],[100,400,400,400,100,400,400,400],[400,400,400,300,400,400,400,300],[400,300,100,300,400,300,100,300],[100,300,100,100,100,300,100,100],[100,100,450,100,100,100,450,100],[450,100,450,0,450,100,450,0],[450,0,0,0,450,0,0,0]]
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def F(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,0,700,0,0,0,700],[0,700,450,700,0,700,450,700],[450,700,450,600,450,700,450,600],[450,600,100,600,450,600,100,600],[100,600,100,400,100,600,100,400],[100,400,300,400,100,400,300,400],[300,400,300,300,300,400,300,300],[300,300,100,300,300,300,100,300],[100,300,100,0,100,300,100,0],[100,0,0,0,100,0,0,0]]
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def G(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def H(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,0,700,0,0,0,700],[0,700,100,700,0,700,100,700],[100,700,100,400,100,700,100,400],[100,400,450,400,100,400,450,400],[450,400,450,700,450,400,450,700],[450,700,550,700,450,700,550,700],[550,700,550,0,550,700,550,0],[550,0,450,0,550,0,450,0],[450,0,450,300,450,0,450,300],[450,300,100,300,450,300,100,300],[100,300,100,0,100,300,100,0],[100,0,0,0,100,0,0,0]]
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def I(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[0,0,0,100,0,0,0,100],[0,100,100,100,0,100,100,100],[100,100,100,600,100,100,100,600],[100,600,0,600,100,600,0,600],[0,600,0,700,0,600,0,700],[0,700,300,700,0,700,300,700],[300,700,300,600,300,700,300,600],[300,600,200,600,300,600,200,600],[200,600,200,100,200,600,200,100],[200,100,300,100,200,100,300,100],[300,100,300,0,300,100,300,0],[0,0,300,0,0,0,300,0]]
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def J(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def K(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def L(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def M(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = [[72.983870967742, -5.468749999999972, 70.7661290322581, 905.4687499999998, 72.983870967742, -2.6041666666666288, 70.7661290322581, 911.1979166666665], [70.7661290322581, 911.1979166666665, 210.483870967742, 911.1979166666665, 72.983870967742, 908.3333333333333, 208.2661290322581, 908.3333333333333], [208.2661290322581, 908.3333333333333, 412.29838709677426, 134.89583333333337, 210.483870967742, 911.1979166666665, 412.29838709677426, 137.76041666666669], [412.29838709677426, 137.76041666666669, 616.3306451612904, 902.6041666666665, 412.29838709677426, 143.48958333333337, 614.1129032258065, 908.3333333333333], [614.1129032258065, 908.3333333333333, 749.3951612903226, 908.3333333333333, 614.1129032258065, 908.3333333333333, 749.3951612903226, 908.3333333333333], [749.3951612903226, 908.3333333333333, 749.3951612903226, 0.2604166666666856, 749.3951612903226, 902.6041666666665, 749.3951612903226, 3.1250000000000284], [751.6129032258065, -5.468749999999972, 660.6854838709678, -2.6041666666666288, 749.3951612903226, -2.6041666666666288, 660.6854838709678, -5.468749999999972], [660.6854838709678, -5.468749999999972, 658.4677419354839, 762.2395833333333, 658.4677419354839, -5.468749999999972, 662.9032258064517, 762.2395833333333], [662.9032258064517, 762.2395833333333, 461.0887096774194, -5.468749999999972, 658.4677419354839, 756.5104166666665, 461.0887096774194, -5.468749999999972], [461.0887096774194, -5.468749999999972, 365.7258064516129, -2.6041666666666288, 458.8709677419355, -2.6041666666666288, 361.29032258064524, -2.6041666666666288], [361.29032258064524, -2.6041666666666288, 163.91129032258067, 765.1041666666665, 361.29032258064524, 0.2604166666666856, 163.91129032258067, 756.5104166666665], [163.91129032258067, 756.5104166666665, 166.12903225806457, -2.6041666666666288, 163.91129032258067, 762.2395833333333, 161.69354838709683, 0.2604166666666856], [161.69354838709683, 0.2604166666666856, 70.7661290322581, -2.6041666666666288, 163.91129032258067, -5.468749999999972, 70.7661290322581, -2.6041666666666288]]
    coords, final_x, final_y = scale_coords(coords, 0.893157262, 0.751677852)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)
    print final_x, final_y

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def N(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def O(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def P(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def Q(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def R(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def S(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

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

    return write_letter(coords, final_x, final_y)

def U(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def V(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def W(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def X(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def Y(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)

def Z(x_shift=None, y_shift=None, x_scale=1, y_scale=1):
    """Prepare the Latex for a T, but also return the end character so we know where so start the next one.
    Recall that it goes [x1,y1,x2,y2,x3,y3,x4,y4], so each Bezier curve is a list inside coords.
    Also that the numbers are input as integers"""
    coords = []
    #To save time, we compute the scale in a semi-obfuscated manner.
    coords, final_x, final_y = scale_coords(coords, 1, 1)
    coords, final_x, final_y = scale_coords(coords, 600./final_x, 700./final_y)
    coords, final_x, final_y = scale_coords(coords, x_scale, y_scale)

    #Scale must occur before shift.
    final_x += x_shift
    final_y += y_shift

    #TODO: Technically don't need to call this is both are 0.
    coords = shift_coords(x_shift, y_shift, coords)

    return write_letter(coords, final_x, final_y)
