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

countMM = 0
countMC = 0
countNG = 0

#
# N*(N') mod R = -1となるN'を返す.
#
"""
def mod_equal_minus_1(N, R):
    for n_prime in range(2, R):
        #print(n_prime)
        if (n_prime*N) % R == (-1+R):
            return n_prime
"""

def mod_equal_minus_1(N, R):
    print('N={0}; R={1}'.format(N, R))
    result = 0;
    t = 0;
    r = R;
    i = 1;

    while ( r > 1 ):

        if (t % 2 == 0):
            t += N
            result += i

        t //= 2
        r /= 2
        i *= 2

    print('N_dash = {0}'.format(result))
    return result


#
# モンゴメリ還元
#
def MR(T, mod_count, mult_count, N_dash, N):

    global countMM
    global countMC
    global countNG
    #global flag
    #print('N: {0}'.format(N))
    array_N = bin.binary_d(N)
    length_N = len(array_N)
    R = 2 ** length_N
    #print('R:  {0}'.format(R))
    #print('N_dash: {0}'.format(N_dash))
    R_2 = R*R % N
    #print('N={0}, R={1}, R_2={2}, N_dash={3}'.format(N,R,R_2,N_dash))
    #print(' ~~~~~~~~~~~~ MR(T:{0}, mod_count:{1}, mult_count:{2}, N_dash:{3}, N:{4}) ~~~~~~~~~~~~'.format(T, mod_count, mult_count, N_dash, N))

    flag = bin.flag

    tr, mod_count = bin.modulo(T, R, mod_count) # tr <= T % R の計算
    #print('tr = T % R = {0} % {1} = {2}'.format(T, R, tr))
    trn, mult_count = bin.multiply(tr, N_dash, mult_count) # trn <= (T % R) * N'の計算
    #print('trn = tr * N_dash = {0} * {1} = {2}'.format(tr, N_dash, trn))
    m_1, mod_count = bin.modulo(trn, R, mod_count) # m_1 <= ((T % R) * N') % Rの計算
    #print('m_1 = trn % R = {0} % {1} = {2}'.format(trn, R, m_1))
    mn, mult_count = bin.multiply(m_1, N, mult_count)
    #print('mn = m_1 * N = {0} * {1} = {2}'.format(m_1, N, mn))
    """
    質問その2：m_2計算時の「//」はmod_countをインクリメントしなくて良いか.
    """
    m_2 = (T + mn)//R
    #print('m_2 = (T + mn)//R = ({0} + {1})//{2} = {3}'.format(T, mn, R, m_2))

    if m_2 <= N:
        #print('MRにおいてmod_countを余分にインクリメントしませんでした.\n')
        #print('@@@@@@@ flag = {0}'.format(flag))
        countNG += 1
        #print('NO:                countNG = {0}'.format(countNG))
        if flag == 1:
            countNG += 0
            #print('NO:                countNG = {0}'.format(countNG))
            #print('')

        return m_2, mod_count, mult_count
    else:
        #print('MRにおいてmod_countを余分にインクリメントしました.')
        """
        質問その3：m_2 > Nのとき, mod_countを1インクリメントすべきかどうか.
        """
        if flag == 1:
            countMM += 1
            #print('YES: countMM={0}'.format(countMM))
        else:
            countMC += 1
            #print('YES: countMC={0}'.format(countMC))

        mod_count += 1
        #print('m_2 = m_2 - N = {0} - {1} = {2}\n'.format(m_2, N, m_2-N))
        return m_2 - N, mod_count, mult_count

#
# ModBinを実行するメソッド
#
def mod_bin(c, d, N):

    global countMM
    global countMC
    global countNG

    countMM = 0
    countMC = 0
    countNG = 0

    array_N = bin.binary_d(N)
    #print('\n\narray_N = {0}'.format(array_N))
    length_N = len(array_N)
    #print('length_N = {0}'.format(length_N))
    R = 2 ** length_N
    R_2 = R*R % N
    N_dash = mod_equal_minus_1(N, R)

    mod_count = 0
    mult_count = 0
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    #print('c={0}, d={1}, N={2}, R={3}, R_2={4}, N_dash={5}'.format(c,d,N,R,R_2,N_dash))
    """
    質問その4：RとR_2の計算はカウント対象でない (ついでにRの計算方法があっているかを確認する).
    """
    #print('length_N: {0}, R : {1}, R_2 : {2}, N_dash : {3}'.format(length_N, R, R_2, N_dash))
    cr, mult_count = bin.multiply(c, R_2, mult_count)
    #print('cr = c * R_2 = {0}'.format(cr))
    #print('MR(c*R_2)の実行>>>')
    large_C, mod_count, mult_count = MR(cr, mod_count, mult_count, N_dash, N)
    print('largc_C = {0}'.format(large_C))
    #print('MR({1}): large_C={0}'.format(large_C, cr))
    large_M = large_C
    array_d = bin.binary_d(d)
    l = len(array_d)
    for i in range(1, l):
        mm, mult_count = bin.multiply(large_M, large_M, mult_count)
        #print('MM = {0}'.format(mm))
        #print('MR(M*M)の実行>>>')
        large_M, mod_count, mult_count = MR(mm, mod_count, mult_count, N_dash, N)
        #print('MR({1}) large_M={0}'.format(large_M, mm))
        if array_d[i] == 1:
            mc, mult_count = bin.multiply(large_M, large_C, mult_count)
            #print('MC = {0}'.format(mc))
            #print('MR(M*C)の実行>>>')
            large_M, mod_count, mult_count = MR(mc, mod_count, mult_count, N_dash, N)
            #print('MR({1}) large_M={0}'.format(large_M, mc))
    #print('MR(M)の実行>>>')
    bin.flag = 0
    m, mod_count, mult_count = MR(large_M, mod_count, mult_count, N_dash, N)
    #print('MR({1}) m={0}'.format(m, large_M))

    print('countMM = {0}'.format(countMM))
    print('countMC = {0}'.format(countMC))
    print('countNG = {0}'.format(countNG))

    return m, mod_count, mult_count, countMM, countMC, countNG

#N_dash = mod_equal_minus_1(N, R)
