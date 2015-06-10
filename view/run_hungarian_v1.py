from controller.src_hungarian_v1 import *
from model.matrix_generator import *

"""
The folder view contains the actual utilization of the hungarian algorithm.
"""

p = [0, 2, 3, 5, 1, 4]
a = gen_matrix_given_permutation(10, 6, p)

print a

ans = hungarian(a)
#ans = a.shape

# TODO: test and debug each step of the hungarian algorithm!!

print ans

