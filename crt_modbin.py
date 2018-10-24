#
# CRT-ModBinを実行するプログラム
#
import binary as bin
import montgomery as mon

#
# B*b = 1 (mod n)となるbを返す.
#
"""
def mod_equal_1_crt(B, n):
    for b in range(2, n):
        if (B*b) % n == 1:
            break
    return b
"""

def egcd(a, b):
 (x, lastx) = (0, 1)
 (y, lasty) = (1, 0)
 while (b != 0):
  q = a // b
  (a, b) = (b, a%b)
  (x, lastx) = (lastx - q*x, x)
  (y, lasty) = (lasty - q*y, y)
 return (lastx, lasty, a)

def mod_equal_1_crt(B, n):
 (inv, q, gcd_val) = egcd(B, n)

 return inv%n


#
# CRT-ModBinを実行するメソッド
#
def crt(c,d,N,p,q):

    mod_count = 0
    mult_count = 0
    #
    # あらかじめ計算しておく部分
    #
    d_p = d % (p-1)
    d_q = d % (q-1)
    #d_p, _ = bin.modulo(d, p-1, mod_count)
    #d_q, _ = bin.modulo(d, q-1, mod_count)
    q_dash = mod_equal_1_crt(q, p)
    #print('q_dash = {0}'.format(q_dash))

    """
    # Q, Pの計算
    # countの操作はしなくて良い.
    # あらかじめ計算しなければいけないものなので.
    y = mod_equal_1_crt(q, p)
    x = mod_equal_1_crt(p, q)

    # 以下の二つはcountを操作しなくて良い
    # あらかじめ計算しなければいけないものなので.
    Q, _ = bin.modulo(q*y, N, 0)
    P, _ = bin.modulo(p*x, N, 0)
    """

    #
    # 以上, あらかじめ計算しておく部分
    #

    """
    #print('\n\nc={0}, d={1}, N={2}, p={3}, q={4}'.format(c,d,N,p,q))
    print('================= CRT(c:{0}, d:{1}, N:{2}, p:{3}, q:{4}) ================='.format(c, d, N, p, q))
    a, mod_count1, mult_count1 = mon.mod_bin(c, d, p)
    print('c**d mod p = {0}'.format(a))
    b, mod_count2, mult_count2 = mon.mod_bin(c, d, q)
    print('c**d mod q = {0}'.format(b))
    #print('\na = {0}, b = {1}'.format(a, b))
    mod_count = mod_count1 + mod_count2
    mult_count = mult_count1 + mult_count2


    aq, mult_count = bin.multiply(a, Q, mult_count)
    bp, mult_count = bin.multiply(b, P, mult_count)
    aqbp = aq + bp
    ans, mod_count = bin.modulo(aqbp, N, mod_count)
    """

    #print('================= CRT(c:{0}, d:{1}, N:{2}, p:{3}, q:{4}) ================='.format(c, d, N, p, q))
    #c_p = c % p
    c_p, mod_count = bin.modulo(c, p, mod_count)
    #print('c_p = c % p = {0} % {1} = {2}'.format(c, p, c_p))
    #print('d_p = d % (p-1) = {0} % {1} = {2}'.format(d, p-1, d_p))

    #c_q = c % q
    c_q, mod_count = bin.modulo(c, q, mod_count)
    #print('c_q = c % q = {0} % {1} = {2}'.format(c, q, c_q))
    #print('d_q = d % (q-1) = {0} % {1} = {2}'.format(d, q-1, d_q))

    m_p, mod_count1, mult_count1 = mon.mod_bin(c_p, d_p, p)
    #print('(c_p)**(d_p) mod p = {0}'.format(m_p))

    m_q, mod_count2, mult_count2 = mon.mod_bin(c_q, d_q, q)
    #print('(c_q)**(d_q) mod q = {0}'.format(m_q))

    mod_count += (mod_count1 + mod_count2)
    mult_count += (mult_count1 + mult_count2)

    x, mult_count = bin.multiply(q_dash, (m_p - m_q), mult_count)
    y, mod_count = bin.modulo(x, p, mod_count)
    z, mult_count = bin.multiply(y, q, mult_count)
    ans = m_q + z

    #ans = m_q + (q_dash * (m_p - m_q) mod p)

    return ans, mod_count, mult_count
