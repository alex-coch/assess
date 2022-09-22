import itertools
import sys

N = int(sys.argv[1])
s = '0' * N + ''.join(map(str, range(1, N + 1)))
for i in set(itertools.permutations(s, N * 2)):
    print(''.join(i))
