from nose.tools import assert_equal
from numpy.testing import assert_raises, assert_array_equal
import numpy as np

from HungarianAlgorithm.model import row_reduction, col_reduction, percolation_finder, resolvability_query, \
    covering_segments_searcher


''' Tests row and col reduction '''


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


''' Tests percolation finder '''


def test_percolation_finder():
    # there must be a zero in each row, otherwise
    # there are no percolation available
    m = np.array([[2, 3, 4, 0],
                  [0, 2, 3, 4],
                  [4, 0, 2, 3],
                  [3, 4, 0, 2]])
    a = percolation_finder(m)
    founded_percolation = a[1][0]
    expected_percolation = [3, 0, 1, 2]
    assert_array_equal(founded_percolation, expected_percolation)


def test_percolation_finder_type_error():
    m = np.array([[2, 3, 4, 1],
                  [1, 2, 3, 4],
                  [4, 1, 2, 3],
                  [3, 4, 1, 2]])
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


''' Test resolvability query '''


def test_resolvability_query_one_zero():
    phantom_input = [['phantom'], [[1, 2, 3], 1,
                                   [0, 2, 3], 0,
                                   [1, 2, 3], 1]]
    resp = resolvability_query(phantom_input[0], phantom_input[1])
    expected_resp = [['phantom'], [[0, 2, 3]], True]
    assert_array_equal(resp, expected_resp)


def test_resolvability_query_no_zero_one_min():
    phantom_input = [['phantom'], [[1, 2, 3], 1,
                                   [0, 2, 3], 0.5,
                                   [1, 2, 3], 1]]
    resp = resolvability_query(phantom_input[0], phantom_input[1])
    expected_resp = [['phantom'], [[0, 2, 3]], False]
    assert_array_equal(resp, expected_resp)


def test_resolvability_query_no_zero_all_min():
    phantom_input = [['phantom'], [[1, 2, 3], 1,
                                   [0, 2, 3], 1,
                                   [1, 2, 3], 1]]
    resp = resolvability_query(phantom_input[0], phantom_input[1])
    expected_resp = [['phantom'], [[1, 2, 3], [0, 2, 3], [1, 2, 3]], False]
    assert_array_equal(resp, expected_resp)


def test_resolvability_query_flag_1():
    resp = resolvability_query(['matrix'], [['walks'], 0])
    assert_equal(resp[2], True)


def test_resolvability_query_flag_2():
    resp = resolvability_query(['matrix'], [['walks'], 1])
    assert_equal(resp[2], False)


def test_percolation_finder__and_resolvability_query_custom():
    m = np.array([[0, 9, 7, 8, 1, 9],
                  [5, 8, 0, 4, 2, 6],
                  [5, 9, 5, 0, 3, 7],
                  [7, 6, 8, 2, 2, 0],
                  [9, 0, 7, 4, 2, 8],
                  [2, 1, 4, 6, 0, 7]])
    a = percolation_finder(m, max_num_percolation=15)
    b = resolvability_query(a[0], a[1])
    assert_equal(b[2], True)


def test_percolation_finder__and_resolvability_query_custom2():
    m = np.array([[1, 1, 0, 1, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0]])
    a = percolation_finder(m, max_num_percolation=15)
    b = resolvability_query(a[0], a[1])
    print("Consider this test carefully, a correct refactoring that changes the order of the walks may not pass it")
    assert_equal(b[2], False)


def test_percolation_finder__and_resolvability_query_custom3():
    m = np.array([[1, 1, 0, 1, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0]])
    a = percolation_finder(m, max_num_percolation=50)
    b = resolvability_query(a[0], a[1])
    assert_equal(b[2], True)  # same matrix as before, increased numbers of percolations.


''' Test covering segment searcher '''


def test_covering_segment_searcher_1():
    a = np.array([[0, 0, 0, 0],
                  [1, 0, 1, 1],
                  [1, 0, 1, 1],
                  [1, 0, 1, 1]])
    resp = covering_segments_searcher(a, [0, 1, 1, 1])
    assert_array_equal(resp, ([1, 0, 0, 0], [0, 1, 0, 0]))


def test_covering_segment_searcher_2():
    a = np.array([[0, 1, 1, 1],
                  [0, 1, 1, 1],
                  [0, 1, 1, 1],
                  [0, 1, 1, 1]])
    resp = covering_segments_searcher(a, [0, 0, 0, 0])
    assert_array_equal(resp, ([0, 0, 0, 0], [1, 0, 0, 0]))


def test_covering_segment_searcher_3():
    a = np.array([[1, 0, 1, 1],
                  [1, 1, 0, 1],
                  [1, 0, 1, 1],
                  [1, 0, 1, 1]])
    resp = covering_segments_searcher(a, [1, 2, 1, 1])
    assert_array_equal(resp, ([0, 1, 0, 0], [0, 1, 0, 0]))


def test_covering_segment_searcher_4():
    a = np.array([[6, 12, 14, 0],
                  [0, 0, 0, 5],
                  [9, 0, 1, 9],
                  [2, 0, 9, 8]])
    resp = covering_segments_searcher(a, [1, 2, 1, 1])
    assert_array_equal(resp, ([1, 1, 0, 0], [0, 1, 0, 0]))
