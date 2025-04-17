from medium_122_canon import Solution as SolutionCanon
from chatgpt_medium_122 import Solution as SolutionChatGPT
from claude_medium_122 import Solution as SolutionClaude
from gemini_medium_122 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    # Test case from the task description
    assert solution.maxProfit([7,1,5,3,6,4]) == 7
    assert solution.maxProfit([1,2,3,4,5]) == 4
    assert solution.maxProfit([7,6,4,3,1]) == 0

def run_advanced_tests(solution):
    assert solution.maxProfit([6833, 4016, 3340, 9155]) == 5815
    assert solution.maxProfit([3803, 8280, 4943, 4289, 7018, 2284, 7118, 3127, 8286, 2506]) == 17199
    assert solution.maxProfit([9919, 9286, 5772, 1167, 5751, 2808, 6582, 2194, 267]) == 8358
    assert solution.maxProfit([2122, 7868, 4038, 5040, 6127]) == 7835
    assert solution.maxProfit([5140, 3521, 5338, 4001, 2055]) == 1817
    assert solution.maxProfit([8964, 1126, 1634, 415, 4105, 8816, 2168, 154]) == 8909
    assert solution.maxProfit([9620, 6550, 63, 1816, 7212, 7282]) == 7219
    assert solution.maxProfit([8666, 7442, 1634, 7022, 4559, 4530]) == 5388
    assert solution.maxProfit([7979, 5825, 9682, 5339, 8244, 196, 8042, 4399, 1896]) == 14608
    assert solution.maxProfit([2199, 3649]) == 1450
    assert solution.maxProfit([4817, 9023, 2394]) == 4206
    assert solution.maxProfit([5013, 6982]) == 1969
    assert solution.maxProfit([3260, 2744, 7486, 1875, 4587, 9126, 7708, 8806, 9105, 7590]) == 13390
    assert solution.maxProfit([6332, 5291, 6141, 423, 2271, 4161, 1620, 8150, 8431, 9899]) == 12867
    assert solution.maxProfit([1711, 444, 8624, 2389, 1160, 7348, 985, 6636, 4109, 3268]) == 20019
    assert solution.maxProfit([2624]) == 0
    assert solution.maxProfit([8144]) == 0
    assert solution.maxProfit([7525, 2058, 1614, 5310, 4585, 8617, 5481]) == 7728
    assert solution.maxProfit([3550, 613]) == 0
    assert solution.maxProfit([5375]) == 0
    assert solution.maxProfit([9825, 3431]) == 0
    assert solution.maxProfit([345, 8141, 4628, 3713, 2115, 2250, 4405, 3840, 3471]) == 10086
    assert solution.maxProfit([783]) == 0
    assert solution.maxProfit([4147, 4551, 6455, 339, 8717]) == 10686
    assert solution.maxProfit([6836, 6464, 3834, 9945, 7977, 7497, 9434, 2103, 4492, 8035]) == 13980
    assert solution.maxProfit([6296, 7413, 618, 3807]) == 4306
    assert solution.maxProfit([733]) == 0
    assert solution.maxProfit([3506, 1516, 2062, 1850, 8824, 6083, 1488, 1559]) == 7591
    assert solution.maxProfit([1029, 7046, 9500, 5023, 3881, 8472, 8483]) == 13073
    assert solution.maxProfit([8846, 3850, 6412, 5755, 9380, 6397, 3606, 5387, 379]) == 7968
    assert solution.maxProfit([259, 3690, 9718]) == 9459
    assert solution.maxProfit([8690, 5907, 2638, 5054, 7281]) == 4643
    assert solution.maxProfit([9001, 4185, 7330, 7366, 7796, 7308, 8928, 44]) == 5231
    assert solution.maxProfit([8225, 5291, 7854, 3598, 4303, 245, 7342, 8209, 8847]) == 11870
    assert solution.maxProfit([912, 1478, 9230, 8033]) == 8318
    assert solution.maxProfit([4289, 6565, 1455, 4560, 9892, 4024, 261, 7944, 9760, 5944]) == 20212
    assert solution.maxProfit([8378, 1986, 6724, 8220, 6307]) == 6234
    assert solution.maxProfit([998]) == 0
    assert solution.maxProfit([8600, 1296, 9029, 9381, 832, 7434, 28, 2478, 7921]) == 22580
    assert solution.maxProfit([3994, 1024, 8563, 6504, 6781, 6933]) == 7968
    assert solution.maxProfit([3740, 3598, 6929, 3346, 4513, 1632, 3799]) == 6665
    assert solution.maxProfit([935, 9799, 6961, 1875, 3193, 818, 8264, 7833]) == 17628
    assert solution.maxProfit([6331, 5070, 9670, 6879]) == 4600
    assert solution.maxProfit([8539, 7186, 4334, 8606]) == 4272
    assert solution.maxProfit([3917, 2777, 7617, 5247, 8378, 2163]) == 7971
    assert solution.maxProfit([9157, 2503, 7060, 1948, 4469, 3261, 9619, 3244, 1313]) == 13436
    assert solution.maxProfit([6267, 5494, 2694, 1607, 8024, 1974, 7751, 6563, 7582]) == 13213
    assert solution.maxProfit([7521, 1721, 4585, 6513, 6492, 4553, 8198]) == 8437
    assert solution.maxProfit([1557]) == 0
    assert solution.maxProfit([3467, 9129, 1092, 787]) == 5662
    assert solution.maxProfit([6301, 220, 5921, 6732, 1911]) == 6512
    assert solution.maxProfit([1929, 1144, 6728, 6237, 9071]) == 8418
    assert solution.maxProfit([213, 2199, 13, 3103, 7426, 9516, 9885, 1444]) == 11858
    assert solution.maxProfit([7474, 2098, 6623, 6992, 490, 8555, 5811]) == 12959
    assert solution.maxProfit([6479]) == 0
    assert solution.maxProfit([7731, 1321, 8867]) == 7546
    assert solution.maxProfit([8615, 6000, 4609, 5917, 1053, 7717, 3878]) == 7972
    assert solution.maxProfit([4018, 5189, 7515, 845]) == 3497
    assert solution.maxProfit([156, 8344, 7590, 2257, 9275, 3282, 62, 4832, 4501, 4308]) == 19976
    assert solution.maxProfit([2152, 7362, 6977, 5808, 7476, 7700]) == 7102
    assert solution.maxProfit([4377, 4185, 5407, 4589, 9316, 5054, 2985, 8614, 7722, 5197]) == 11578
    assert solution.maxProfit([3348, 9765]) == 6417
    assert solution.maxProfit([8014, 329, 1883, 6802, 8305, 1085]) == 7976
    assert solution.maxProfit([105, 7617, 9025, 2881, 4399]) == 10438
    assert solution.maxProfit([8453, 5908, 7892, 6310, 3869, 9706, 9710]) == 7825
    assert solution.maxProfit([6746]) == 0
    assert solution.maxProfit([1941]) == 0
    assert solution.maxProfit([7705, 4287, 9294, 1261, 2752, 5444, 1163, 921, 8401, 7327]) == 16670
    assert solution.maxProfit([9805, 6066, 683, 5778, 534]) == 5095
    assert solution.maxProfit([4295, 7654, 9051, 2612, 2751, 7060, 9764, 7609, 4751, 3476]) == 11908
    assert solution.maxProfit([1429, 348, 1769, 2804, 1461, 7900, 3104]) == 8895
    assert solution.maxProfit([61, 7845, 1211, 8137, 8448, 8635, 5823, 5951, 5864, 8688]) == 18160
    assert solution.maxProfit([6780, 3381, 9125, 5454, 1854, 4263, 1129, 8429, 7966]) == 15453
    assert solution.maxProfit([1552, 5151, 7680, 2714, 2624, 6220, 5367, 1835]) == 9724
    assert solution.maxProfit([4350, 646]) == 0
    assert solution.maxProfit([7429, 7094, 8844, 9707, 8643, 3360]) == 2613
    assert solution.maxProfit([9004, 6592, 7765, 6730, 5499]) == 1173
    assert solution.maxProfit([1228, 6823, 5783, 923, 871, 3919, 8476, 1876]) == 13200
    assert solution.maxProfit([4410, 109, 1374, 4137]) == 4028
    assert solution.maxProfit([8558, 8638, 3886, 3378, 7423]) == 4125
    assert solution.maxProfit([2196, 6737, 2189, 2845, 3485]) == 5837
    assert solution.maxProfit([8021, 1944, 3869]) == 1925
    assert solution.maxProfit([7734, 1009, 6259, 3871, 7200, 5716, 1119]) == 8579
    assert solution.maxProfit([838, 3227, 2825, 6785, 4572, 5245, 5906, 6305, 4027]) == 8082
    assert solution.maxProfit([1313, 3357, 525]) == 2044
    assert solution.maxProfit([9149, 9485, 8106, 6139]) == 336
    assert solution.maxProfit([104, 1843, 3273, 7220, 4131]) == 7116
    assert solution.maxProfit([5835, 27, 8745, 4989, 1433, 1943, 7568, 145]) == 14853
    assert solution.maxProfit([2829, 9462, 3523, 1364, 9292, 7723, 2043, 1319, 782]) == 14561
    assert solution.maxProfit([1962]) == 0
    assert solution.maxProfit([7102, 5118, 8409, 762, 3524, 5653, 9310, 2782, 8408]) == 17465
    assert solution.maxProfit([5755, 7665, 1817, 3125, 8726, 8300, 2996, 8878, 8267, 6617]) == 14701
    assert solution.maxProfit([7430, 3048, 7556, 6842, 6832, 5453, 2701, 4863, 4503, 1421]) == 6670
    assert solution.maxProfit([1394, 547, 9261, 5444, 8156, 5604, 109]) == 11426
    assert solution.maxProfit([1871, 8219]) == 6348
    assert solution.maxProfit([9669, 9761, 4638, 9407, 3815, 3791, 3345, 9337, 3767]) == 10853
    assert solution.maxProfit([7348, 4635, 5809, 3989]) == 1174
    assert solution.maxProfit([6018, 7445, 9741, 2454]) == 3723
    assert solution.maxProfit([3443, 9234, 9851]) == 6408
    assert solution.maxProfit([6814]) == 0

