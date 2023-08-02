import math
import numpy as np

# task 1A
fA = np.array([[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]])

# task 1B
fB = np.array(
    [
        [5, 13, 19, 14, 42, 49, 46, 67, 64, 32, 12, 4],
        [8, 17, 28, 39, 66, 71, 74, 154, 126, 57, 20, 7],
        [2, 8, 15, 24, 14, 51, 48, 68, 145, 55, 11, 2],
    ]
)

# task 1C
fC = np.concatenate((fA, fB), axis=0).T

print(fC)
