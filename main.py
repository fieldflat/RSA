#
# 定数一覧
#
#p = 269
#q = 271
p = 1683317
#p = 9999973
#p = 6025133
#q = 2146159
#q = 1289513
#q = 8621749
q = 6700417
#q = 9999991

N = p * q
phi_N = (p-1)*(q-1) # Nのオイラー数
Loop_times = 1000 # ループ回数
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
        #d = 90071186311999362788755963842271919032901320345624111091925866785870887410966846212653460541312009646042265420772617971613550488970003078250204684147898640305715062235362579686116990362032029895553043672391000120765711354025623132640677259373153853338147620200325451923618657539030651366094668811732470726656
        #d = 138077524384358897387044254528942666865362436963425081806222678029623527212561397169625919256841085997842460692685629820335432379563877502861077662100645851747408164039505064751503719854570729630741324273793686789643069754389888125919913610491927011554612571257339014291317914843276351034098443218764569772032
        #d = 112355821013181156334579806714681205113924101983091861382414581448074528853593605127763129459607001465442516908138238424303909864293999123027639058680152442574950795353128551552720849511889171655164974758120631156315783552861760016539440473035738314285696233932793785419140238228427811142518736338748655534216
        #d = 133857774395556098823468076626040347428204866818519542402902008784242273588316831913605996105230853461276135011422723944412845259711225048858837394986306394647391907198726511192712952714328510682163669967335973252036472304294328739156120877752865219694442283089125533996403824366372974853733187988425356295024
        #d = 92672982967554862852872006766567885353927794137150728379364376690926427171759450260823444154424352669428620565618041049755868480284199412293078394066055239894180641830867546527203202271291597555024007333879865905283486866630899589672475264171999801451395902946562129189391119900984175066161729889310646122594
        #d = 113813244351128015985725472713799074858302071177559053942112014638788671381991253282405181172424524305518788455655662991697764200854729806319332367596212279599001943195420594782844193398223385020569219824365726550599798813591088325549820289065752592119059411046289242404680945642950558285906917488427350067624
        #d = 154306836123321631119810799993069910562141298931598323240160602873671313236111868972030294077912144521304411731326072185184552318703310573606495608896444935154732549995879559329450180425460887277250996580725663464080385147621501500334111997031535773362131377142103450071529478728786081711354141515585781890867
        #d = 144158195593448605833804358266959731071319524602506883655484058320858197715337147221541236215995256052433774784893470051901675638209433372179900041158152554361983763960343665324874540181999367855835609860134390778783899662849805853369844243552402213219357445415050466245170450596556905770235758017088277438463
        d = 133882584169402263649273269380196608150084375269146243075496885327405606895985408568168074590228694708438736519641709599822579193115157935449659948346845017681175549217934255050505731490489216233723387151881486768711240179550970803743221393089463044661701791371054424648342246977177087977856380921510782107615
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

        print('乗算クロック数 = {0}'.format(mult_count2*1024))
        print('剰余クロック数 = {0}'.format(mod_count2*32))
        print('総クロック数 = {0}'.format(mult_count2*1024 + mod_count2*32))
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
