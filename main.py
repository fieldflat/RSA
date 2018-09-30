#
# 定数一覧
#
p = 269
q = 271
N = p * q
phi_N = (p-1)*(q-1) # Nのオイラー数
Loop_times = 10000 # ループ回数
d_length = 1024 # dの鍵長
d_top_bit = 1 # dにおける1の最上位ビット
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
        #d = 129667142224493376692598009254433971104142689639133939016663805235690514764070439278340529821593613733767736085840342773227562005989366225702930262500188315921135735194352545776495216733861881734424315530019034559017641676246678908946030724757838055909739018695585134456243742833078805185867721830502040224979
        #d = 98988172907157536041411651836332915409495238193958618881994891816204855747906446866341871818009754294835341535624597289908621427392149320450427205852149548332287353115497516242401599421634979853506638393804768050236069253337668774919239694949456378470058673515155977335130447038781976130436286554482667842358
        #d = 155220333643075440049874609005254799824389838264946193126966558624583992636973173335977229916631884962555133905435522866470967523787387823856289879993237744910808966653958757859034906792661194143927663715974828957407525615274485877655663416792652797611750564594666211555371726839364516553421973019531262185165
        #d = 90404803435003011030952403298087588241122976397891586528577171387498341600254545243309118060900715330317784854384938000055299508064630220442332245328982659778429230323162186930723694800834837140160063114778386876608703929802434819989551055752716760704798322393815581622176658177005092913574865684004109308071
        d = 105587712568170014815018788924256375275021522565307677987799946428380600019073852805257804352058888661964091896598153579944877946366587860527015837499891326244570099402093681549841377236493224231078029895318102881947781601120548885464048829657105266971946196883589979781409233865566147934205902543340689244829
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


    plot.plotting(binary_mod_count_list, binary_mult_count_list,  binary_sum_count_list,'binary')
    plot.plotting(modbin_mod_count_list, modbin_mult_count_list, modbin_sum_count_list,'ModBin')
    plot.plotting(crt_mod_count_list, crt_mult_count_list, crt_sum_count_list, 'CRT-ModBin')
