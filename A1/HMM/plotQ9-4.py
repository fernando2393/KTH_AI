import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [-6.068505769599569, -11.942898406665513, -28.9136995794595, -43.42900220338189, -56.739880465369055, -73.71421685484155, -84.13088885765562, -99.8385214357918, -114.60728697930905, -126.15538628102503, -137.63792227118563, -153.05244490812214, -168.1687860910999, -177.53187463639176, -192.78037185916085, -207.67009615272318, -219.74526922852402, -235.07559113070573, -249.38049974045623, -259.2671374984008, -270.8787593962698, -283.9704250959127, -298.65894852631743, -313.37454860099723, -327.1260648139473, -341.59066590344963, -353.9218339727222, -366.19677380256667, -384.10122334772666, -398.3586121575246, -411.0808501951189, -424.6483070163208, -436.20508351923075, -449.91840075977166, -462.01703903626577, -474.5571935924124, -487.73837671507204, -504.29985362282804, -515.5125129820569, -530.8279904050187, -544.3555852917011, -557.7921827958078, -571.5684473474663, -585.6514669017029, -597.3164182064512, -611.2288414837304, -626.3356877565935, -638.6694243663574, -651.6262395715331, -664.8449183806217, -678.9113721222185, -689.5073430066808, -702.6030475904033, -717.3872592849023, -730.3717666291969, -746.8873613544197, -759.9849937071076, -772.901816319955, -783.1530777528484, -795.922533065579, -810.8935078712174, -822.5073984992202, -837.5119119338107, -848.9901072864733, -862.3564749000059, -877.3519799986038, -884.3889977760616, -898.0356023455431, -910.2756382883941, -927.3217796157335, -942.3511512189099, -953.2652750726975, -965.6915304695608, -975.8786041076718, -992.5769545697174, -1003.0124606525011, -1016.0560661260943, -1034.606899236451, -1048.3482444547135, -1062.0565223415222, -1074.5048846354186, -1088.0894221546132, -1101.4414655033856, -1114.1202565264064, -1127.027832766008, -1141.1046961220377, -1153.524323663151, -1164.9633724065206, -1179.1534442022894, -1193.7721651677045, -1208.3920507991897, -1221.8378954140912, -1234.6788628912304, -1249.0160045000391, -1264.9954816833408, -1278.5995910186325, -1292.376821143764, -1304.8560441850777, -1317.6533732211553, -1331.6774246336356]) #Plot X
plt.plot([], 'ro')
fig.suptitle('Last Log Prob vs Number of Observations', fontsize=20)
plt.ylabel('Last Log Prob')
plt.xlabel('Number of Observations')
plt.show()

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [13.0, 22.0, 18.0, 32.0, 32.0, 44.0, 42.0, 38.0, 64.0, 65.0, 77.0, 81.0, 90.0, 103.0, 59.0, 47.0, 61.0, 61.0, 86.0, 98.0, 86.0, 69.0, 122.0, 84.0, 93.0, 162.0, 141.0, 152.0, 81.0, 98.0, 68.0, 116.0, 101.0, 73.0, 91.0, 98.0, 122.0, 105.0, 155.0, 178.0, 126.0, 145.0, 118.0, 112.0, 111.0, 97.0, 111.0, 145.0, 92.0, 79.0, 103.0, 109.0, 91.0, 125.0, 162.0, 141.0, 111.0, 128.0, 89.0, 111.0, 96.0, 97.0, 103.0, 121.0, 112.0, 78.0, 162.0, 156.0, 144.0, 187.0, 175.0, 209.0, 136.0, 209.0, 151.0, 180.0, 175.0, 223.0, 174.0, 176.0, 168.0, 272.0, 318.0, 260.0, 199.0, 210.0, 254.0, 176.0, 182.0, 161.0, 164.0, 160.0, 160.0, 171.0, 203.0, 169.0, 182.0, 157.0, 159.0, 160.0])
plt.plot([], 'ro')
fig.suptitle('Number of Iterations vs Number of Observations', fontsize=20)
plt.ylabel('Number of Iterations')
plt.xlabel('Number of Observations')
plt.show()


fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [7.120871345165768, 14.586355176069677, 12.952063858646742, 12.485958180359795, 13.133771430985348, 9.236754827690092, 11.447550411304633, 10.1389431490325, 8.175896553308448, 10.518477737175303, 11.366183144753961, 9.104009686270444, 6.7001436690944445, 12.296905351316838, 9.943169595046811, 9.44403259605454, 8.965134244347553, 8.123735255660904, 7.7512456597609685, 10.314800657013961, 11.746672715645786, 11.130665075136278, 10.36635068103925, 8.424867833350902, 8.361503526013678, 8.427153177921468, 11.72017317729302, 13.510932366187262, 9.147573904119554, 9.89092356718254, 9.915479287889468, 10.856089321001093, 12.294693590368354, 12.580341396078893, 12.781555387568517, 11.668257093763657, 9.233700365447078, 7.226398592587202, 8.629541341181607, 8.010881128043025, 6.738010181203435, 7.292066074644822, 7.172983202233809, 5.815012822318977, 8.00177739432695, 6.786812847756551, 6.288495936265008, 7.000245413845619, 8.391886276765263, 9.082638398750987, 8.54014049790851, 7.6084219108500974, 8.359921673834265, 8.048591831319868, 8.510620892544125, 6.166843257159826, 6.8057971765598495, 8.657287817156657, 9.640270991565671, 10.62240901777136, 9.451703899914605, 9.843840552402753, 8.959103588946732, 10.836917683200227, 10.614702510700454, 7.430711203001351, 14.103236476244206, 13.519699722751284, 14.149203969117366, 9.708802808317841, 8.310217302909791, 10.424623897877723, 11.23948411714889, 14.544411657780643, 11.592039327075554, 14.791030374087995, 14.45753213226294, 9.35197093942952, 9.759054691293613, 9.684792015512585, 10.613012530954848, 11.46542676407853, 11.082797850764337, 11.843018597998253, 12.593668937026905, 12.98321900165638, 12.501583850797033, 12.169552063473475, 12.110471998943467, 13.14266498058214, 13.147667689442187, 12.999849648952477, 13.12502705234192, 12.841835544299556, 11.2388038056597, 10.890791119264577, 10.816280824935802, 11.700116077058738, 11.394044133537818, 11.25267647656824])
plt.plot([], 'ro')
fig.suptitle('Probability Error vs Number of Observations', fontsize=20)
plt.ylabel('Probability Error')
plt.xlabel('Number of Observations')
plt.show()