def get_range(probability, element, lower_bound=0, upper_bound=1):

    # elements = list(probability.keys())
    number = len(probability)
    LR = [lower_bound]
    UR = []
    # range of symbol = lower limit : lower limit + (upper bound - lower bound) * P[symbol]
    # lower ranges: LR = [ lower bound,...., LR[i-1] + d(P[i-1]) ]
    d = upper_bound - lower_bound
    for i in range(1, number):
        x = LR[i-1] + d*(probability[i-1])
        LR.append(x)
        UR.append(x)
    UR.append(upper_bound)

    return [LR[element], UR[element]]


def encoding(probability, sequence):
    x = get_range(probability, sequence[0])

    for i in range(1, len(sequence)):
        x = get_range(probability, sequence[i], x[0], x[1])
    return (x[0] + x[1]) / 2