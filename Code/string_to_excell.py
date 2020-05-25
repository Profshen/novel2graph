import xlsxwriter

#This file translate coordinates from tikzpicture form to an excel file (easy to plot for Power Point)

# hermione = "(0.3333333333333333,0.055697430765069944)(0.5,0.00899106720841314)(0.6666666666666666," \
#            "0.044493068618475684)(0.8333333333333333,0.013151304916594664)(1.0,0.011214634948915725)(1.0," \
#            "0.06310487751123339)(1.1666666666666667,0.032442398095156366)(1.3333333333333333,0.015389980849714102)(" \
#            "1.5,0.04461684162767632)(1.6666666666666665,0.037125010658615065)(1.8333333333333333," \
#            "0.046067112601006044)(2.0,0.08028293094346228)(2.0,0.07157398330428943)(2.125,0.049529263485158515)(2.25," \
#            "0.04027532399859457)(2.375,0.03358789754846936)(2.5,0.044683256185126696)(2.625,0.025546839797264242)(" \
#            "2.75,0.04699407180241011)(2.875,0.012993036066271446)(3.0,0.008721775580141533)(3.0,0.10286542543454968)(" \
#            "3.0588235294117645,0.08821159099765541)(3.1176470588235294,0.036035022159017105)(3.176470588235294," \
#            "0.033785605421382314)(3.235294117647059,0.023903160182944916)(3.2941176470588234,0.0629390884090626)(" \
#            "3.3529411764705883,0.04923096586348452)(3.4705882352941178,0.056501794082085666)(3.5294117647058822," \
#            "0.012749420184309246)(3.588235294117647,0.061756936604156265)(3.6470588235294117,0.02832917337646701)(" \
#            "3.7058823529411766,0.031237836733785773)(3.764705882352941,0.0760782655624912)(3.8235294117647056," \
#            "0.03517947362281404)(3.8823529411764706,0.029532597333841726)(3.9411764705882355,0.07603127949173472)(" \
#            "4.0,0.02709436042440927)(4.0,0.11422836728115504)(4.083333333333333,0.07886008282071744)(" \
#            "4.166666666666667,0.12411137542713602)(4.25,0.061446681205068576)(4.333333333333333,0.05194004608174596)(" \
#            "4.416666666666667,0.080663351371148)(4.5,0.041306961243205986)(4.583333333333333,0.03044873786965352)(" \
#            "4.666666666666667,0.0833190402255618)(4.75,0.06635781688370002)(4.833333333333333,0.11421493965838547)(" \
#            "4.916666666666667,0.17694407917295363)(5.0,0.095970115329991)"
# ron = "(0.16666666666666666,0.054023700241486394)(0.3333333333333333,0.01588680608257753)(0.5,0.032340175971085516)(" \
#       "0.6666666666666666,0.035002456329140896)(0.8333333333333333,0.011726632859257347)(1.0,0.009997593531240856)(" \
#       "1.0,0.05717161051842401)(1.1666666666666667,0.02016461768677036)(1.3333333333333333,0.010412291664277262)(1.5," \
#       "0.06372886014026458)(1.6666666666666665,0.037064767552647204)(1.8333333333333333,0.00959967735340439)(2.0," \
#       "0.022003732142110377)(2.0,0.07045918629835157)(2.125,0.032080477614050085)(2.25,0.020566935586175616)(2.375," \
#       "0.035061270066559236)(2.5,0.043463699723881644)(2.625,0.03369593715819852)(2.75,0.027017417627986817)(2.875," \
#       "0.017428381653430636)(3.0,0.021266521631402635)(3.0,0.1036071508987898)(3.0588235294117645," \
#       "0.04954374392930716)(3.1176470588235294,0.022990256782397744)(3.176470588235294,0.03164579260891742)(" \
#       "3.235294117647059,0.020527025441055446)(3.2941176470588234,0.05507505652043965)(3.3529411764705883," \
#       "0.04933253420741579)(3.4705882352941178,0.02601916740607413)(3.5294117647058822,0.004125391458897232)(" \
#       "3.588235294117647,0.029196458749644383)(3.6470588235294117,0.03121571412971902)(3.7058823529411766," \
#       "0.021571994639028924)(3.764705882352941,0.04349526512755153)(3.8235294117647056,0.05558943931957172)(" \
#       "3.8823529411764706,0.03952948681984547)(3.9411764705882355,0.016855949358024258)(4.0,0.03138126616378667)(4.0," \
#       "0.12750560873138683)(4.083333333333333,0.05458569344652242)(4.166666666666667,0.09782826004279632)(4.25," \
#       "0.08076871476490366)(4.333333333333333,0.07487238916590988)(4.416666666666667,0.0576133830637402)(4.5," \
#       "0.05289239570982529)(4.583333333333333,0.03218827444906702)(4.666666666666667,0.094801246426509)(4.75," \
#       "0.021929130537898134)(4.833333333333333,0.11874981309925858)(4.916666666666667,0.1340155328891317)(5.0," \
#       "0.09206238183812931)"
# voldemort = "(0.0,0.03936666516330389)(0.8333333333333333,0.07028986024765016)(1.0,0.013801808689667405)(1.0," \
#             "0.052813533093232556)(1.8333333333333333,0.09797217399434976)(2.0,0.1367589107693713)(2.0," \
#             "0.05481189653527829)(2.125,0.10868770237726721)(2.25,0.13240315588213747)(2.375,0.0556345618779398)(2.5," \
#             "0.055714351707065624)(2.75,0.13436439787045895)(2.875,0.09984088115365786)(3.0,0.0635779192635324)(3.0," \
#             "0.03638845556261139)(3.176470588235294,0.023288414535307722)(3.235294117647059,0.04197497185971755)(" \
#             "3.2941176470588234,0.08198705677004836)(3.3529411764705883,0.031130171549768715)(3.411764705882353," \
#             "0.020772449964888584)(3.4705882352941178,0.037555154924698186)(3.5294117647058822,0.031074608580872742)(" \
#             "3.7058823529411766,0.07152508107258093)(3.8235294117647056,0.06588264940296307)(3.8823529411764706," \
#             "0.0948769916056511)(4.0,0.06553653663811776)(4.083333333333333,0.19278779597040685)(4.166666666666667," \
#             "0.1599901026137759)(4.25,0.09289990136989035)(4.333333333333333,0.17565624345163033)(4.416666666666667," \
#             "0.18290546857241985)(4.5,0.12048023788514262)(4.583333333333333,0.12510629346171964)(4.666666666666667," \
#             "0.19571999158788644)(4.75,0.16597809025731391)(4.833333333333333,0.07441552436072385)(4.916666666666667," \
#             "0.1860592798438533)"
# datas = [hermione, ron, voldemort]
# names = ['Hermione', 'Ron', 'Voldemort']

