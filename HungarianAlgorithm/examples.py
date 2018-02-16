import numpy as np

from HungarianAlgorithm.model import hungarian
from HungarianAlgorithm.matrix_generator import gen_matrix_given_permutation, gen_matrix


if __name__ == '__main__':
    """
    Some test ready to go, to see utilities and limitations.
    """

    p = [0, 2, 3, 5, 1, 4]
    a = gen_matrix_given_permutation(10, 6, p)
    resp = hungarian(a)

    print('Cost matrix:')
    print(a)
    print('Solution:')
    print(resp)

    a = np.array([[0, 9, 7, 8, 1, 9],
                      [5, 8, 0, 4, 2, 6],
                      [5, 9, 5, 0, 3, 7],
                      [7, 6, 8, 2, 2, 0],
                      [9, 0, 7, 4, 2, 8],
                      [2, 1, 4, 6, 0, 7]])
    resp = hungarian(a, max_num_percolation=50)

    print('Cost matrix:')
    print(a)
    print('Solution:')
    print(resp)

    a = np.array([[1, 1, 0, 1, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0]])
    resp = hungarian(a, max_num_percolation=500)

    print('Cost matrix:')
    print(a)
    print('Solution:')
    print(resp)

    a = gen_matrix(60, 15)
    resp = hungarian(a, max_num_percolation=5000)

    print('Cost matrix:')
    print(a)
    print('Solution:')
    print(resp)

    # counterexample: matrix with too many zeros:
    # Bugs must be fixed for sparse matrices - code may fail here.

    a = gen_matrix(6, 15)
    print('\n\n --- Particular case where the algorithm fails --- ')
    print('\n For this matrix we expect the algorithm to raise an issue '
          '(too sparse respect to the max num percolation):')
    print('\nCost matrix:')
    print(a)
    resp = hungarian(a, max_num_percolation=10000)

    print('Solution:')
    print(resp)
