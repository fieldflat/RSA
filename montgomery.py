#
# ModBinを実行するプログラム
#

import math
import main
import binary as bin

p = main.p
q = main.q
N = main.N
phi_N = main.phi_N

array_N = bin.binary_d(N)
length_N = len(array_N)
R = 2 ** length_N
R_2 = R*R % N

#
# N*(N') mod R = -1となるN'を返す.
#
def mod_equal_minus_1(N, R):
    for n_prime in range(2, R):
        if (n_prime*N) % R == (-1+R):
            return n_prime

#
# モンゴメリ還元
#
def MR(T, count):
    #tr, count = bin.modulo(T, R, count)
    m_1 = ((T % R) * N_dash) % R
    #m_1, count = bin.modulo((tr * N_dash), R, count)
    m_2 = (T + m_1*N)//R
    if m_2 <= N:
        return m_2, count
    else:
        count += 1
        return m_2 - N, count

#
# ModBinを実行するメソッド
#
def mod_bin(c, d, N):
    mod_count = 0
    mult_count = 0
    count = 0
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    large_C, count = MR(c*R_2, count)
    large_M = large_C
    array_d = bin.binary_d(d)
    l = len(array_d)
    for i in range(1, l):
        large_M, count = MR(large_M * large_M, count)
        if array_d[i] == 1:
            count += 1
            large_M, count = MR(large_M * large_C, count)
    m, count = MR(large_M, count)

    return m, count

N_dash = mod_equal_minus_1(N, R)
