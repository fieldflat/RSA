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
    b, mod_count2, mult_count2 = mon.mod_bin(c, d, q)
    #print('\na = {0}, b = {1}'.format(a, b))
    mod_count = mod_count1 + mod_count2
    mult_count = mult_count1 + mult_count2

    # Q, Pの計算
    # countの操作はしなくて良い.
    # あらかじめ計算しなければいけないものなので.
    y = mod_equal_1_crt(q, p)
    x = mod_equal_1_crt(p, q)

    # 以下の二つはcountを操作しなくて良い
    # あらかじめ計算しなければいけないものなので.
    Q, no_count_mod_count = bin.modulo(q*y, N, mod_count)
    P, no_count_mod_count3 = bin.modulo(p*x, N, mod_count)

    mult_count += 2 # a*Q+b*Pを実行するため.
    ans, mod_count = bin.modulo(a*Q+b*P, N, mod_count)

    return ans, mod_count, mult_count
