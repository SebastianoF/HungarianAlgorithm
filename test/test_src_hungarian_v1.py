from controller.src_hungarian_v1 import *
from nose.tools import assert_equal, assert_raises
from numpy.testing import assert_array_almost_equal, assert_array_equal
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