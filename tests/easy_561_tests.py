from easy_561_canon import Solution as SolutionCanon
from chatgpt_easy_561 import Solution as SolutionChatGPT
from claude_easy_561 import Solution as SolutionClaude
from gemini_easy_561 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.arrayPairSum([1, 4, 3, 2]) == 4
    assert solution.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9

def run_advanced_tests(solution):
    assert solution.arrayPairSum([1375, -1930, 181, 1787, 8555, -4929, -9209, -8304, -3311, -3433, -973, -3730, -6059, 478, -2362, -6069, -7004, 1119]) == -28156
    assert solution.arrayPairSum([285, 8133, -8755, 6352, -6025, 5430, -2333, -7781, 8983, -4726, -3457, 7959]) == -3467
    assert solution.arrayPairSum([8483, -56, 8040, -5108]) == 2932
    assert solution.arrayPairSum([-3984, -1368, 5233, 1695, 567, -9391, 818, -918, -517, -2946, -208, -4871, 1484, 4618, -7313, 6287, -692, 374, 281, 2451]) == -8627
    assert solution.arrayPairSum([-7699, -3122, -8872, 5907, -8020, 1550, -3699, 3380, 1168, 6810, -1947, 2399, 6208, 8359, 9794, 1756]) == 1178
    assert solution.arrayPairSum([9940, 534, -3655, -1745, 2096, 3725, -4096, -4439]) == -3835
    assert solution.arrayPairSum([1085, -8664, -1696, -3398]) == -10360
    assert solution.arrayPairSum([1322, -4697, 8238, 2445, 5605, 4612, -162, -9445]) == -1557
    assert solution.arrayPairSum([6119, -5640, 3598, 9215, 5639, 8561, -197, -71, 4827, 4620, 5426, 7975, 7961, -3860, 4085, 3781]) == 28834
    assert solution.arrayPairSum([3390, 7758, -9854, 91, -325, 9533, 6082, -8044, 1638, 8934, -7126, -859, -7720, -4757, 1625, 3063, -8298, -1690]) == -7335
    assert solution.arrayPairSum([-6069, 7736, 8082, -1891, 2456, 7418, 3031, -8514, 7192, -3337, -3289, -4, -6839, 9930]) == 655
    assert solution.arrayPairSum([7455, -4224, -5167, 8794, -387, 2833, 2631, 9493, -3948, -7650, -8811, 2031, 4772, 3185, 3673, -8124]) == -1690
    assert solution.arrayPairSum([-5782, 4377, -7233, 8579, -7526, 1408, 7106, -6056, 2819, 3010]) == -2058
    assert solution.arrayPairSum([-737, 5560, 1792, 9778, -8929, -689, -1498, 4703, 944, 2072, -5238, -5905, -4515, -8617, 5550, 3042, 8046, 1922, 9936, 1303]) == 4763
    assert solution.arrayPairSum([8194, 3746, 1447, -8565, -5327, 5402]) == -1716
    assert solution.arrayPairSum([-7396, 3757, 2689, 8639, 5662, 8730]) == 5000
    assert solution.arrayPairSum([-7822, -5987, 1972, 7163, -2938, 1462, 9730, -5350, -9838, -9893, 7973, -7538, -5558, 8313, 3407, 3269, 1543, 1082, 8372, -4004]) == -8804
    assert solution.arrayPairSum([2956, -5070, 917, 1681]) == -3389
    assert solution.arrayPairSum([-9980, 4964, 9773, -2708, -9826, 8596]) == -4092
    assert solution.arrayPairSum([-5406, 2604, 6385, -7610, -4593, -368, 1170, -368, -2268, -7499, 4909, 1627, -2103, -8506, -7889, 4051, 3303, -6995, 9114, -9209]) == -18429
    assert solution.arrayPairSum([1567, 7739, 6547, -5731, -406, 3919, -8645, 9297, 1910, 3747, 3661, -2802, -1161, 6703, -1220, 870, 68, -9029]) == 4427
    assert solution.arrayPairSum([-9471, -2357, 876, 3486, -3519, 813, 494, 6133, 7405, -271]) == -4325
    assert solution.arrayPairSum([1998, -9503, -4302, 3775, -2954, 5403, -7181, 5459, -4887, -8190, 1704, 9324]) == -10048
    assert solution.arrayPairSum([-9313, 2101, -5373, -2986, 2275, 1177, 7234, -4350, -6943, -1116, 2836, 9715, -3623, 8462, -5528, 4643]) == -5620
    assert solution.arrayPairSum([9002, 8201, -485, -9091, -9797, 9450, 9131, 4852, -4232, -4012, 9412, -4485, -795, 8236, 7188, 5849, -8651, 2881]) == 11870
    assert solution.arrayPairSum([-6931, 4759, 8723, 5132, -5878, -9751, -352, -3518, -106, 5213, 9748, -8062]) == -6451
    assert solution.arrayPairSum([-9494, 8824, -8213, 848, 5611, 434, -8298, -6425, 9441, -2268]) == -10303
    assert solution.arrayPairSum([167, 689, 5973, -431, -7583, 2115, -8780, -7895, -1493, -9621, -1335, -213, 329, -941, 298, -925, -7271, -8273]) == -25731
    assert solution.arrayPairSum([-5097, -5298, 4831, 7514, -8546, 8219, -750, -3392, 525, 3512]) == -3367
    assert solution.arrayPairSum([-1569, 9960, -9727, -613, -8203, -9495, 3586, -8544, -5401, 7337, 8965, 2727, 9891, -5126, 4019, 362]) == -4065
    assert solution.arrayPairSum([-8231, -2487, -4451, -6941, -3559, -7312, -7578, 6075, 2940, 9658, 8205, 1745, -6529, 4017]) == -11664
    assert solution.arrayPairSum([3222, -7764, 741, 1101, 3617, 386]) == -3801
    assert solution.arrayPairSum([604, -4366, -7721, 1783]) == -7117
    assert solution.arrayPairSum([-6428, -7631, -8436, 2816, 8419, -9078, -1627, 1225]) == -15520
    assert solution.arrayPairSum([3981, -4184, 3140, -59]) == -1044
    assert solution.arrayPairSum([5196, -6408, 523, -1363, -5455, -8850]) == -13782
    assert solution.arrayPairSum([-2241, -8683, 422, 1301, -4630, 1360, -248, 4259, -1858, 301, 3578, -7508, 1636, -6208, -381, -7032, 4921, 1179]) == -14833
    assert solution.arrayPairSum([3344, -2120, -1237, -3537, -5877, 2406, 8812, 3646, -1928, -4070]) == -5290
    assert solution.arrayPairSum([-5625, 1369, 197, 175, 6124, -5400, 3209, -5111, -5703, -2900, 7272, 4935, -6053, -7001, 3482, 3193, 1666, -5896]) == -9290
    assert solution.arrayPairSum([-2370, 4206, -3238, -2635, 6649, -8568, 3778, 6229, -6642, 3111, 4102, -16]) == -734
    assert solution.arrayPairSum([1445, -6717, -6262, -1667, -5045, 6933, 9101, -6374, 7265, 93, -2620, 3421, 3771, 528]) == -3025
    assert solution.arrayPairSum([-3069, 6012, 1946, -8266, -247, 6320, -4236, -1748, 7815, 3275, 9366, 8158, -8655, 4417]) == 6202
    assert solution.arrayPairSum([-6969, 1020, -9525, -393, 8688, -8138]) == -15474
    assert solution.arrayPairSum([1865, -1718, -4406, 6634, 6051, -7502, -8526, -4176, -9378, -4905, -6489, -694, 5426, -6168]) == -21256
    assert solution.arrayPairSum([-450, 5144, -6803, 814, 6666, 9805, 9595, -8948, -5530, 7285, 9840, -1212, 1896, 2865, -655, 585, 5622, -633]) == 10808
    assert solution.arrayPairSum([4917, -3726, -6266, 989, 4473, 9517, -1825, -8847, 412, 9490, 8583, -270, 7559, -1801, -3639, -4615, -1721, -3073, -7611, -1145]) == -2924
    assert solution.arrayPairSum([8679, 7012, 9442, 5086, 9895, 9855, -1336, 3016, -8272, -7368, 7424, 3881]) == 19819
    assert solution.arrayPairSum([-3290, -7181, 6318, 1918, 3726, 1989, 9349, 8873, -6351, -4908, -744, 4573, 8184, -5543]) == 4821
    assert solution.arrayPairSum([7004, -5318, -6799, -5408, 1228, 8559, -7431, 336, -6372, 7748]) == -10145
    assert solution.arrayPairSum([-2295, -6495, 3957, 6330, 481, -3645, 8858, 1566, 4909, -8070, -2710, -1416, 3335, 197, -1664, -5, 2411, -4711, 7083, -5112]) == -3448
    assert solution.arrayPairSum([-6555, -8419, 395, -6844, -1153, 4]) == -14970
    assert solution.arrayPairSum([3383, 7928, 2628, 1373, 1363, -6392, 4257, 9750, -1929, 6463, -2577, 83]) == 7855
    assert solution.arrayPairSum([-3155, 6476, -5006, 9860]) == 1470
    assert solution.arrayPairSum([-2465, -2999, -9685, 6037, -8068, 9133, 6382, -3573, -5244, 3899, 3234, -8779, -2890, -7376, 4642, -1896, 3198, 3560]) == -10679
    assert solution.arrayPairSum([-555, -4001, -2445, 9299, 6752, 4416, 7532, -2110, 8240, 8700, -3220, -27, -4294, 3263]) == 10997
    assert solution.arrayPairSum([-3313, 4881, -5169, -7914, 5414, 8591, 5520, 9300, 6137, 9407, 9911, 1516, -42, 1114]) == 18286
    assert solution.arrayPairSum([5734, 7767, 623, -4281]) == 1453
    assert solution.arrayPairSum([-4724, -4269, 6843, -7055, -4335, 1020]) == -10370
    assert solution.arrayPairSum([-5054, -9827, 2025, 1822, 6802, 5057]) == -2948
    assert solution.arrayPairSum([-7745, 3341, -9082, 7846]) == -5741
    assert solution.arrayPairSum([-1546, -6179, -9668, 1544, 1248, -570, 5978, 2959]) == -7007
    assert solution.arrayPairSum([2808, 4571, -3341, 6772, -4197, 6280, 3634, 1166, 5330, 6611, -6765, 2505, -738, 7401, 2315, -6463, 9588, -2720]) == 12965
    assert solution.arrayPairSum([9058, 8671, -3479, -803, 4819, -433, -8761, 6303, -8866, 395]) == 712
    assert solution.arrayPairSum([-7997, -2479, -5570, -1253, 5721, 446, 4178, -4370, 1710, 2987, 4779, 9531, 1072, 6741, -2021, -2756, 8263, -9711, -6905, -4465]) == -5540
    assert solution.arrayPairSum([-3748, 7942, -2006, 6911, -3044, -3488, 1085, 1272]) == 1204
    assert solution.arrayPairSum([6052, 294, 3233, 5446, -5100, -8683, 7492, 4289, -8039, -3271, 211, -7123]) == -8442
    assert solution.arrayPairSum([4159, 5476, 8427, 7771, 7842, 5950, -1858, 98, 9068, 6480, -305, 2561]) == 24547
    assert solution.arrayPairSum([9076, 9228, -888, -4106, -111, 3975]) == 4859
    assert solution.arrayPairSum([-4355, 3952, 1425, -2594, 4830, 5391, 7272, 9769, 9588, 555, 7563, -1389, 1503, 1225, -3397, 5414, 6603, 4919]) == 26176
    assert solution.arrayPairSum([3755, -2619, -7929, -817, -5496, -4246, 5875, 1700]) == -9237
    assert solution.arrayPairSum([-6159, -3404, -3832, 3196, 5428, 8965, -6028, 3213, 1668, -3910, 1366, -571]) == -3483
    assert solution.arrayPairSum([8, -4693, -2600, 2621, -4387, -4344, -5784, 9290, 2687, 878]) == -9206
    assert solution.arrayPairSum([-3869, -4279, -8849, 8230, -2045, 3243, -7850, 3805, 7251, 4031, 9824, -4600, -4248, -6088, -8968, -6180, 8114, 2864, 201, -2995]) == -10949
    assert solution.arrayPairSum([1647, -3125, -9006, 7052, 4611, -6976]) == -7520
    assert solution.arrayPairSum([3389, 2818, -4356, -9577, -2108, -8055, -4018, 7970, -2548, -2449, -3039, 2242, 231, -6429, -2688, -6589, -1151, 4241, -1164, 1425]) == -20884
    assert solution.arrayPairSum([-8631, -4432, 4478, 7375]) == -4153
    assert solution.arrayPairSum([5868, 1867, -6390, 1630, -8980, -9695, -9069, 977]) == -15831
    assert solution.arrayPairSum([-5561, -9469, -70, 1323, 3628, 5689, -2475, 989, -3101, 8439, 1351, 365, -4918, -3999, 6051, -9575]) == -10243
    assert solution.arrayPairSum([-6284, 3271, -3599, 8682, -466, -7399, 7432, -9030, -7430, -2461, -2937, -2983, -6901, -6843, -531, 2749, 7728, -6248, 6662, 3083]) == -17957
    assert solution.arrayPairSum([-6395, -1508, 3390, 4761, 7871, 9601, 7181, -6794, 966, 1492, -4694, -4837, 1809, 2521, -6768, 9408, 3335, -8862, -6358, 1015]) == -1724
    assert solution.arrayPairSum([3255, 4183, 5658, 113]) == 4296
    assert solution.arrayPairSum([74, 133, -2181, 1249, 8362, -4350, 9684, 3414]) == 5335
    assert solution.arrayPairSum([1464, -7111, -5679, -9344, 7724, 1890, 1801, -1925, -2710, -7523, 8337, -9458, 6939, -3292, 3082, 8827, 8320, -8042, -535, 8506]) == -2709
    assert solution.arrayPairSum([-4920, 2904, -484, 1917, -9585, 7964, -9623, -5472, 6074, 5912, 4724, 3096]) == -1877
    assert solution.arrayPairSum([-6184, -8599, -6363, 277, 7000, 1155, 7146, 697, 6185, -7840, -2572, -3230, 4267, -9035]) == -13667
    assert solution.arrayPairSum([-5204, -6811, 4137, -9521, 295, 8363, -5967, 6859, 8495, 4581, 3295, 1168, -3593, -9094]) == -5002
    assert solution.arrayPairSum([-992, -3902, 199, 7280, -1542, -3761, -2712, 3557, -6727, -3900]) == -10774
    assert solution.arrayPairSum([5385, 232, 3274, 7586, 2532, -9575, -1167, -8476, -328, -6549, -6243, -3098, 2456, 7501, 7788, 1226]) == -2821
    assert solution.arrayPairSum([-5928, -7200, 8477, 2414]) == -4786
    assert solution.arrayPairSum([43, 2625, 9373, -5886, -6664, -5793, 1053, 934, 216, 1893]) == -8563
    assert solution.arrayPairSum([-4916, -8422, 6709, -4350, 3165, 8342, 9166, -5191, -1355, -2199]) == -4030
    assert solution.arrayPairSum([-141, -2522, 6927, 5128, 8482, -4289, 6636, -8747, 2666, 3076, -7015, 9759, -9230, 1418, 9835, 8543, -4925, 470, 4209, 9053]) == 14176
    assert solution.arrayPairSum([-98, 942, -804, -2165, 7552, -6472, 4669, -4786, 9545, 7783, -6993, 1816, -6690, -2936, 3028, -8350]) == -7821
    assert solution.arrayPairSum([563, 7239, 3758, -6152, 7118, -4837, -1356, -5725, -5040, 5977]) == -1672
    assert solution.arrayPairSum([4040, 108, 3250, -1503, 3621, 5399, 7161, 8136, -3243, -7817, -4817, -8712, 6912, 8092, -3782, 9364]) == 7653
    assert solution.arrayPairSum([7052, -604, -2365, 7399, 5031, -7449, -1418, -1049, -1232, -6106, -7916, -7820, 7047, -9890, -8379, 5419, -4118, 3512, 6845, -3764]) == -14646
    assert solution.arrayPairSum([246, -6046, -3125, 2452, -2273, -942, 847, 4685, -1920, -5085]) == -8393
    assert solution.arrayPairSum([4212, -5152, 6134, -9170, -8267, 9608, -5113, -8864, 8093, -3331]) == -10245
    assert solution.arrayPairSum([1260, -9341, -2533, -361, 9813, -1780, 6864, -5248]) == -5371
    assert solution.arrayPairSum([-5673, 8447, -2794, -5585, -4564, 6780]) == -3457

