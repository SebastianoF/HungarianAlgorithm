"""
model to generate the random matrix and solutions as toy examples.
matrix are np.array, permutations are list of integers
"""
import numpy as np
import random


def gen_random_permutation(n):
    ans = [-1]*n
    for i in range(n):
        ans[i] = random.choice(list(set(range(0, n)) - set(ans)))
    return ans


def gen_matrix(n_max, d):
    """
    :param n_max: maximal value of the integer in the matrix
    :param d: dimension of the square matrix
    :return: matrix of size d times d and integer values not greater than n_max
    """
    a = np.random.randint(n_max, size=(d, d))
    return a


def dig_permutation(m, p):
    """
    :param m: matrix dxd
    :param p: permutation
    :return: matrix m on which the percolation correspondent to the permutation p is digged
    """
    a = m.copy()
    for i in range(m.shape[0]):
        a[i, p[i]] = 0
    return a


def gen_matrix_given_permutation(n_max, d, p):
    """
    :param n_max: maximal value of the integer in the matrix
    :param d: dimension of the square matrix
    :param p: permutation as list of integer from 0 to d-1
    :return: matrix with minimal 0-percolation corresponding to the
     permutation, and just this only one!
    """
    a = gen_matrix(n_max-1, d)
    a = a + np.ones(d*d, dtype=np.int).reshape(d, d)
    return dig_permutation(a, p)


def gen_matrix_given_permutations(n_max, d, p_list):
    """
    :param n_max: maximal value of the integer in the matrix
    :param d: dimension of the square matrix
    :param p_list: list of permutations
    :return: matrix with 0-percolations corresponding to the given
     permutation list
    """
    a = gen_matrix(n_max-1, d) + np.ones(d*d, dtype=np.int).reshape(d, d)
    for p in p_list:
        a = dig_permutation(a, p)
    return a
