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
d_weight = 768 # dの重み

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
        #d = 134915454641405804456485143665201754424596023110346764326057417180316928185941980868285624671568104523485681864248245547285919942722141151459570971739351205141940604199054633460896520261688544415375557697488208868878981216001111084042911689542540422862958586816764529112070582411220215331222998435004111914120
        #d = 117973613314725240428181563242104188994155766251524969707567491349843965625086495939112257356215552902397205721497723113588852608596218574994648231869783909295644969853963253953248951591774783771757867560421654540771623509787093494026630226013822855947905696039531157779213373409415341525871675861079341138433
        #d = 89888771675121838833320390709549304532793892998261667938440763953705936061987023915595054164691239044897900549588728586071899211577530177005038407715995575497908207031005658654786534041735098210499458979627963338162499167815787595631525900451590372766217019082203877706426149668440474142876128237320495171608
        #d = 121031295719596071904596507865424914793393328803254372167589684735846751014414921461689294250177809345371782798153390951869597852426664268546078488577862978101570256025934254952987551211884027313603603680897477386764452976599145921670739846303199488807218220214131009951462800777539712785391878748466557034697
        d = 178364854086087593806842647602004200491024243602206933758186872356529711402422976313312493732445948779049046330500868588291169074057488304742708275839286608338261619235560897123950640217789008145046920894569857207741785389047024852887239558839423089725779350034864856872861395257192697106208021972374576136179
        #d = 176913431551634683946482101254912923278042063111018208568004735105550521689862807515238939951787729581063536489943935462671552130529845841123606004741899563357672796193746550104274245381253336069650161881872938365490224933417137312430344390613731989732018868007364648312747551029780987837154690111202371039211
        #d = 161289989142268417376989198481142443115897341761918998356996793992692775586902891468986504866469935841474151914181426814039107876995236404967278086805518209000886905634852216036226198406131331704492131852265039020766772595796647204805699360672482615066843212253686437309662594307894081738820532228769333292535

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