def run_timed_tests(solution):
    assert solution.maxProfit([6833, 4016, 3340, 9155]) == 5815
    assert solution.maxProfit([3803, 8280, 4943, 4289, 7018, 2284, 7118, 3127, 8286, 2506]) == 17199
    assert solution.maxProfit([9919, 9286, 5772, 1167, 5751, 2808, 6582, 2194, 267]) == 8358
    assert solution.maxProfit([2122, 7868, 4038, 5040, 6127]) == 7835
    assert solution.maxProfit([5140, 3521, 5338, 4001, 2055]) == 1817
    assert solution.maxProfit([8964, 1126, 1634, 415, 4105, 8816, 2168, 154]) == 8909
    assert solution.maxProfit([9620, 6550, 63, 1816, 7212, 7282]) == 7219
    assert solution.maxProfit([8666, 7442, 1634, 7022, 4559, 4530]) == 5388
    assert solution.maxProfit([7979, 5825, 9682, 5339, 8244, 196, 8042, 4399, 1896]) == 14608
    assert solution.maxProfit([2199, 3649]) == 1450
        

if __name__ == '__main__':
    import sys
    problem_id = 122
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

        print(f'medium_122,{sys.argv[2]},', end='')
        if problem_id == 527 and sys.argv[2] == 'claude':
            print('-- NR --')
            sys.exit(0)

        try:
            for _ in range(int(sys.argv[3])):
                start = time.time()
                run_timed_tests(solver)
                end = time.time()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            print('-- IR --')
            sys.exit(0)

        avg_time = statistics.mean(times)
        print(f'{avg_time:.4E}')