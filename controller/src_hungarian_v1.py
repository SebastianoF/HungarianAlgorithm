# -------------------------
# source-code hungarian algorithm
# See the reference:
#-------------------------


def row_reduction(m):
    """
    Step 1 row reduction
    """
    s = m.copy()
    for i in range(s.shape[0]):
        min_row = min([s[i, j] for j in range(s.shape[1])])
        for j in range(s.shape[1]):
            s[i, j] -= min_row
    return s


def col_reduction(m):
    """
    Step 2 column reduction
    """
    s = m.copy()
    for j in range(s.shape[0]):
        min_col = min([s[i, j] for i in range(s.shape[0])])
        for i in range(s.shape[1]):
            s[i, j] -= min_col
    return s

walks = []


def percolation_finder(m, find_all=True, max_percolation=6):
    """
    Step 3 percolation finder
    """
    #walks = []

    def redundancy_index(v):
        n = len(v)
        occurrence_vector = [v.count(i) for i in range(n)]
        return max(occurrence_vector) - 1 + occurrence_vector.count(0) * 1.0 / n

    def scout(m, breadcrumbs):
        global walks
        n_cols = m.shape[0]
        crumbs_number = len(breadcrumbs)
        #print breadcrumbs
        if crumbs_number < n_cols:
            col_index_arranged = list(set(range(n_cols)) - set(breadcrumbs)) + list(set(breadcrumbs))
            for j in col_index_arranged:
                if m[crumbs_number, j] == 0:
                    scout(m, breadcrumbs + [j])
        elif crumbs_number == n_cols:
            walks_recorder(breadcrumbs)

    def walks_recorder(v, find_all_=find_all):
        global walks
        ri = redundancy_index(v)
        if find_all_:
            walks = walks + [v] + [ri]
        else:
            if 0 not in walks and len(walks) < max_percolation:
                walks = walks + [v] + [ri]

    for j in range(m.shape[1]):
        if m[0, j] == 0:
            scout(m, [j])

    return [m, walks]


def resolvability_query(m, walks_):
    """
    resolvability_test
    """
    min_redundancy = min(walks_)
    filtered_walks = [walks_[i] for i in range(len(walks_))[::2] if walks_[i + 1] == min_redundancy]
    if min_redundancy == 0:
        flag = True
    else:
        flag = False
    return [m, filtered_walks, flag]


def covering_segments_searcher(m, min_redundancy_percolation):
    """
     step 5, auxiliary function
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
    step 5 - shaker
    """
    n_rows = m.shape[0]
    n_cols = m.shape[1]
    min_redundancy_percolation = filtered_walks[0]
    # (1)
    [cov_row, cov_col] = covering_segments_searcher(m, min_redundancy_percolation)
    # (2)
    zero_pos_in_cov_row = [i for i in range(n_rows) if cov_row[i] == 0]
    zero_pos_in_cov_col = [j for j in range(n_cols) if cov_col[j] == 0]
    m = min([m[i, j] for i in zero_pos_in_cov_row for j in zero_pos_in_cov_col])
    # (3)
    for i in range(n_rows):
        for j in range(n_cols):
            if cov_row[i] == 0 == cov_col[j]:
                m[i, j] -= m
            elif cov_row[i] == 1 == cov_col[j]:
                m[i, j] += 2 * m
    return m


def hungarian(m, find_all=True, max_percolation=6):
    """

    :param m: cost matrix
    :param find_all: if require all the permutations
    :param max_percolation:
    :return: solution to the hungarian algorithm with cost matrix m
    """
    global walks
    walks = []
    cont = 0
    max_loop = max(m.shape[0], m.shape[1])
    s = row_reduction(col_reduction(m))
    [s, walks] = percolation_finder(s, find_all, max_percolation)
    [s, filtered_walks, flag] = resolvability_query(s, walks)
    while not flag and cont < max_loop:
        s = shaker(s, filtered_walks)
        walks = []
        [s, walks] = percolation_finder(s, find_all, max_percolation)
        [s, filtered_walks, flag] = resolvability_query(s, walks)
        cont += 1
    walks = []
    return filtered_walks