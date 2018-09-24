#
# 定数一覧
#
p = 269
q = 271
N = p * q
phi_N = (p-1)*(q-1) # Nのオイラー数
Loop_times = 1000 # ループ回数
d_length = 1024 # dの鍵長
d_top_bit = 500 # dにおける1の最上位ビット
d_weight = 512 # dの重み

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
    import plot
    import random

    binary_mod_count_list = []
    binary_mult_count_list = []
    binary_sum_count_list = []
    modbin_mod_count_list = []
    modbin_mult_count_list = []
    modbin_sum_count_list = []
    crt_mod_count_list = []
    crt_mult_count_list = []
    crt_sum_count_list = []

    print('\n\n\n********* p = {0}, q = {1}, N = {2}, phi_n = {3} ********\n'.format(p, q, N, phi_N))

    # 以下, 鍵生成アルゴリズム
    array = key.coprime(phi_N)
    #set_array = key.mod_equal_1(array, phi_N) # これで[d,e]のセットを取得できる.
    #print(set_array)

    for i in range(0, Loop_times):
        # 以下, 鍵と暗号文の設定
        c = random.randint(1, N-1)
        #c = 13
        #d, e = random.choice(set_array)
        d = key.make_d(d_length, d_top_bit, d_weight)
        d = key.change_decimal(d)
        print('\n\n************* {0}回目 ***************'.format(i+1))
        print('******** c = {0} , d = {1}, {2}  ********\n'.format(c, bin.binary_d(d), d))
        #print('******** c = {0} , d = {1}, {2} , e = {3} ********\n'.format(c, bin.binary_d(d), d, e))

        # 以下, バイナリ法の実施により,
        # 平文mとカウント数countを計算
        print('*************binary_method*************')
        m, mod_count, mult_count = bin.binary_method(c, d, N)
        binary_mod_count_list.append(mod_count)
        binary_mult_count_list.append(mult_count)
        binary_sum_count_list.append(mod_count + mult_count)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('binary(c, d, N) = {0}'.format(m))
        print('mod_count = {0}'.format(mod_count))
        print('mult_count = {0}'.format(mult_count))
        #print('binary_mod_count_list = {0}'.format(binary_mod_count_list))
        #print('binary_mult_count_list = {0}'.format(binary_mult_count_list))


        # 以下Mod_Bin
        print('\n************* Mod_bin *************')
        m, mod_count, mult_count = mon.mod_bin(c, d, N)
        modbin_mod_count_list.append(mod_count)
        modbin_mult_count_list.append(mult_count)
        modbin_sum_count_list.append(mod_count + mult_count)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('mod_bin(c, d, N) = {0}'.format(m))
        print('mod_count = {0}'.format(mod_count))
        print('mult_count = {0}'.format(mult_count))
        #print('modbin_mod_count_list = {0}'.format(modbin_mod_count_list))
        #print('modbin_mult_count_list = {0}'.format(modbin_mult_count_list))


        # 以下CRT-Modbin
        print('\n************* CRT-Mod_bin *************')
        m, mod_count, mult_count = crt.crt(c,d,N,p,q)
        crt_mod_count_list.append(mod_count)
        crt_mult_count_list.append(mult_count)
        crt_sum_count_list.append(mod_count + mult_count)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('CRT-ModBin(c, d, N, p, q) = {0}'.format(m))
        print('mod_count = {0}'.format(mod_count))
        print('mult_count = {0}'.format(mult_count))
        #print('crt_mod_count_list = {0}'.format(crt_mod_count_list))
        #print('crt_mult_count_list = {0}'.format(crt_mult_count_list))


        # 一致性のチェック
        """
        print('\n********** 暗号化(一致性のチェック) ***********')
        print('m = {0}, e = {1}, N = {2}'.format(m, e, N))
        c, _, _ = bin.binary_method(m, e, N)
        print('binary(m, e, N) = {0}'.format(c))
        c, _, _ = mon.mod_bin(m, e, N)
        print('mod_bin(m, e, N) = {0}'.format(c))
        c, _, _ = crt.crt(m, e, N, p, q)
        print('CRT-ModBin(m, e, N, p, q) = {0}'.format(c))
        print('暗号文 c = {0}\n\n'.format(c))
        """
    plot.plotting(binary_mod_count_list, binary_mult_count_list,  binary_sum_count_list,'binary')
    plot.plotting(modbin_mod_count_list, modbin_mult_count_list, modbin_sum_count_list,'ModBin')
    plot.plotting(crt_mod_count_list, crt_mult_count_list, crt_sum_count_list, 'CRT-ModBin')
