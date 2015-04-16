from model.matrix_generator import *
from nose.tools import assert_equal, assert_raises
from numpy.testing import assert_array_almost_equal, assert_array_equal
import numpy as np


def test_gen_random_permutation():
    n = 5
    random_permutation = gen_random_permutation(n)
    assert len(random_permutation) == n
    assert len(set(random_permutation)) == n
    for i in range(n):
        assert i in random_permutation


def test_shape_gen_matrix():
    n_max, d = 10, 5
    a = gen_matrix(n_max, d)
    assert_array_equal(a.shape, (d, d))


def test_type_and_values_gen_matrix():
    n_max, d = 10, 5
    a = gen_matrix(n_max, d)
    assert a.dtype == 'int64'
    assert np.amax(a) < n_max and np.amin(a) >= 0


def test_max_val_gen_matrix():
    n_max, d = 10, 5
    a = gen_matrix(n_max, d)
    assert a.max() < n_max


def test_diagonal_dig_permutation():
    d = 6
    m = np.array([5]*(d**2)).reshape(d, d)
    permutation = range(d)
    m = dig_permutation(m, permutation)
    assert_array_equal(list(np.diag(m)), [0]*d)


def test_antidiag_dig_permutation():
    d = 6
    m = np.array([5]*(d**2)).reshape(d, d)
    permutation = range(d)[::-1]
    m = dig_permutation(m, permutation)
    antidiag = [m[j, d-1-j] for j in range(d)]
    assert_array_equal(antidiag, [0]*d)