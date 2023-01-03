vals = [
    [
        "DateTime","Temperature","Humidity","Wind Speed","general diffuse flows","diffuse flows","Zone 1 Power Consumption","Zone 2  Power Consumption","Zone 3  Power Consumption"
    ],
    ["1/01/2017 0:00",6.559,73.8,0.083,0.051,0.119,34055.6962,16128.87538,20240.96386],
    ["1/01/2017 0:10",6.414,74.5,0.083,0.07,0.085,29814.68354,19375.07599,20131.08434],
    ["1/01/2017 0:20",6.313,74.5,0.08,0.062,0.1,29128.10127,19006.68693,19668.43373],
    ["1/01/2017 0:30",6.121,75,0.083,0.091,0.096,28228.86076,18361.09422,18899.27711],
    ["1/01/2017 0:40",5.921,75.7,0.081,0.048,0.085,27335.6962,17872.34043,18442.40964],
    ["1/01/2017 0:50",5.853,76.9,0.081,0.059,0.108,26624.81013,17416.41337,18130.12048],
    ["1/01/2017 1:00",5.641,77.7,0.08,0.048,0.096,25998.98734,16993.31307,17945.06024],
    ["1/01/2017 1:10",5.496,78.2,0.085,0.055,0.093,25446.07595,16661.39818,17459.27711],
    ["1/01/2017 1:20",5.678,78.1,0.081,0.066,0.141,24777.72152,16227.35562,17025.54217],
    ["1/01/2017 1:30",5.491,77.3,0.082,0.062,0.111,24279.49367,15939.20973,16794.21687],
    ["1/01/2017 1:40",5.516,77.5,0.081,0.051,0.108,23896.70886,15435.86626,16638.07229],
    ["1/01/2017 1:50",5.471,76.7,0.083,0.059,0.126,23544.3038,15213.37386,16395.18072],
    ["1/01/2017 2:00",5.059,78.6,0.081,0.07,0.096,23003.5443,15169.60486,16117.59036],
    ["1/01/2017 2:10",4.968,78.8,0.084,0.07,0.134,22329.11392,14710.0304,15822.6506],
    ["1/01/2017 2:20",4.975,78.9,0.083,0.055,0.152,22092.1519,14421.8845,15672.28916],
    ["1/01/2017 2:30",4.897,79.1,0.083,0.07,0.096,21903.79747,14104.55927,15597.10843],
    ["1/01/2017 2:40",5.02,79.7,0.081,0.051,0.134,21685.06329,13965.95745,15510.36145],
    ["1/01/2017 2:50",5.407,78.5,0.082,0.062,0.163,21484.55696,13612.15805,15336.86747],
    ["1/01/2017 3:00",5.169,77.9,0.083,0.066,0.108,21107.8481,13535.56231,15140.24096],
    ["1/01/2017 3:10",5.081,77.7,0.084,0.051,0.13,20998.48101,13371.42857,15059.27711],
    ["1/01/2017 3:20",5.041,77.2,0.081,0.062,0.152,20870.88608,13196.35258,15013.01205],
    ["1/01/2017 3:30",5.034,76.9,0.083,0.051,0.185,20870.88608,13167.17325,14897.3494],
    ["1/01/2017 3:40",4.896,76.6,0.085,0.07,0.137,20597.46835,13137.99392,14602.40964],
    ["1/01/2017 3:50",4.805,76.2,0.081,0.059,0.134,20421.26582,12908.20669,14590.84337],
    ["1/01/2017 4:00",4.753,75.7,0.083,0.044,0.134,20524.55696,12820.66869,14585.06024],
    ["1/01/2017 4:10",4.901,74.4,0.083,0.07,0.122,20482.02532,13032.21884,14452.04819],
    ["1/01/2017 4:20",5.203,74.1,0.085,0.062,0.096,20530.63291,12926.44377,14232.28916],
    ["1/01/2017 4:30",5.394,71.9,0.081,0.073,0.1,20512.40506,12948.32827,14157.10843],
    ["1/01/2017 4:40",5.156,74,0.079,0.062,0.148,20494.17722,12922.79635,14232.28916],
    ["1/01/2017 4:50",5.179,74.2,0.083,0.037,0.137,20311.89873,12879.02736,14243.85542],
    ["1/01/2017 5:00",4.934,72.9,0.082,0.055,0.134,20542.78481,12806.07903,14243.85542],
    ["1/01/2017 5:10",4.718,75.8,0.08,0.051,0.152,20621.77215,12853.49544,14105.06024],
    ["1/01/2017 5:20",5.546,74,0.082,0.055,0.093,20627.8481,12842.55319,14266.98795],
    ["1/01/2017 5:30",4.658,73.5,0.08,0.044,0.104,20797.97468,13137.99392,14353.73494],
    ["1/01/2017 5:40",4.382,76.9,0.081,0.073,0.148,20858.73418,13203.64742,14538.79518],
    ["1/01/2017 5:50",4.212,78.3,0.081,0.117,0.082,21393.41772,13575.68389,14862.6506],
    ["1/01/2017 6:00",4.308,77.2,0.081,0.062,0.126,22219.74684,14068.08511,14908.91566],
    ["1/01/2017 6:10",4.735,74.3,0.08,0.04,0.156,21928.10127,13852.88754,14729.63855],
    ["1/01/2017 6:20",4.769,75.6,0.082,0.099,0.063,21776.20253,13626.74772,14625.54217],
    ["1/01/2017 6:30",4.92,73.7,0.083,0.099,0.096,21654.68354,13582.97872,14480.96386],
    ["1/01/2017 6:40",4.408,76.7,0.082,0.037,0.119,21466.32911,13539.20973,14319.03614],
    ["1/01/2017 6:50",4.29,77,0.085,0.033,0.193,20846.58228,12908.20669,14018.31325],
    ["1/01/2017 7:00",4.304,76,0.082,0.048,0.152,19983.79747,12342.85714,13492.04819],
    ["1/01/2017 7:10",4.513,74.6,0.084,0.055,0.134,18908.35443,11897.87234,12630.36145],
    ["1/01/2017 7:20",4.489,74.3,0.082,0.081,0.119,18167.08861,11551.36778,11600.96386],
    ["1/01/2017 7:30",4.356,72.3,0.082,0.07,0.119,18075.94937,11263.22188,10640.96386],
    ["1/01/2017 7:40",4.478,72.2,0.083,0.073,0.089,18063.79747,10719.75684,10455.90361],
    ["1/01/2017 7:50",4.583,71,0.083,0.066,0.104,18045.56962,10924.01216,10496.38554],
    ["1/01/2017 8:00",4.794,72,0.084,0.187,0.145,18385.82278,10949.54407,10710.36145],
    ["1/01/2017 8:10",4.807,73.1,0.082,0.955,0.949,18987.34177,11347.11246,10837.59036],
    ["1/01/2017 8:20",4.757,73.5,0.083,3.188,3.134,19576.70886,11733.7386,10941.68675],
    ["1/01/2017 8:30",4.509,74.5,0.084,6.643,6.494,19837.97468,11945.28875,11178.79518],
    ["1/01/2017 8:40",4.346,74.8,0.082,12.64,10.13,20166.07595,12029.17933,11514.21687],
    ["1/01/2017 8:50",4.718,73.7,0.081,58.97,17,20676.4557,12426.74772,11959.51807],
    ["1/01/2017 9:00",4.704,71.8,0.083,82.5,20.15,21296.20253,12871.73252,12283.37349],
    ["1/01/2017 9:10",4.624,74.1,0.082,106.9,22.55,22043.5443,13203.64742,12427.95181],
    ["1/01/2017 9:20",4.629,74.8,0.083,132.1,24.3,22651.13924,13542.85714,12826.98795],
    ["1/01/2017 9:30",4.599,74,0.082,156.1,26.9,23131.13924,14046.20061,13121.92771],
    ["1/01/2017 9:40",4.524,74.7,0.081,182.4,28.19,23641.51899,14392.70517,13648.19277],
    ["1/01/2017 9:50",4.575,74.5,0.082,208.8,29.2,24668.35443,14830.39514,13850.60241],
    ["1/01/2017 10:00",5.124,73.7,0.076,234.8,29.23,25275.94937,15238.90578,14162.89157],
    ["1/01/2017 10:10",5.836,71.3,2.66,257.9,31.01,25920,15837.08207,14428.91566],
    ["1/01/2017 10:20",5.996,69.85,4.93,282.7,31.96,26393.92405,16059.57447,14671.80723],
    ["1/01/2017 10:30",6.22,68.81,4.924,307,32.42,26861.77215,16322.18845,15036.14458],
    ["1/01/2017 10:40",6.703,68.01,4.923,327.6,33.22,27511.89873,16774.46809,15267.46988],
    ["1/01/2017 10:50",6.993,66.14,4.918,349.6,33.41,28149.87342,17164.74164,15244.33735],
    ["1/01/2017 11:00",7.54,64.21,4.916,371.1,33.43,28714.93671,17507.59878,15591.3253],
    ["1/01/2017 11:10",8.22,61.9,4.916,388.2,33.89,29043.03797,17478.41945,15816.86747],
    ["1/01/2017 11:20",9.49,59.3,2.451,401.3,34.4,29261.77215,17792.09726,15932.53012],
    ["1/01/2017 11:30",10.65,56.03,0.084,419.5,35.29,29474.43038,17748.32827,16053.9759],
    ["1/01/2017 11:40",11.06,53.52,0.082,430.9,37.58,29523.03797,17963.52584,16256.38554],
    ["1/01/2017 11:50",12.4,53.26,0.08,437.5,43.46,29711.39241,18142.24924,16354.6988],
    ["1/01/2017 12:00",13.08,54.36,0.077,450.4,43.2,29644.55696,18131.30699,16562.89157],
    ["1/01/2017 12:10",14.38,54.42,0.076,470.5,37.92,29802.53165,18102.12766,16522.40964],
    ["1/01/2017 12:20",15.02,56.46,0.074,480,38.81,29887.59494,18156.83891,16649.63855],
    ["1/01/2017 12:30",15.55,58.7,0.075,486.1,39.46,30039.49367,18335.56231,16869.39759],
    ["1/01/2017 12:40",15.56,59.23,0.076,490.2,40.92,29966.58228,18204.25532,17094.93976],
    ["1/01/2017 12:50",15.49,59.3,0.076,495.9,40.9,29996.96203,18196.96049,17418.79518],
    ["1/01/2017 13:00",15.57,58.06,0.077,498.1,40.94,30258.22785,18466.8693,17413.01205],
    ["1/01/2017 13:10",15.65,58.7,0.077,498.1,42.75,30404.05063,18350.15198,17436.14458],
    ["1/01/2017 13:20",15.73,59.33,0.076,498.8,44.65,30094.17722,18331.91489,17332.04819],
    ["1/01/2017 13:30",15.68,58.6,0.079,497,44.26,30161.01266,18419.45289,17465.06024],
    ["1/01/2017 13:40",15.7,55.29,0.074,489.2,39.32,30318.98734,18310.0304,17164.33735],
    ["1/01/2017 13:50",15.75,52.45,0.077,482.4,38.65,30154.93671,18390.27356,16979.27711],
    ["1/01/2017 14:00",15.83,54.99,0.079,476.1,39.49,29984.81013,18353.79939,17054.45783],
    ["1/01/2017 14:10",15.79,56.66,0.076,467.7,39.94,30021.26582,18142.24924,17048.6747],
    ["1/01/2017 14:20",15.72,55.86,0.077,456.1,39.95,30021.26582,18113.06991,16950.36145],
    ["1/01/2017 14:30",15.8,54.06,0.075,449.2,41.52,29911.89873,18036.47416,16823.13253],
    ["1/01/2017 14:40",15.74,55.56,0.075,437.4,44.13,29747.8481,17996.35258,16684.33735],
    ["1/01/2017 14:50",15.72,56.69,0.077,422,43.87,29705.31646,17952.58359,16678.55422],
    ["1/01/2017 15:00",15.64,57.26,0.077,409,44.9,29571.64557,17894.22492,16753.73494],
    ["1/01/2017 15:10",15.69,57.96,0.074,391.8,46.89,29553.41772,17846.80851,16805.78313],
    ["1/01/2017 15:20",15.69,58.93,0.075,369.4,51.51,29383.29114,17525.83587,16649.63855],
    ["1/01/2017 15:30",15.6,58.7,0.073,321,57.14,29061.26582,17547.72036,16586.0241],
    ["1/01/2017 15:40",15.39,57.6,0.075,180.3,60.31,28885.06329,17770.21277,16476.14458],
    ["1/01/2017 15:50",15.34,58.7,0.075,149.5,67.85,28854.68354,17751.97568,16296.86747],
    ["1/01/2017 16:00",15.33,59.23,0.077,209.1,128.9,28836.4557,17646.20061,16256.38554],
    ["1/01/2017 16:10",15.48,57.46,0.074,265.1,219.1,28708.86076,17514.89362,16250.60241],
    ["1/01/2017 16:20",15.54,58.3,0.076,241.3,246,28556.96203,17325.22796,16192.77108]
]