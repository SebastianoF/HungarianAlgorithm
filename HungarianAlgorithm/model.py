import numpy as np


def row_reduction(m):
    """
    step 1: row reduction
    """
    assert isinstance(m, np.matrixlib.defmatrix.matrix)
    return m - np.min(m, axis=1)


def col_reduction(m):
    """
    step 2: col reduction
    """
    assert isinstance(m, np.matrixlib.defmatrix.matrix)
    return m - np.min(m, axis=0)


def redundace_index(v):
    """
    step 3: redundacy index
    """
    n = v.size
    occurrence_vector = [list(v).count(i) for i in range(n)]
    return np.max(occurrence_vector) - 1 + occurrence_vector.count(0) / float(n)


def percolation_finder(m, max_num_percolation=6):
    """
    Step 3 percolation finder
    """
    walks = { 'walk': [] }  # Name binding

    def redundancy_index(v):
        n = len(v)
        occurrence_vector = [v.count(i) for i in range(n)]
        return max(occurrence_vector) - 1 + occurrence_vector.count(0) * 1.0 / n

    def scout(m, breadcrumbs):
        n_cols = m.shape[1]
        crumbs_number = len(breadcrumbs)
        # print breadcrumbs
        if crumbs_number < n_cols:
            col_index_arranged = list(set(range(n_cols)) - set(breadcrumbs)) + list(set(breadcrumbs))
            for j in col_index_arranged:
                if m[crumbs_number, j] == 0:
                    # More scouts are launched only if some place in the walks' vector is available
                    # Rearranging indexes may guarantee that a percolation with 0 redundancy index is stored in the
                    # the first explorations, when available.
                    if len(walks['walk']) < 2 * max_num_percolation:
                        scout(m, breadcrumbs + [j])
        elif crumbs_number == n_cols:
            walks_recorder(breadcrumbs)

    def walks_recorder(v):
        ri = redundancy_index(v)
        walks['walk'] = walks['walk'] + [v] + [ri]

    first_zero = True
    for j in range(m.shape[1]):
        if m[0, j] == 0:
            if first_zero:
                # reset to [] the list of walks
                walks['walk'] = []
                first_zero = False
            # print 'A scout goes in mission'
            scout(m, [j])

    if len(walks['walk']) == 0:
        raise TypeError('Input matrix has no 0-percolations.')

    return [m, walks['walk']]


def resolvability_query(m, walks_):
    """
    :param m: cost matrix
    :param walks_: list of 0-percolation followed by its index of redundancy
    as returned by percolation_finder
    :return: M again untouched, followed by the list of $0$-percolation with
    minimal index of redundancy, and with a flag, True if the minimal index
    is 0 and so we have already our solution, False otherwise.
    """
    min_redundancy = np.min(walks_[1::2])
    filtered_walks = [walks_[i] for i in list(range(len(walks_)))[::2] \
                      if walks_[i + 1] == min_redundancy]
    if min_redundancy == 0:
        flag = True
    else:
        flag = False
    return [m, filtered_walks, flag]


def covering_segments_searcher(m, min_redundancy_percolation):
    """
     step 5, auxiliary function.
     Returns the positions of horizontal and vertical covering segments
    """
    # (A)
    n_rows = m.shape[0]
    n_cols = m.shape[1]
    marked_row = [0] * n_rows
    marked_col = [0] * n_cols
    # (B)
    occurrence_vector = [min_redundancy_percolation.count(i) for i in range(n_rows)]
    for pos in range(n_rows):
        if occurrence_vector[pos] > 1:
            duplicates_pos = [k for k in range(n_rows) if min_redundancy_percolation[k] == pos][1:]
            for j in duplicates_pos:
                marked_row[j] = 1
    # (C)
    flag_mark = 1
    while flag_mark != 0:
        flag_mark = 0
        # (C-1)
        for i in range(n_rows):
            if marked_row[i] == 1:
                for j in range(n_cols):
                    if m[i, j] == 0 and marked_col[j] != 1:
                        marked_col[j] = 1
                        flag_mark += flag_mark
        # (C-2)
        for j in range(n_cols):
            if marked_col[j] == 1:
                for i in range(n_rows):
                    if m[i, j] == 0 and marked_row[i] != 1 and min_redundancy_percolation[i] == j:
                        marked_row[i] = 1
                        flag_mark += 1
    # (D)
    covered_row = [(i + 1) % 2 for i in marked_row]
    covered_col = marked_col

    return covered_row, covered_col


def shaker(m, filtered_walks):
    """
    :param m : cost matrix $M$,
    :param filtered_walks: set of walks with minimal redundance index.
    """
    n_rows = m.shape[0]
    n_cols = m.shape[1]
    min_redundancy_percolation = filtered_walks[0]
    # (1)
    [cov_row, cov_col] = covering_segments_searcher(m, min_redundancy_percolation)
    # (2)
    zero_pos_in_cov_row = [i for i in range(n_rows) if cov_row[i] == 0]
    zero_pos_in_cov_col = [j for j in range(n_cols) if cov_col[j] == 0]
    uncovered_elements = [m[i, j] for i in zero_pos_in_cov_row for j in zero_pos_in_cov_col]
    if not uncovered_elements:  # uncovered_elements == []
        raise EnvironmentError('Not enough percolations has been considered, '
                               'set an higher max_num_percolation parameter!')

    min_val = min(uncovered_elements)
    # (3)
    for i in range(n_rows):
        for j in range(n_cols):
            if cov_row[i] == 0 == cov_col[j]:
                m[i, j] -= min_val
            elif cov_row[i] == 1 == cov_col[j]:
                m[i, j] += 2 * min_val
    return m


def hungarian(m, max_num_percolation=10):
    """
    Hungarian algorithm.
    Note that too many zeros in the initial cost matrix may need an high max_num_percolation,
    Set the weight away from zero, if this is a common value.
    Parameters:
    ------------
    :param m: cost matrix
    :param max_num_percolation:
    :return: solution to the hungarian algorithm with cost matrix m
    """
    walks = []
    cont = 0
    max_loop = max(m.shape[0], m.shape[1])
    s = row_reduction(col_reduction(m))
    [s, walks] = percolation_finder(s, max_num_percolation=max_num_percolation)
    [s, filtered_walks, flag] = resolvability_query(s, walks)
    while not flag and cont < max_loop:
        s = shaker(s, filtered_walks)
        walks = []
        [s, walks] = percolation_finder(s, max_num_percolation=max_num_percolation)
        [s, filtered_walks, flag] = resolvability_query(s, walks)
        cont += 1
    walks = []
    return filtered_walks
