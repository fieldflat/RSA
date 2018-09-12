#
# 鍵生成プログラム
#

import math
import main

p = main.p
q = main.q
N = main.N
phi_N = main.phi_N

#
# 整数変数xと互いに素で, xより小さい数全てを配列に格納して返す
#
def coprime(x):
    array = []
    for i in range(2, x):
        if math.gcd(x, i) == 1:
            array.append(i)
    return array

#
# arrayの各要素eに対して, de = 1 (mod phi_N)となるdを計算し, [d,e]のセットを配列として返す.
#
def mod_equal_1(array, phi_N):
    set_array = []
    for e in array:
        for d in range(2, phi_N):
            if (d*e) % phi_N == 1:
                set_array.append([d, e])
                break
    return set_array
