__author__ = 'sebastiano'

from model.matrix_generator import *

global mm
global p


a = [1, 2, 3]

for _ in range(10):
    b = gen_random_permutation(5)
    #print b


d = 5

a = gen_matrix(12, d)

print a
print a.max()

permutation = range(d)

mm = dig_permutation(a, permutation)

print 'test:'
print mm


mm = gen_matrix(12, d)

print 'test2:'

print mm
perm = range(d)[::-1]
mm = dig_permutation(mm, perm)
print 'test2 antidiagonal digged:'
print mm



def lassie():
    d = 5
    a = gen_matrix(12, d)
    mm = dig_permutation(a, p)

    return mm