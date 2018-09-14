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
    a, count1 = mon.mod_bin(c, d, p)
    b, count2 = mon.mod_bin(c, d, q)
    #print('\na = {0}, b = {1}'.format(a, b))
    count = count1 + count2

    # Q, Pの計算
    y = mod_equal_1_crt(q, p)
    x = mod_equal_1_crt(p, q)

    # 以下の二つはcountを操作しなくて良い
    Q, count3 = bin.modulo(q*y, N, count)
    P, count3 = bin.modulo(p*x, N, count)

    ans, count = bin.modulo(a*Q+b*P, N, count)

    return ans, count
