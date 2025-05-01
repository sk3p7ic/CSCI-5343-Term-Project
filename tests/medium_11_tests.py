from medium_11_canon import Solution as SolutionCanon
from chatgpt_medium_11 import Solution as SolutionChatGPT
from claude_medium_11 import Solution as SolutionClaude
from gemini_medium_11 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.maxArea([1,1]) == 1

def run_advanced_tests(solution):
    assert solution.maxArea([6728, 372, 5812]) == 11624
    assert solution.maxArea([9985, 3437]) == 3437
    assert solution.maxArea([8118, 4329, 2379, 751, 2496, 5226]) == 26130
    assert solution.maxArea([9280, 5489, 7935, 9972, 4171, 5413, 7226, 4756, 3201]) == 43356
    assert solution.maxArea([3097, 4458, 47, 118, 8790, 7521, 4044, 4244]) == 25464
    assert solution.maxArea([5632, 2411, 4811]) == 9622
    assert solution.maxArea([3525, 8157, 7774, 2773, 1223, 3711, 6932, 4556, 9908, 7833]) == 62664
    assert solution.maxArea([7877, 3917, 2392]) == 4784
    assert solution.maxArea([350, 3006, 5146, 7769]) == 6012
    assert solution.maxArea([9380, 7633, 2530, 5814, 7505, 7906, 3745, 343, 4952]) == 39616
    assert solution.maxArea([5961, 6215]) == 5961
    assert solution.maxArea([7758, 7031, 8454, 5191]) == 15573
    assert solution.maxArea([7967, 8143, 6425, 1161, 6811, 9564, 722]) == 39835
    assert solution.maxArea([8087, 4621, 7635, 6679]) == 20037
    assert solution.maxArea([7316, 7183, 26]) == 7183
    assert solution.maxArea([5199, 3285, 2554, 1128, 5888]) == 20796
    assert solution.maxArea([7839, 764, 8635]) == 15678
    assert solution.maxArea([9468, 344]) == 344
    assert solution.maxArea([272, 6197]) == 272
    assert solution.maxArea([428, 5267, 3233, 4327, 199]) == 8654
    assert solution.maxArea([1842, 3271, 9166, 4732, 4134, 9189, 7241, 134, 9269, 8872]) == 62104
    assert solution.maxArea([1964, 7579, 5857, 849, 2453]) == 7856
    assert solution.maxArea([980, 8177, 8041, 2719, 3507, 1715, 3524, 9275, 4951]) == 49062
    assert solution.maxArea([3219, 5560, 4882, 3062, 2503, 5833, 1403, 6820, 7863]) == 38920
    assert solution.maxArea([3075, 953, 7248, 8488, 3143, 2835, 1842]) == 14175
    assert solution.maxArea([5057, 7519, 3922]) == 7844
    assert solution.maxArea([6352, 6077, 323, 6113, 7492, 8942, 830, 2816]) == 31760
    assert solution.maxArea([746, 5987, 9123, 8612, 2453]) == 11974
    assert solution.maxArea([4447, 4567, 1803, 6295]) == 13341
    assert solution.maxArea([8092, 5729, 7873, 734]) == 15746
    assert solution.maxArea([321, 6835, 4632, 3241, 1756, 2985, 9359, 6282, 621]) == 37692
    assert solution.maxArea([46, 7071, 716]) == 716
    assert solution.maxArea([2865, 2074, 3764, 8780, 8991, 2140, 7758, 8769, 800, 2233]) == 35076
    assert solution.maxArea([5997, 2766, 888, 8087, 3906, 2769, 5803]) == 34818
    assert solution.maxArea([2403, 3662]) == 2403
    assert solution.maxArea([8507, 1621, 1046]) == 2092
    assert solution.maxArea([1034, 4041]) == 1034
    assert solution.maxArea([1482, 5175, 8424, 2572, 2986, 5767]) == 20700
    assert solution.maxArea([7891, 4969, 8677, 7725, 8652, 9242]) == 39455
    assert solution.maxArea([1272, 4440, 887]) == 1774
    assert solution.maxArea([9939, 6766, 1156]) == 6766
    assert solution.maxArea([2468, 2246, 1087, 2327, 2670, 9085, 2738, 6223, 3978, 3198]) == 22212
    assert solution.maxArea([8724, 7608, 9970, 3147, 8195]) == 32780
    assert solution.maxArea([655, 8544, 950, 6870, 8227, 3652, 1042, 3422, 9478]) == 59808
    assert solution.maxArea([1315, 5018, 782, 3075, 3115]) == 9345
    assert solution.maxArea([5088, 5800, 2088, 4738, 1199]) == 14214
    assert solution.maxArea([7893, 1023]) == 1023
    assert solution.maxArea([5735, 7576, 9438]) == 11470
    assert solution.maxArea([8397, 8414]) == 8397
    assert solution.maxArea([8614, 3816]) == 3816
    assert solution.maxArea([5378, 4303, 127, 9344, 8836]) == 21512
    assert solution.maxArea([5799, 1658, 3453, 4601, 7686]) == 23196
    assert solution.maxArea([3981, 660, 5129]) == 7962
    assert solution.maxArea([6424, 3481, 8171, 7900]) == 19272
    assert solution.maxArea([4833, 1239, 579, 2592, 6113, 1502, 4249, 7124, 348]) == 33831
    assert solution.maxArea([8874, 6566, 6604, 6066]) == 18198
    assert solution.maxArea([1584, 8711, 6011, 8248, 9046, 7169, 654]) == 28676
    assert solution.maxArea([8829, 4956, 8387]) == 16774
    assert solution.maxArea([366, 5664, 6438, 9967, 8221, 8112, 6324, 1898, 1131, 24]) == 28320
    assert solution.maxArea([9777, 9439]) == 9439
    assert solution.maxArea([7387, 8826, 1502, 9977, 1001]) == 22161
    assert solution.maxArea([5159, 4101, 1410, 9056, 1491]) == 15477
    assert solution.maxArea([5521, 2450, 1947, 6207, 3485, 3431, 4053, 1292]) == 24318
    assert solution.maxArea([7797, 1944, 2667, 1151, 8676, 649, 2589, 2005, 4797]) == 38376
    assert solution.maxArea([6697, 2368, 2629, 4468, 7843, 5060, 5356, 6568]) == 45976
    assert solution.maxArea([9210, 2134, 8690, 6655, 1967, 1323]) == 19965
    assert solution.maxArea([6002, 9479, 2987, 7230, 1962, 4949, 2734]) == 24745
    assert solution.maxArea([462, 7094, 7695]) == 7094
    assert solution.maxArea([344, 3882]) == 344
    assert solution.maxArea([8748, 330, 3282, 2320, 901, 9144, 9503, 3446, 5398]) == 52488
    assert solution.maxArea([9856, 9083, 3782, 874, 4493, 8748]) == 43740
    assert solution.maxArea([10000, 5571, 4879, 9329, 9021, 5520, 3216, 340, 7962, 9939]) == 89451
    assert solution.maxArea([2536, 3240, 9338, 5089, 9106, 9167, 8204, 1322]) == 32816
    assert solution.maxArea([2153, 931, 7410, 4060, 527]) == 6459
    assert solution.maxArea([1510, 5675, 9025, 8120, 1938, 2620, 9785]) == 36100
    assert solution.maxArea([8563, 3564, 6383]) == 12766
    assert solution.maxArea([7322, 2334, 4474]) == 8948
    assert solution.maxArea([3384, 2563, 5946, 1949, 155, 7545, 7592, 7045, 7220]) == 35676
    assert solution.maxArea([414, 1421, 3587, 4175, 4318, 6224, 9811, 3306, 67, 8549]) == 25647
    assert solution.maxArea([7760, 4057, 6256, 2843, 1954, 3131, 7070, 9825, 7562]) == 60496
    assert solution.maxArea([6823, 4070, 4850, 8926, 2956, 4972, 5069, 2386, 310, 1928]) == 30414
    assert solution.maxArea([2526, 7611, 4810, 2893, 1208, 5380]) == 21520
    assert solution.maxArea([9433, 5387]) == 5387
    assert solution.maxArea([22, 6138, 1897, 1226, 1531, 9996, 9007, 9050, 8530, 1430]) == 42966
    assert solution.maxArea([8531, 3912, 7841, 2230, 7161, 2432, 4916, 3338, 3364]) == 29496
    assert solution.maxArea([6346, 6701, 5790, 8835, 2701, 5741, 7838]) == 38076
    assert solution.maxArea([3975, 61, 6221, 7686, 9650, 2991, 3637, 884, 4488, 8803]) == 46116
    assert solution.maxArea([8655, 1724]) == 1724
    assert solution.maxArea([8531, 364, 8030, 9976]) == 25593
    assert solution.maxArea([5426, 3838, 8067, 6405, 9585, 2722, 6181]) == 32556
    assert solution.maxArea([2845, 4894, 4260]) == 5690
    assert solution.maxArea([7333, 6632, 9916, 6617, 4895, 5226, 9437]) == 43998
    assert solution.maxArea([4945, 6805, 4510, 5628]) == 14835
    assert solution.maxArea([4024, 6555, 4979, 1147, 5515]) == 16545
    assert solution.maxArea([694, 3588, 5985, 7252, 9365, 847, 1981, 7559, 3310, 4086]) == 29925
    assert solution.maxArea([4569, 9922, 9787]) == 9787
    assert solution.maxArea([616, 2611, 4776, 2363, 9121, 1328]) == 9552
    assert solution.maxArea([8785, 2469, 4802, 3718, 1575, 3705, 3464, 891, 7113]) == 56904
    assert solution.maxArea([6963, 146, 2745, 6377, 3632, 5923]) == 29615
    assert solution.maxArea([1889, 1895, 4957, 4119, 5059, 1783, 8608, 7787]) == 24785

def run_timed_tests(solution):
    assert solution.maxArea([6728, 372, 5812]) == 11624
    assert solution.maxArea([9985, 3437]) == 3437
    assert solution.maxArea([8118, 4329, 2379, 751, 2496, 5226]) == 26130
    assert solution.maxArea([9280, 5489, 7935, 9972, 4171, 5413, 7226, 4756, 3201]) == 43356
    assert solution.maxArea([3097, 4458, 47, 118, 8790, 7521, 4044, 4244]) == 25464
    assert solution.maxArea([5632, 2411, 4811]) == 9622
    assert solution.maxArea([3525, 8157, 7774, 2773, 1223, 3711, 6932, 4556, 9908, 7833]) == 62664
    assert solution.maxArea([7877, 3917, 2392]) == 4784
    assert solution.maxArea([350, 3006, 5146, 7769]) == 6012
    assert solution.maxArea([9380, 7633, 2530, 5814, 7505, 7906, 3745, 343, 4952]) == 39616
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 11
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

        output += f'medium_11,{sys.argv[2]},'
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