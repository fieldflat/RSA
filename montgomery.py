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
def MR(T, mod_count, mult_count):

    tr, mod_count = bin.modulo(T, R, mod_count) # tr <= T % R の計算
    trn, mult_count = bin.multiply(tr, N_dash, mult_count) # trn <= (T % R) * N'の計算
    m_1, mod_count = bin.modulo(trn, R, mod_count) # m_1 <= ((T % R) * N') % Rの計算
    #mult_count += 1 # m1 * Nを実行するため
    mn, mult_count = bin.multiply(m_1, N, mult_count)
    """
    質問その2：m_2計算時の「//」はmod_countをインクリメントしなくて良いか.
    """
    m_2 = (T + mn)//R

    if m_2 <= N:
        return m_2, mod_count, mult_count
    else:
        """
        質問その3：m_2 > Nのとき, mod_countを1インクリメントすべきかどうか.
        """
        mod_count += 1
        return m_2 - N, mod_count, mult_count

#
# ModBinを実行するメソッド
#
def mod_bin(c, d, N):
    mod_count = 0
    mult_count = 0
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    cr, mult_count = bin.multiply(c, R_2, mult_count)
    large_C, mod_count, mult_count = MR(cr, mod_count, mult_count)
    large_M = large_C
    array_d = bin.binary_d(d)
    l = len(array_d)
    for i in range(1, l):
        mm, mult_count = bin.multiply(large_M, large_M, mult_count)
        large_M, mod_count, mult_count = MR(mm, mod_count, mult_count)
        if array_d[i] == 1:
            mc, mult_count = bin.multiply(large_M, large_C, mult_count)
            large_M, mod_count, mult_count = MR(mc, mod_count, mult_count)
    m, mod_count, mult_count = MR(large_M, mod_count, mult_count)

    return m, mod_count, mult_count

N_dash = mod_equal_minus_1(N, R)
