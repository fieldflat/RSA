#
# 定数一覧
#
p = 5
q = 7
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
    import crt_modbin as crt
    import random

    print('\n\n\n********* p = {0}, q = {1}, N = {2}, phi_n = {3} ********\n'.format(p, q, N, phi_N))

    # 以下, 鍵生成アルゴリズム
    array = key.coprime(phi_N)
    set_array = key.mod_equal_1(array, phi_N) # これで[d,e]のセットを取得できる.
    #print(set_array)

    # 以下, 鍵と暗号文の設定
    c = 3
    d, e = random.choice(set_array)
    d, e = 5, 5
    #d, e = 3707, 6323    #p, q, c = 71, 97, 153
    print('******** c = {0} , d = {1}, {2} , e = {3} ********\n'.format(c, bin.binary_d(d), d, e))

    # 以下, バイナリ法の実施により,
    # 平文mとカウント数countを計算
    print('*************binary_method*************')
    m, mod_count, mult_count = bin.binary_method(c, d, N)
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    print('binary(c, d, N) = {0}'.format(m))
    print('mod_count = {0}'.format(mod_count))
    print('mult_count = {0}'.format(mult_count))


    # 以下Mod_Bin
    print('\n************* Mod_bin *************')
    m, mod_count, mult_count = mon.mod_bin(c, d, N)
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    print('mod_bin(c, d, N) = {0}'.format(m))
    print('mod_count = {0}'.format(mod_count))
    print('mult_count = {0}'.format(mult_count))


    # 以下CRT-Modbin
    print('\n************* CRT-Mod_bin *************')
    m, mod_count, mult_count = crt.crt(c,d,N,p,q)
    #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
    print('CRT-ModBin(c, d, N, p, q) = {0}'.format(m))
    print('mod_count = {0}'.format(mod_count))
    print('mult_count = {0}'.format(mult_count))


    # 一致性のチェック
    print('\n********** 暗号化(一致性のチェック) ***********')
    print('m = {0}, e = {1}, N = {2}'.format(m, e, N))
    c, _, _ = bin.binary_method(m, e, N)
    print('binary(m, e, N) = {0}'.format(c))
    c, _, _ = mon.mod_bin(m, e, N)
    print('mod_bin(m, e, N) = {0}'.format(c))
    c, _, _ = crt.crt(m, e, N, p, q)
    print('CRT-ModBin(m, e, N, p, q) = {0}'.format(c))
    print('暗号文 c = {0}\n\n'.format(c))
