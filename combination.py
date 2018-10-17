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