def run_timed_tests(solution):
    assert solution.arrayPairSum([1375, -1930, 181, 1787, 8555, -4929, -9209, -8304, -3311, -3433, -973, -3730, -6059, 478, -2362, -6069, -7004, 1119]) == -28156
    assert solution.arrayPairSum([285, 8133, -8755, 6352, -6025, 5430, -2333, -7781, 8983, -4726, -3457, 7959]) == -3467
    assert solution.arrayPairSum([8483, -56, 8040, -5108]) == 2932
    assert solution.arrayPairSum([-3984, -1368, 5233, 1695, 567, -9391, 818, -918, -517, -2946, -208, -4871, 1484, 4618, -7313, 6287, -692, 374, 281, 2451]) == -8627
    assert solution.arrayPairSum([-7699, -3122, -8872, 5907, -8020, 1550, -3699, 3380, 1168, 6810, -1947, 2399, 6208, 8359, 9794, 1756]) == 1178
    assert solution.arrayPairSum([9940, 534, -3655, -1745, 2096, 3725, -4096, -4439]) == -3835
    assert solution.arrayPairSum([1085, -8664, -1696, -3398]) == -10360
    assert solution.arrayPairSum([1322, -4697, 8238, 2445, 5605, 4612, -162, -9445]) == -1557
    assert solution.arrayPairSum([6119, -5640, 3598, 9215, 5639, 8561, -197, -71, 4827, 4620, 5426, 7975, 7961, -3860, 4085, 3781]) == 28834
    assert solution.arrayPairSum([3390, 7758, -9854, 91, -325, 9533, 6082, -8044, 1638, 8934, -7126, -859, -7720, -4757, 1625, 3063, -8298, -1690]) == -7335
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 561
    output = ''
    if sys.argv[1] == 'test':
        solvers = [SolutionCanon()]
        if len(sys.argv) == 3 and sys.argv[2] == 'all':
            solvers.extend([SolutionChatGPT(), SolutionGemini(), SolutionClaude()])
        for solver in solvers:
            run_basic_tests(solver)
            run_advanced_tests(solver)
    elif sys.argv[1] == 'time':
        import time, statistics
        solver = {
            'canon': SolutionCanon,
            'chatgpt': SolutionChatGPT,
            'claude': SolutionClaude,
            'gemini': SolutionGemini,
        }[sys.argv[2]]()
        times = []

        output += f'easy_561,{sys.argv[2]},'
        if problem_id == 527 and sys.argv[2] == 'claude':
            output += '-- NR --,'
            save_output(output)
            sys.exit(0)

        try:
            for _ in range(int(sys.argv[3])):
                start = time.perf_counter_ns()
                run_timed_tests(solver)
                end = time.perf_counter_ns()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            output += '-- IR --,'
            save_output(output)
            sys.exit(0)

        avg_time = statistics.mean(times)
        total_time = sum(times)
        output += f'{avg_time:.4E},{total_time:.4E}'
        save_output(output)