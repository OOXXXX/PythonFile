import numpy as np


def EuclideanDistance(dataA, dataB):
    # np.linalg.norm 用于范数计算，默认是二范数，相当于平方和开根号
    return 1.0/(1.0 + np.linalg.norm(dataA - dataB))
