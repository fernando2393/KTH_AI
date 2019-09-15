import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [-8.849398734897404, -13.688691381081211, -35.84702459948117, -50.70051027711441, -64.96084270006303, -76.41737718846262, -89.57024906796633, -101.58563790386367, -114.25319366573538, -127.73988190598779, -140.10619043289375, -155.17628212202908, -167.83007348992223, -185.1970096735886, -197.64824449763228, -211.4791147134426, -224.70951269504533, -238.9054971869952, -253.68498321009073, -266.69249717178866, -280.1363554291987, -293.4397662318738, -306.9958728093323, -319.7543148246165, -333.61794847226446, -347.8718084086628, -363.8214974481885, -376.8313262706404, -389.7385685085578, -406.1694680627048, -418.4146179557307, -433.3756196890415, -445.78267255796055, -460.347507375852, -472.9077956932286, -486.4679831037896, -499.75350992567957, -514.6940336337614, -527.1656085523989, -542.0028744573085, -554.8420608553502, -568.3551995846366, -582.3601697518066, -595.4141124462066, -608.4219126855353, -621.3319604162824, -635.242938356535, -649.203380454122, -662.4385164190794, -676.086200794069, -689.6063749662284, -700.368398292431, -713.6120548423946, -727.5856169898161, -740.5990334907541, -754.5546924772532, -767.458429439541, -781.9212452607109, -793.193900300115, -806.6423682070499, -821.3274492575761, -833.3819982775331, -847.3635324518469, -861.005049448956, -874.7990179586594, -887.8300557615331, -901.3250312108509, -914.7520549992984, -927.7532606630488, -939.3011247972779, -953.43358168462, -966.5700036835984, -979.7721884126735, -993.2916543380713, -1006.9487290589151, -1021.2316342418195, -1034.1920195608895, -1047.0166581606172, -1060.8863541322391, -1074.923980815392, -1087.4729519194384, -1101.8986300382935, -1114.8545667072656, -1128.519727792323, -1141.9956232325324, -1156.4888117727392, -1168.6326950159994, -1180.8280712961703, -1195.102955400543, -1210.0103678580688, -1224.2547664587232, -1237.9160807865362, -1250.251550163213, -1263.7069788107212, -1279.1252666386213, -1292.8385531350762, -1306.4383195733271, -1319.6814108520198, -1332.697707727618, -1347.117012075538]) #Plot X
plt.plot([], 'ro')
fig.suptitle('Last Log Prob vs Number of Observations', fontsize=20)
plt.ylabel('Last Log Prob')
plt.xlabel('Number of Observations')
plt.show()

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [21.0, 8.0, 4.0, 25.0, 24.0, 23.0, 4.0, 6.0, 2.0, 3.0, 3.0, 4.0, 5.0, 32.0, 2.0, 80.0, 3.0, 4.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 10.0, 3.0, 3.0, 2.0, 3.0, 2.0, 2.0, 2.0, 3.0, 3.0, 7.0, 9.0, 2.0, 9.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 33.0, 10.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 4.0, 2.0, 6.0, 2.0, 4.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
plt.plot([], 'ro')
fig.suptitle('Iterations Array vs Number of Observations', fontsize=20)
plt.ylabel('Iterations Array')
plt.xlabel('Number of Observations')
plt.show()


fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [1.358759840095967, 1.4075413022330652, 1.158254246195137, 1.145719907898016, 1.161482729571402, 1.1332861886758916, 1.1496183875601271, 1.1559109753511858, 1.1844027840117122, 1.1805787965519152, 1.1892471759553833, 1.195325214911591, 1.1811287535701775, 1.1896412485911472, 1.1935567787115178, 1.3366115365851925, 1.265063755944614, 1.2690506148404854, 1.267591366923505, 1.2225957582524565, 1.2198968226949363, 1.216905381851339, 1.2299888519276931, 1.2337784350757244, 1.2376580986211518, 1.2414608204877287, 1.236306848756508, 1.2475730992611598, 1.2283688446952712, 1.2236034096924515, 1.231765936153367, 1.233182145825941, 1.2353745218479337, 1.2375741972328536, 1.2402577389621174, 1.1905781467440653, 1.171642515118933, 1.1720522397747202, 1.1505091265889669, 1.1530523014769574, 1.1552782831439101, 1.157476530817829, 1.1616467374324602, 1.1636599464264583, 1.1588874359705297, 1.160815081762551, 1.1631202527750468, 1.1684237261201038, 1.1688509763368335, 1.1703432732873913, 1.1709772773619112, 1.1327395221809082, 1.1382624665968513, 1.1361254880781844, 1.1359632285285859, 1.1410107735526431, 1.1394239417639078, 1.14427330769347, 1.1214007120001872, 1.1215492648988092, 1.120624573554799, 1.1178575684775358, 1.120129859800889, 1.1212738928071055, 1.118577155680038, 1.1133116528281422, 1.1143167764566249, 1.1133868144999546, 1.1170725691798946, 1.0865395803389488, 1.086792124395152, 1.0874209435411193, 1.0880766191672007, 1.0890793120449858, 1.0918319862776675, 1.0915311723925747, 1.0895184392402428, 1.0874721854200633, 1.0895572736435115, 1.0910101749124956, 1.0922826095706333, 1.0930415195434868, 1.0931773355412324, 1.0935831605282806, 1.0921818774129217, 1.09178513380449, 1.0835282291603956, 1.0795043640089843, 1.0827234879575665, 1.0827104566203696, 1.0837076570911173, 1.0870608464636005, 1.088394441358678, 1.0894488363081853, 1.0874625655885155, 1.0869980308081684, 1.0878630730718677, 1.0887211535147794, 1.089921410242176, 1.0918124924637473])
plt.plot([], 'ro')
fig.suptitle('Error A vs Number of Observations', fontsize=20)
plt.ylabel('Error A')
plt.xlabel('Number of Observations')
plt.show()


fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [0.6895129624929829, 1.1224971383377733, 0.8557509601867657, 0.6354432784153594, 0.8816637610063293, 1.0462158904575316, 0.9597452770474454, 0.9576388958311001, 0.9316436620053913, 0.9182243229561755, 0.8875227853067311, 0.8537546737661782, 0.8208821320077088, 0.7444615470686383, 0.7496135916080544, 0.9480460277182324, 0.9707645497765947, 1.0041135809987722, 0.9854000281421291, 0.9883178212788567, 0.9841386565944213, 0.9903529965239943, 0.9972238988112915, 1.0047473402851288, 1.003074424234175, 0.9129104945845721, 0.9150425710072074, 0.9065811181205636, 0.8999850999292992, 0.9064234197332068, 0.9032692773919828, 0.9135432466139876, 0.9098909972402136, 0.9306758403094839, 0.9373949822428473, 0.9816948242410044, 1.0432730828471148, 1.052712226245836, 1.0994764111318656, 1.105032787830931, 1.1062443595004465, 1.106088699450968, 1.1095729815518098, 1.1137496436719951, 1.1153561969130732, 1.1177358715903305, 1.1157155913719357, 1.1177350184462225, 1.118864971935879, 1.11524086372977, 1.1122101701690854, 1.111225976254231, 1.1093581673268367, 1.1111573497769307, 1.1127373726712506, 1.1115485289492801, 1.110910510234377, 1.111630226493242, 1.1137506695055717, 1.1149196705474498, 1.1184239586768079, 1.118225006337228, 1.120511529160704, 1.1215517118134561, 1.1254351974673635, 1.1285495364201552, 1.1272965750662018, 1.1272528139704407, 1.1242398358464325, 0.9880522614947721, 0.9463622497818731, 0.9380460241533288, 0.9312576404304314, 0.925915743938129, 0.9225176113511895, 0.9187850635102464, 0.9194457197141341, 0.9192076521831801, 0.9239441163550594, 0.9263795404358326, 0.9263400609772261, 0.9250876195605293, 0.9153131469135958, 0.9102573848004243, 0.902585410439455, 0.8987863095416763, 0.879413305546492, 0.8764737822863441, 0.8622062667173701, 0.8621742134436873, 0.862176972651591, 0.8579858417016658, 0.8524827830347431, 0.8490450558080095, 0.8492676956991921, 0.8472187996708705, 0.8499344348434017, 0.8531307693955108, 0.8577349263681655, 0.8605367488012894])
plt.plot([], 'ro')
fig.suptitle('Error B vs Number of Observations', fontsize=20)
plt.ylabel('Error B')
plt.xlabel('Number of Observations')
plt.show()

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [3.3306690738754696E-16, 1.1102230246251565E-16, 2.220446049250313E-16, 1.012696995822751E-127, 1.3322676295501878E-15, 5.551115123125783E-16, 1.7763568394002505E-15, 2.220446049250313E-15, 1.1102230246251565E-16, 3.3306690738754696E-16, 7.771561172376096E-16, 6.661338147750939E-16, 3.885780586188048E-15, 9.992007221626409E-16, 4.884981308350689E-15, 3.6637359812630166E-15, 1.1102230246251565E-14, 8.881784197001252E-16, 5.329070518200751E-15, 6.661338147750939E-16, 6.661338147750939E-16, 6.439293542825908E-15, 3.1086244689504383E-15, 1.5543122344752192E-15, 8.215650382226158E-15, 2.9976021664879227E-15, 5.10702591327572E-15, 1.5543122344752192E-15, 2.1094237467877974E-15, 2.6645352591003757E-15, 1.021405182655144E-14, 1.3322676295501878E-15, 1.4432899320127035E-15, 3.774758283725532E-15, 2.4424906541753444E-15, 4.440892098500626E-16, 2.220446049250313E-15, 4.440892098500626E-16, 7.549516567451064E-15, 4.884981308350689E-15, 4.6629367034256575E-15, 2.220446049250313E-15, 4.6629367034256575E-15, 2.4424906541753444E-15, 7.993605777301127E-15, 2.3314683517128287E-15, 3.774758283725532E-15, 6.661338147750939E-15, 1.532107773982716E-14, 8.43769498715119E-15, 5.551115123125783E-15, 7.771561172376096E-15, 5.995204332975845E-15, 5.329070518200751E-15, 1.3322676295501878E-14, 7.771561172376096E-15, 6.217248937900877E-15, 1.27675647831893E-14, 7.105427357601002E-15, 6.439293542825908E-15, 8.659739592076221E-15, 3.774758283725532E-15, 1.1102230246251565E-16, 3.552713678800501E-15, 1.6209256159527285E-14, 2.8421709430404007E-14, 2.1316282072803006E-14, 1.9761969838327786E-14, 6.661338147750939E-16, 9.325873406851315E-15, 1.0436096431476471E-14, 2.220446049250313E-15, 3.774758283725532E-15, 1.7763568394002505E-15, 1.4432899320127035E-14, 2.4424906541753444E-15, 1.176836406102666E-14, 3.3306690738754696E-15, 4.884981308350689E-15, 8.43769498715119E-15, 9.992007221626409E-16, 1.2656542480726785E-14, 1.2656542480726785E-14, 2.220446049250313E-16, 4.218847493575595E-15, 1.9539925233402755E-14, 5.662137425588298E-15, 1.554312234475219E-14, 4.440892098500626E-15, 2.4424906541753444E-15, 1.554312234475219E-14, 2.886579864025407E-14, 7.771561172376096E-16, 2.2537527399890678E-14, 1.3655743202889425E-14, 1.887379141862766E-15, 2.120525977034049E-14, 1.1102230246251565E-14, 1.3322676295501878E-15, 4.9960036108132044E-15])
plt.plot([], 'ro')
fig.suptitle('Error pi vs Number of Observations', fontsize=20)
plt.ylabel('Error pi')
plt.xlabel('Number of Observations')
plt.show()