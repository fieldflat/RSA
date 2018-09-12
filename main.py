#
# 定数一覧
#
p = 193
q = 197
N = p * q
phi_N = (p-1)*(q-1) # Nのオイラー数

#
# メイン関数
#
if __name__ == '__main__':
    #
    # 他プログラムをインポート
    #
    import binary as bin
    import key
    import montgomery as mon
    import random

    print('********* p = {0}, q = {1}, N = {2}, phi_n = {3} ********\n'.format(p, q, N, phi_N))

    # 以下, 鍵生成アルゴリズム
    array = key.coprime(phi_N)
    set_array = key.mod_equal_1(array, phi_N) # これで[d,e]のセットを取得できる.
    #print(set_array)

    # 以下, 鍵と暗号文の設定
    c = 10
    d, e = random.choice(set_array)
    print('******** c = {0} , d = {1} , e = {2} ********\n'.format(c, bin.binary_d(d), e))

    # 以下, バイナリ法の実施により,
    # 平文mとカウント数countを計算
    m, count = bin.binary_method(c, d)
    print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    print('binary(c, d, N) = {0}'.format(m))
    print('count = {0}'.format(count))

    # 以下Mod_Bin
    m, count = mon.mod_bin(c, d, N)
    print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    print('mod_bin(c, d, N) = {0}'.format(m))
    print('count = {0}'.format(count))

    # cの一致性のチェック
    print('\n********** 暗号化(cの一致性のチェック) ***********')
    print('m = {0}, e = {1}, N = {2}'.format(m, e, N))
    c, count = bin.binary_method(m, e)
    print('binary(m, e, N) = {0}'.format(c))
    print('暗号文 c = {0}'.format(c))
