from controller.src_hungarian_v1 import *
from nose.tools import assert_equal
from numpy.testing import assert_raises, assert_array_equal
import numpy as np
from scipy.linalg import circulant


def test_row_reduction_1():
    d = 5
    m = np.array([0]*d**2).reshape(d, d)
    m_red = row_reduction(m)
    m_expected = np.array([0]*d**2).reshape(d, d)
    assert_array_equal(m_red, m_expected)


def test_row_reduction_2():
    d = 5
    m = np.array([[j+1] for j in range(d)*d]).reshape(d, d)
    m_red = row_reduction(m)
    m_expected = np.array([[j] for j in range(d)]*d).reshape(d, d)
    assert_array_equal(m_red, m_expected)


def test_col_reduction_1():
    d = 5
    m = np.array([[j+1]*d for j in range(d)])
    m_red = col_reduction(m)
    m_expected = np.array([[j]*d for j in range(d)])
    assert_array_equal(m_red, m_expected)


def test_col_reduction_2():
    d = 5
    m = np.array([[j+1]*d for j in range(d)])
    m_red = col_reduction(m)
    m_expected = np.array([[j]*d for j in range(d)])
    assert_array_equal(m_red, m_expected)


def test_percolation_finder():
    # there must be a zero in each row, otherwise
    # there are no percolation available
    m = circulant([2, 3, 4, 0])
    a = percolation_finder(m)
    founded_percolation = a[1][0]
    expected_percolation = [1, 2, 3, 0]
    assert_array_equal(founded_percolation, expected_percolation)


def test_percolation_finder_type_error():
    m = circulant([2, 3, 4, 1])
    assert_raises(TypeError, percolation_finder(m))


def test_percolation_finder_multiple_row_n_5():
    m = np.array([0]*5**2).reshape(5, 5)
    a = percolation_finder(m, max_num_percolation=5)
    number_of_paths = len(a[1]) - 5
    expected_number_of_paths = 5
    assert_equal(number_of_paths, expected_number_of_paths)


def test_percolation_finder_multiple_row_n_15():
    m = np.array([0]*5**2).reshape(5, 5)
    a = percolation_finder(m, max_num_percolation=15)
    number_of_paths = len(a[1]) - 15
    expected_number_of_paths = 15
    assert_equal(number_of_paths, expected_number_of_paths)