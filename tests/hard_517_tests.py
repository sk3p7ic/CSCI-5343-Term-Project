from hard_517_canon import Solution as SolutionCanon
from chatgpt_hard_517 import Solution as SolutionChatGPT
from claude_hard_517 import Solution as SolutionClaude
from gemini_hard_517 import Solution as SolutionGemini


def run_basic_tests(solution):
    
    assert solution.findMinMoves([1, 0, 5]) == 3
    assert solution.findMinMoves([0, 3, 0]) == 2
    assert solution.findMinMoves([0, 2, 0]) == -1

def run_advanced_tests(solution):
    assert solution.findMinMoves([86085, 63081, 92523, 62834, 94292, 45356, 10810, 85316, 10785, 70039]) == -1
    assert solution.findMinMoves([1131, 2330, 16654, 4860, 88564, 73252, 87617, 21336]) == 122897
    assert solution.findMinMoves([51585, 67007, 12181, 51858, 94425]) == -1
    assert solution.findMinMoves([14872, 38940, 50810, 88324, 91726, 50737, 40132, 63562, 46254]) == -1
    assert solution.findMinMoves([51936, 70431, 12913, 41108, 59910, 48549, 53094]) == -1
    assert solution.findMinMoves([15011, 23871, 60567, 58940, 10900, 44605, 14305, 4638]) == -1
    assert solution.findMinMoves([50337, 77670, 95557, 59169, 50434, 57921, 14281, 29329]) == -1
    assert solution.findMinMoves([21637, 15224, 57846, 1013, 6829, 31747, 26374, 93414, 92426]) == -1
    assert solution.findMinMoves([70890, 33406, 77735, 30435, 95018, 21229, 39821, 19125, 40580]) == -1
    assert solution.findMinMoves([26611, 51845, 5719, 63725, 17182, 38334, 11025, 82617]) == -1
    assert solution.findMinMoves([91786, 17627, 3052, 17089, 55038, 74106, 62158, 23560, 38533]) == -1
    assert solution.findMinMoves([42508, 71463, 97080, 67029]) == 27560
    assert solution.findMinMoves([47401, 42974, 62462, 55147, 72991, 20810, 44019, 23038, 21285, 10056]) == -1
    assert solution.findMinMoves([26322, 91036, 66115, 34693, 48048, 78781, 70630]) == 33053
    assert solution.findMinMoves([93308, 18941, 54698, 76064, 31223]) == -1
    assert solution.findMinMoves([99930, 33630, 68292, 85135, 76286]) == -1
    assert solution.findMinMoves([59088, 95424, 63131, 45139, 27537, 60814, 35701]) == 51857
    assert solution.findMinMoves([3507, 57862, 12411, 96736, 65562, 59472, 33035, 65254]) == -1
    assert solution.findMinMoves([36536, 9952, 73702]) == -1
    assert solution.findMinMoves([25693, 12753, 25331, 60246, 28180, 21192, 46404, 33176, 69056, 3069]) == 36546
    assert solution.findMinMoves([3677, 39300, 71963, 65889, 11880]) == -1
    assert solution.findMinMoves([31180, 50562, 99045, 60284, 40885, 24546, 71790, 61608, 52887]) == -1
    assert solution.findMinMoves([40655, 25656, 87372]) == -1
    assert solution.findMinMoves([20365, 8972, 16940, 42486, 70385, 13814, 32089, 10598, 82753]) == -1
    assert solution.findMinMoves([30131, 87178, 68456, 46660, 16938, 82240, 33698]) == -1
    assert solution.findMinMoves([52081, 85335, 59269, 79800, 27334]) == -1
    assert solution.findMinMoves([7386, 17774, 83871, 31951, 28751, 92374, 1747, 69082]) == 58074
    assert solution.findMinMoves([77225, 16515, 38763]) == -1
    assert solution.findMinMoves([28280, 74168, 49966]) == -1
    assert solution.findMinMoves([3427, 46837, 546, 23290, 71542, 51368, 39480]) == -1
    assert solution.findMinMoves([80900, 61891, 97562, 48065, 75302, 90331, 60734, 35854, 94381]) == -1
    assert solution.findMinMoves([43647, 91669, 17723, 30154, 20874, 7793, 80330]) == -1
    assert solution.findMinMoves([53196, 41361, 24860, 94484, 27015, 54607, 14237, 78488, 58244]) == -1
    assert solution.findMinMoves([44074, 55455, 50471, 68138, 24851, 6628, 33202, 67506]) == -1
    assert solution.findMinMoves([45715, 94982, 27977, 2411, 24051, 90726, 32672]) == -1
    assert solution.findMinMoves([45950, 13336, 93940]) == -1
    assert solution.findMinMoves([31062, 55116, 32276]) == -1
    assert solution.findMinMoves([64258, 62951, 64531, 19952, 1972, 65306, 37259, 5411, 2355, 92132]) == -1
    assert solution.findMinMoves([19776, 82964, 65201, 66660, 45444, 3948, 91501, 95320]) == -1
    assert solution.findMinMoves([44646, 61216, 14256, 15407, 74402, 7490, 20316, 1284, 335]) == -1
    assert solution.findMinMoves([60714, 52919, 53650, 88500, 30668, 493, 43966, 12095, 38897, 20849]) == -1
    assert solution.findMinMoves([13185, 85410, 31746, 90514, 22123]) == -1
    assert solution.findMinMoves([52598, 6948, 46332, 46746, 40891]) == 17860
    assert solution.findMinMoves([54493, 58965, 40205, 94660, 98740]) == -1
    assert solution.findMinMoves([23037, 8405, 80060, 56499, 19555, 72120]) == -1
    assert solution.findMinMoves([61277, 62452, 39825, 73078, 27659, 68672, 36578, 94790, 17182]) == -1
    assert solution.findMinMoves([23814, 96198, 67052, 70387, 53584]) == 38393
    assert solution.findMinMoves([77609, 51136, 17394, 22373, 22454, 91653]) == -1
    assert solution.findMinMoves([23264, 46043, 86987, 92863, 22067, 20531, 64989, 37930, 83260, 56650]) == -1
    assert solution.findMinMoves([29006, 43323, 75165, 72270, 65655, 22619, 78764, 4269, 99960, 58747]) == -1
    assert solution.findMinMoves([93205, 53745, 84997, 18194, 12626]) == -1
    assert solution.findMinMoves([75325, 66023, 35711, 55507, 13719, 81857, 10432, 92435]) == -1
    assert solution.findMinMoves([53917, 36728, 5755, 90419, 22297, 92012, 42269, 20599]) == -1
    assert solution.findMinMoves([95894, 46508, 98999, 41977, 55762, 14831, 66839]) == -1
    assert solution.findMinMoves([97713, 63452, 41055, 42041, 80542, 61575, 22716]) == 44281
    assert solution.findMinMoves([2145, 76441, 43920, 59006, 15667]) == -1
    assert solution.findMinMoves([43768, 51389, 56193, 39069, 22429]) == -1
    assert solution.findMinMoves([47975, 95433, 67180, 47877]) == -1
    assert solution.findMinMoves([37145, 50103, 60003, 54268, 55464, 27100, 90827, 94470]) == -1
    assert solution.findMinMoves([507, 26254, 51594, 98829, 83895, 76629, 89041, 35069, 79815, 99334]) == -1
    assert solution.findMinMoves([45824, 36216, 85210, 47857, 15718, 5899, 42922, 38340]) == -1
    assert solution.findMinMoves([64376, 11017, 83755, 42257, 49016, 59823, 50097]) == -1
    assert solution.findMinMoves([92908, 47248, 4748, 80554]) == -1
    assert solution.findMinMoves([3857, 59179, 16179, 47424, 54647, 31169, 31844, 46575]) == -1
    assert solution.findMinMoves([66077, 75375, 39079, 32155, 23003, 48136, 33843, 38802, 49369]) == -1
    assert solution.findMinMoves([87493, 45841, 76617, 88511, 54743, 36164]) == -1
    assert solution.findMinMoves([73455, 12186, 57560, 29586, 28307]) == -1
    assert solution.findMinMoves([64543, 61653, 35789, 51695, 60506, 98396, 66571, 26481, 48481, 48932]) == -1
    assert solution.findMinMoves([35740, 41587, 84794, 33851, 77698, 41842, 47720]) == -1
    assert solution.findMinMoves([21035, 8731, 9617]) == -1
    assert solution.findMinMoves([81129, 14346, 42732, 79038, 61119, 75009]) == -1
    assert solution.findMinMoves([34523, 12607, 61609, 66059, 74036, 33386, 78255, 92564]) == -1
    assert solution.findMinMoves([50774, 39022, 20922]) == 15984
    assert solution.findMinMoves([6658, 10267, 19663, 12578, 32721, 74644, 73136, 46301, 83941]) == -1
    assert solution.findMinMoves([90573, 24004, 24599, 64261, 57424, 60718, 37663, 71001]) == -1
    assert solution.findMinMoves([45618, 11263, 99490, 69144, 44937, 33020, 76842]) == -1
    assert solution.findMinMoves([63167, 28797, 29677, 56409, 50027, 44195, 98731, 33562, 59461]) == -1
    assert solution.findMinMoves([31329, 51808, 20270, 54175, 51439, 21129, 14253, 38821, 91945, 11358]) == -1
    assert solution.findMinMoves([96229, 2922, 95943, 80090, 60397, 16523, 4780, 7286]) == -1
    assert solution.findMinMoves([15686, 26499, 84166, 37653, 42312]) == -1
    assert solution.findMinMoves([78942, 6912, 72570, 34552]) == 30698
    assert solution.findMinMoves([37304, 97578, 11543, 13276, 86858, 1500, 89109, 54789, 94093]) == -1
    assert solution.findMinMoves([82338, 67979, 21606, 78461, 86688, 20063, 11813, 77998, 44617]) == -1
    assert solution.findMinMoves([1888, 55241, 95165, 57962, 77240, 41624, 38795, 15977, 82006]) == -1
    assert solution.findMinMoves([44253, 69208, 14935]) == -1
    assert solution.findMinMoves([14143, 46637, 23719, 69966]) == -1
    assert solution.findMinMoves([72163, 28095, 31319, 55587, 73941, 4274, 28677, 35042, 21503]) == -1
    assert solution.findMinMoves([43445, 97255, 86607, 40572]) == -1
    assert solution.findMinMoves([8417, 32465, 87964, 7620]) == -1
    assert solution.findMinMoves([49037, 42628, 81294, 12540, 61158, 98199, 1997]) == -1
    assert solution.findMinMoves([68427, 28484, 83880, 50859, 28681, 11249, 7005, 57879, 37832, 92673]) == -1
    assert solution.findMinMoves([65734, 76277, 90713, 4988, 51960, 67893, 76689, 52545, 89353, 69058]) == 39161
    assert solution.findMinMoves([49320, 32703, 38965, 672]) == 29743
    assert solution.findMinMoves([38372, 25070, 62512, 17953, 73724]) == -1
    assert solution.findMinMoves([23490, 17985, 27590]) == -1
    assert solution.findMinMoves([91172, 81388, 48718, 49547, 20367, 45425]) == -1
    assert solution.findMinMoves([81218, 85442, 45383, 87801, 92104, 59928, 47496, 89839, 88528]) == -1
    assert solution.findMinMoves([87808, 86564, 13416, 75990, 18935, 16290, 35362, 6729, 77294]) == -1
    assert solution.findMinMoves([96806, 63685, 6916, 63039, 69058, 26272, 79554, 91198, 94685]) == -1
    assert solution.findMinMoves([64546, 23822, 49002, 46475, 85730, 63282, 31957, 30123, 64487, 67636]) == 33024
        

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'test':
        solvers = [SolutionCanon()]
        if len(sys.argv) == 3 and sys.argv[2] == 'all':
            solvers.extend([SolutionChatGPT(), SolutionClaude(),
                            SolutionGemini()])
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

        print(f'hard_517,{sys.argv[2]},', end='')
        try:
            for _ in range(int(sys.argv[3])):
                start = time.time()
                run_basic_tests(solver)
                run_advanced_tests(solver)
                end = time.time()
                times.append(end - start)
        except AssertionError as err:
            print(f'Assertion Failed: {err}', file=sys.stderr)
            print('------')

        avg_time = statistics.mean(times)
        print(f'{avg_time:.4E}')