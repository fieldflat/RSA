import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
import sys
sys.setrecursionlimit(10000)

def combination(n, k):
    if n < k:
        print("combination error")

    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return Fraction(n-k+1, k) * combination(n, k-1)

def C(n, k):
    ans = combination(n, k)

    return ans.numerator


def loop_mult(y, p, loop):
    for i in range(loop):
        y = y * p
        y = round(y, 10000)
        print(y)

    return y

if __name__ == '__main__':
    p = 0.726
    p_mult = 1000
    p_len = 3
    n = 3451

    x_list = list(range(0, n+1, 1))
    y_list = []

    for x in x_list:
        print(x)

        if x < 2300:
            y_list.append(0)
        else:
            y = C(n, x)
            y = y * (int(p * p_mult) ** x)
            y = y * (int((1-p) * p_mult) ** (n-x))
            length = len(str(y))
            y = int(str(y)[0:3])
            #y /= 1000
            #y /= (10 ** (3-1))
            y = y / (10 ** ((p_len)*(n)-length + 1))
            y /= (10 ** (3-1))
            """
            y = loop_mult(y, p, x)
            y = loop_mult(y, 1-p, n-x)
            """


            y_list.append(y)

    plt.plot(x_list, y_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



    """
    plt.figure(figsize=(10,5))    #画像の出力サイズを調整

    #sigma = [0.2,1.0,5.0] #シグマの値
    #muu = [0,4,0] #μの値

    #sigma = [200.0]
    #muu = [5950]
    sigma = [1200.0]
    muu = [7930]

    x = np.arange(7800., 8100., 0.01)     #-8から８まで0.01刻みの配列

    for i in zip(sigma,muu):     #zipは同時にループしてくれます
        y = (1 / np.sqrt(2 * np.pi * i[0] ) ) * np.exp(-1 * (x - i[1]) ** 2 / (2 * i[0]) )     #ガウス分布の公式

        plt.plot(x, y)     #x, yをplotします
        plt.grid()     #グリット線
        plt.xlabel('x')     #x軸のラベル
        plt.ylabel('y')     #y軸のラベル
        plt.title('μ = {0}, σ = {1}'.format(i[1], i[0]))
    #    plt.legend(["σ=0.2 μ=0", "σ=1.0 μ=4″,"σ=5.0 μ=0″],loc="upper left")   #凡例を左上に表示

    plt.show()
    """
