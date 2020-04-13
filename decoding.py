import numpy


def get_range_decoding(probability, tag, lower_bound=0, upper_bound=1):

    # elements = list(probability.keys())
    number = len(probability)
    LR = [lower_bound]
    UR = []
    d = upper_bound - lower_bound
    for i in range(1, number):
        x = LR[i-1] + d*(probability[i-1])
        LR.append(x)
        UR.append(x)
        if LR[i-1] <= tag <= UR[i-1]:
            return i-1, [LR[i-1], UR[i-1]]
    UR.append(upper_bound)
    if not LR[number - 1] <= tag <= UR[number - 1]:
        print("DECODING ERROR DETECTED")
    return number-1, [LR[number-1], UR[number-1]]


def decoding(probability, tag, number):
    (element, x) = get_range_decoding(probability, tag)
    for i in range(1, number):
        (y, x) = get_range_decoding(probability, tag, x[0], x[1])
        element = numpy.append(element,y)
    return element