meg = "(4.5099607,9.145459)(3.57413,9.0662775)(3.5041938,9.081636)(3.4137459,9.000664)(3.363038,8.866242)(3.2196476,8.789564)(3.336514,8.677338)(3.67762,8.499175)(3.5649667,8.337997)(3.5615878,8.298908)(3.3058891,8.368536)(4.411359,9.214104)(3.2917495,8.400075)(3.572686,8.079635)(3.5276706,7.8792367)(3.5218406,7.819681)(3.5725102,7.283179)(3.5694788,6.764239)(3.564716,6.409861)(3.5642204,6.320786)(3.5614207,6.2602897)(3.5108786,4.1908727)(4.3509064,9.292666)(3.4946973,4.240342)(3.489429,4.2161703)(3.5081418,4.156599)(3.4836624,3.9927704)(3.4858332,3.9810376)(3.4876406,4.0152354)(3.4760244,4.1220536)(3.48372,4.062978)(3.4633827,4.0681324)(3.3955011,0.88099146)(4.241013,9.220942)(3.4554677,0.8562715)(3.530878,0.6703262)(3.5720026,0.8179651)(3.519464,0.59453213)(3.6843014,0.42055798)(3.6399596,0.4366883)(3.7500453,0.424067)(3.7618566,0.33342305)(4.0158863,9.151562)(4.115068,9.066803)(3.9582112,9.206522)(3.8896604,9.35884)(3.6682746,9.320783)"
amy = "(-8.342304,-10.610808)(-9.04275,-10.060997)(-9.673887,-10.093517)(-9.451507,-9.894799)(-9.805856,-10.021437)(-10.046675,-9.8279)(-9.802068,-9.778855)(-10.02607,-9.885238)(-9.633703,-9.747921)(-9.800576,-9.574567)(-10.076173,-9.779362)(-8.397992,-10.55506)(-9.631561,-9.232356)(-9.934353,-9.219695)(-10.326742,-9.217409)(-10.299923,-9.105268)(-10.272848,-8.962244)(-10.114175,-8.881637)(-10.313372,-8.93368)(-9.729081,-8.846545)(-9.693886,-8.706198)(-9.88598,-8.648996)(-8.406389,-10.479309)(-9.358188,-8.688009)(-8.273186,-8.576298)(-8.297483,-8.667865)(-8.266495,-8.644202)(-8.0628805,-8.617887)(-8.164219,-8.62559)(-8.125448,-8.616445)(-8.125835,-8.620081)(-7.810387,-8.408485)(-7.792922,-8.411057)(-8.514099,-10.614926)(-7.28948,-8.103061)(-7.281028,-8.09644)(1.7779036,-0.83017725)(1.8701068,-0.77361786)(2.7121656,-0.16919155)(3.0169158,-0.09458717)(2.9432204,-0.047557563)(3.1993005,0.0181159)(-8.582332,-10.427661)(-8.679336,-10.478853)(-8.920881,-10.344939)(-8.824386,-10.267015)(-8.461559,-9.987007)"
beth = "(3.399134,-8.2278385)(3.9947112,-7.8537307)(4.061526,-7.8462396)(4.165823,-7.5131683)(4.0054226,-7.345303)(4.0395436,-7.191584)(4.0945888,-7.213176)(3.932565,-6.940311)(3.700814,-7.0141015)(3.6766925,-6.587878)(3.5778377,-6.2286468)(3.485731,-8.295013)(3.5197384,-6.2659173)(3.2941034,-6.1130967)(3.408607,-6.144191)(3.4197803,-5.8867893)(3.4845016,-5.838639)(3.4017882,-5.723489)(3.138255,-5.4674745)(3.1901884,-5.452265)(3.2916765,-5.3035164)(3.211435,-5.235973)(3.5488815,-8.21253)(3.2862277,-5.2513647)(3.2602026,-5.086409)(3.2939625,-5.0978804)(3.2242289,-4.5384245)(3.2285585,-4.3551507)(3.2287626,-4.2848268)(3.227612,-4.3508224)(3.3147044,-2.6714005)(3.3094282,-2.7399797)(3.314358,-2.743133)(3.5742745,-8.321654)(3.3214943,-2.7259347)(3.615556,-1.143696)(3.6386466,-0.9926742)(3.74747,-0.3511998)(3.859905,-0.05374667)(3.8619034,-0.062683135)(3.6643476,-8.259762)(3.773303,-8.295963)(3.9048634,-8.060958)(4.026101,-7.9769216)(4.0504045,-7.907703)"
joe = "(-5.6824794,4.460025)(-6.4085937,3.7616632)(-6.4715667,3.5910206)(-6.4541655,3.4378214)(-6.258584,3.3053043)(-5.971511,3.4570346)(-6.040031,3.2492507)(-6.1116266,2.9683256)(-5.6629906,3.1651464)(-5.606908,3.0784843)(-5.9818015,2.7563956)(-5.560352,4.4049788)(-5.9407244,2.6969256)(-5.762161,2.5101566)(-5.707371,2.3922527)(-5.725791,2.3947744)(-5.301888,2.408071)(-5.2534933,2.301176)(-5.171372,2.6046357)(-5.0860906,2.849026)(-5.225759,2.2410443)(-5.1457667,2.3276696)(-5.6619635,4.303816)(-4.7480364,2.6451597)(-4.52371,2.5354176)(-4.51918,2.5908763)(-4.123952,2.5323386)(-4.1186476,2.5123463)(-3.6114733,2.3727474)(-3.2577467,2.2763653)(-3.0931826,2.2395287)(-2.8423347,2.1711357)(-2.7230377,2.1433647)(-5.724335,4.2288923)(-2.4566236,2.0735948)(-2.2592647,2.0183697)(-2.0057557,1.9534389)(-1.5673388,1.8283334)(0.11418169,1.3523777)(0.44578424,1.2423322)(0.83989626,1.1366738)(2.4818993,0.7392258)(-5.8047485,4.1351876)(-5.882184,4.1038823)(-6.0010815,3.994064)(-6.180232,3.9289753)(-6.236088,3.9846852)"
datas = [meg, amy, beth, joe]
names = ["Meg", "Amy", "Beth", "Joe"]

for i, name in enumerate(names):
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()
    coordinates = datas[i].split(')')
    for j, coordinate in enumerate(coordinates):
        coord = coordinate[1:]
        coord = coord.split(',')
        if coord[0] != '':
            x = float(coord[0])
            y = float(coord[1])
            worksheet.write(j, 0, x)
            worksheet.write(j, 1, y)
    workbook.close()

