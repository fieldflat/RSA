#
# 定数一覧
#
#p = 269
#q = 271
#p = 1683317
p = 6025133
#q = 2146159
#q = 1289513
q = 8621749
#q = 6700417

N = p * q
phi_N = (p-1)*(q-1) # Nのオイラー数
Loop_times = 50 # ループ回数
d_length = 1024 # dの鍵長
d_top_bit = 1 # dにおける1の最上位ビット
d_weight = 500 # dの重み


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

    #
    # カウント数を格納しておくためのリスト
    #
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

    correct = 0 # 3種類のアルゴリズムの復号結果が一致しているかを確認する変数. ( = LOOP_timesとなれば完璧.)
    crt_odd = 0 # CRT-ModbinにおいてSumのカウント数が奇数であるかどうかを確認する変数.

    # 以下, 鍵生成アルゴリズム
    #array = key.coprime(phi_N)
    #set_array = key.mod_equal_1(array, phi_N) # これで[d,e]のセットを取得できる.
    #print(set_array)

    for i in range(0, Loop_times):
        # 以下, 鍵と暗号文の設定
        c = random.randint(1, N-1) #(1, N-1)
        #c = 13
        #d, e = random.choice(set_array)
        d = key.make_d(d_length, d_top_bit, d_weight)
        d = key.change_decimal(d)
        #d = 114498007768585415952318849106709696543966223977107756591430355135757434951106440944171247243418782562541537168303718895265322640716192209105440689903873462949617755108122375487770485369767116187690506332016093378079654124966658658919440302847139396810721383189265708907458491468126251194135938709667115602826
        print('\n\n************* {0}回目 ***************'.format(i+1))
        print('******** c = {0} , d = {1}, {2}  ********\n'.format(c, bin.binary_d(d), d))
        #print('******** c = {0} , d = {1}, {2} , e = {3} ********\n'.format(c, bin.binary_d(d), d, e))

        # 以下, バイナリ法の実施により,
        # 平文mとカウント数countを計算
        print('*************binary_method*************')
        m1, mod_count1, mult_count1 = bin.binary_method(c, d, N)
        binary_mod_count_list.append(mod_count1)
        binary_mult_count_list.append(mult_count1)
        binary_sum_count_list.append(mod_count1 + mult_count1)
        bin.average(binary_mod_count_list)
        bin.average(binary_mult_count_list)
        bin.average(binary_sum_count_list)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('binary(c, d, N) = {0}'.format(m1))
        print('mod_count = {0}'.format(mod_count1))
        print('mult_count = {0}'.format(mult_count1))
        #print('binary_mod_count_list = {0}'.format(binary_mod_count_list))
        #print('binary_mult_count_list = {0}'.format(binary_mult_count_list))


        # 以下Mod_Bin
        print('\n************* Mod_bin *************')
        m2, mod_count2, mult_count2 = mon.mod_bin(c, d, N)
        modbin_mod_count_list.append(mod_count2)
        modbin_mult_count_list.append(mult_count2)
        modbin_sum_count_list.append(mod_count2 + mult_count2)
        bin.average(modbin_mod_count_list)
        bin.average(modbin_mult_count_list)
        bin.average(modbin_sum_count_list)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('mod_bin(c, d, N) = {0}'.format(m2))
        print('mod_count = {0}'.format(mod_count2))
        print('mult_count = {0}'.format(mult_count2))
        #print('modbin_mod_count_list = {0}'.format(modbin_mod_count_list))
        #print('modbin_mult_count_list = {0}'.format(modbin_mult_count_list))


        # 以下CRT-Modbin
        print('\n************* CRT-Mod_bin *************')
        m3, mod_count3, mult_count3 = crt.crt(c,d,N,p,q)
        crt_mod_count_list.append(mod_count3)
        crt_mult_count_list.append(mult_count3)
        crt_sum_count_list.append(mod_count3 + mult_count3)
        bin.average(crt_mod_count_list)
        bin.average(crt_mult_count_list)
        bin.average(crt_sum_count_list)
        #print('c = {0}, d = {1}, N = {2}'.format(c, d, N))
        print('CRT-ModBin(c, d, N, p, q) = {0}'.format(m3))
        print('mod_count = {0}'.format(mod_count3))
        print('mult_count = {0}'.format(mult_count3))
        #print('crt_mod_count_list = {0}'.format(crt_mod_count_list))
        #print('crt_mult_count_list = {0}'.format(crt_mult_count_list))


        # 一致性のチェック
        if ((mod_count3 + mult_count3) % 2 == 1):
            crt_odd += 1

        if ((m1 == m2) and (m2 == m3)):
            correct += 1

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
    print('correct: {0}'.format(correct))
    print('crt_odd: {0}'.format(crt_odd))

    """
    plot.plotting(binary_mod_count_list, binary_mult_count_list,  binary_sum_count_list,'binary')
    plot.plotting(modbin_mod_count_list, modbin_mult_count_list, modbin_sum_count_list,'ModBin')
    plot.plotting(crt_mod_count_list, crt_mult_count_list, crt_sum_count_list, 'CRT-ModBin')
    """
