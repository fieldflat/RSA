#
# CRT-ModBinを実行するプログラム
#
import binary as bin
import montgomery as mon

#
# B*b = 1 (mod n)となるbを返す.
#
def mod_equal_1_crt(B, n):
    for b in range(2, n):
        if (B*b) % n == 1:
            break
    return b

#
# CRT-ModBinを実行するメソッド
#
def crt(c,d,N,p,q):
    #print('\n\nc={0}, d={1}, N={2}, p={3}, q={4}'.format(c,d,N,p,q))
    a, mod_count1, mult_count1 = mon.mod_bin(c, d, p)
    print('c**d mod p = {0}'.format(a))
    b, mod_count2, mult_count2 = mon.mod_bin(c, d, q)
    print('c**d mod q = {0}'.format(b))
    #print('\na = {0}, b = {1}'.format(a, b))
    mod_count = mod_count1 + mod_count2
    mult_count = mult_count1 + mult_count2

    """
    質問その5：以下を確認.
    """

    # Q, Pの計算
    # countの操作はしなくて良い.
    # あらかじめ計算しなければいけないものなので.
    y = mod_equal_1_crt(q, p)
    x = mod_equal_1_crt(p, q)

    # 以下の二つはcountを操作しなくて良い
    # あらかじめ計算しなければいけないものなので.
    Q, _ = bin.modulo(q*y, N, mod_count)
    P, _ = bin.modulo(p*x, N, mod_count)

    aq, mult_count = bin.multiply(a, Q, mult_count)
    bp, mult_count = bin.multiply(b, P, mult_count)
    aqbp = aq + bp
    ans, mod_count = bin.modulo(aqbp, N, mod_count)

    return ans, mod_count, mult_count
