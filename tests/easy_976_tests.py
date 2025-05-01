from easy_976_canon import Solution as SolutionCanon
from chatgpt_easy_976 import Solution as SolutionChatGPT
from claude_easy_976 import Solution as SolutionClaude
from gemini_easy_976 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.largestPerimeter([2, 1, 2]) == 5
    assert solution.largestPerimeter([1, 2, 1, 10]) == 0

def run_advanced_tests(solution):
    assert solution.largestPerimeter([434493, 520440, 616438, 628268, 641965, 733236, 911253, 914728]) == 2559217
    assert solution.largestPerimeter([608071, 736445, 756933, 955948]) == 2449326
    assert solution.largestPerimeter([36475, 167373, 835988, 941551, 978698, 990801]) == 2911050
    assert solution.largestPerimeter([70684, 338019, 437643, 449586, 657144, 801441, 808814, 953428]) == 2563683
    assert solution.largestPerimeter([268601, 290001, 795414]) == 0
    assert solution.largestPerimeter([45749, 111306, 292786, 496571, 538713, 581649, 829562, 862150]) == 2273361
    assert solution.largestPerimeter([284366, 406781, 555606, 565983, 679101]) == 1800690
    assert solution.largestPerimeter([59286, 103391, 223733, 236758, 356538, 545933, 602009, 646218, 692645, 721108]) == 2059971
    assert solution.largestPerimeter([115292, 251534, 304386, 400006, 979045]) == 955926
    assert solution.largestPerimeter([381455, 390472, 527238, 540780, 625923, 737513, 806191, 915739, 957321]) == 2679251
    assert solution.largestPerimeter([17320, 126151, 216292, 303776, 683557, 687423, 734747, 863461]) == 2285631
    assert solution.largestPerimeter([87950, 306764, 572859, 616136, 681023, 814341, 894183, 958090]) == 2666614
    assert solution.largestPerimeter([114016, 268676, 479066, 551703, 650930, 898613]) == 2101246
    assert solution.largestPerimeter([4263, 49796, 133883, 145110, 268168, 513241, 551940, 723874, 770529, 772947]) == 2267350
    assert solution.largestPerimeter([37206, 50902, 495606, 567144, 759499, 980717, 994600]) == 2734816
    assert solution.largestPerimeter([97575, 179571, 253332, 307683, 655058, 922267, 994743]) == 2572068
    assert solution.largestPerimeter([56761, 150805, 204191, 215307, 351504, 388666, 390669, 456420, 713343, 845667]) == 2015430
    assert solution.largestPerimeter([56971, 84169, 107827, 144836, 233315, 278598, 461630, 664455, 763033, 799497]) == 2226985
    assert solution.largestPerimeter([26928, 249338, 295614, 377705, 549905, 831087, 849062, 871812, 902915, 907522]) == 2682249
    assert solution.largestPerimeter([52846, 294931, 871403]) == 0
    assert solution.largestPerimeter([75496, 146848, 323907, 373479]) == 844234
    assert solution.largestPerimeter([96902, 230564, 292812, 383347, 537664, 620917, 723689, 946171]) == 2290777
    assert solution.largestPerimeter([81390, 95723, 332334, 436116, 582878, 812005, 933652]) == 2328535
    assert solution.largestPerimeter([348965, 365499, 526951, 781094, 934881]) == 2242926
    assert solution.largestPerimeter([836666, 837366, 877739]) == 2551771
    assert solution.largestPerimeter([195910, 544628, 819581]) == 0
    assert solution.largestPerimeter([142224, 202373, 316583, 482517, 700753, 707226, 788111, 789361, 868900, 879026]) == 2537287
    assert solution.largestPerimeter([97002, 414197, 657872, 774663, 876352, 953018]) == 2604033
    assert solution.largestPerimeter([321090, 416618, 496931, 586684, 624134, 738586, 784915, 797188, 821454, 937966]) == 2556608
    assert solution.largestPerimeter([79615, 197856, 363826, 631343, 751055, 782386, 949489, 978799]) == 2710674
    assert solution.largestPerimeter([41491, 107845, 314511, 339586, 394707, 592294, 598365, 657295, 791157]) == 2046817
    assert solution.largestPerimeter([22548, 143281, 151887, 268987, 464620, 564750]) == 1298357
    assert solution.largestPerimeter([9936, 245489, 528947]) == 0
    assert solution.largestPerimeter([38438, 347517, 707121, 721348, 750009, 897581]) == 2368938
    assert solution.largestPerimeter([86587, 420473, 547570, 576840]) == 1544883
    assert solution.largestPerimeter([4776, 81765, 94869, 158898, 221729, 337053, 642995, 708687, 858644]) == 2210326
    assert solution.largestPerimeter([519709, 530319, 607061, 713737, 783505, 829835, 853697, 943051]) == 2626583
    assert solution.largestPerimeter([175780, 384251, 480646, 548764, 558688, 649579, 751120, 783322, 889751]) == 2424193
    assert solution.largestPerimeter([214339, 333886, 507668, 630253, 709391, 715096, 726876, 908012]) == 2349984
    assert solution.largestPerimeter([15113, 38665, 812588, 916379]) == 0
    assert solution.largestPerimeter([402700, 447213, 597913, 624742, 641985, 648529, 998031]) == 2288545
    assert solution.largestPerimeter([148660, 177273, 252427, 321352, 796034, 831922, 934518, 963382, 976490, 980585]) == 2920457
    assert solution.largestPerimeter([155346, 200195, 470493, 513263, 629419]) == 1613175
    assert solution.largestPerimeter([15793, 33539, 94188, 105253, 297560, 467156, 600023, 726174, 922738, 961093]) == 2610005
    assert solution.largestPerimeter([116042, 337232, 405069, 462110, 509073, 671793, 751633, 931890, 996730]) == 2680253
    assert solution.largestPerimeter([80792, 159733, 261933, 402393, 414629, 574559, 703600, 730597, 845246, 970293]) == 2546136
    assert solution.largestPerimeter([326182, 482073, 645111, 645652, 721722, 736876, 738302, 822578, 903056]) == 2463936
    assert solution.largestPerimeter([388572, 467374, 602047, 772731]) == 1842152
    assert solution.largestPerimeter([210580, 249270, 367939, 509341, 517996]) == 1395276
    assert solution.largestPerimeter([275053, 353905, 463573, 874800]) == 1092531
    assert solution.largestPerimeter([18746, 153061, 305364, 566630, 742527, 862160]) == 2171317
    assert solution.largestPerimeter([4844, 142975, 347315, 529879, 625132, 649729, 732346, 749549, 821629, 981626]) == 2552804
    assert solution.largestPerimeter([258427, 480153, 890199]) == 0
    assert solution.largestPerimeter([6835, 290484, 531364, 637131, 664722, 712632, 805473, 908882]) == 2426987
    assert solution.largestPerimeter([68378, 159045, 255082, 418219, 593299]) == 1266600
    assert solution.largestPerimeter([92726, 255552, 316912, 523991, 700169, 995573]) == 2219733
    assert solution.largestPerimeter([62633, 126683, 315598, 354350, 403196, 404448, 761035, 949161]) == 2114644
    assert solution.largestPerimeter([17732, 229431, 336073, 385655, 493531, 577642]) == 1456828
    assert solution.largestPerimeter([711981, 798481, 821439, 964384]) == 2584304
    assert solution.largestPerimeter([205908, 223959, 413683, 639556, 704579, 772769, 955967, 960673]) == 2689409
    assert solution.largestPerimeter([63676, 525282, 692011, 750904, 791194]) == 2234109
    assert solution.largestPerimeter([234978, 800945, 841746, 843799, 861285]) == 2546830
    assert solution.largestPerimeter([76605, 211146, 503641, 732201, 817677]) == 2053519
    assert solution.largestPerimeter([70971, 207870, 223420, 379080, 456150, 471785, 498519, 537410, 589537, 706542]) == 1833489
    assert solution.largestPerimeter([187640, 205389, 370010, 461425, 657250, 933111, 942646]) == 2533007
    assert solution.largestPerimeter([96081, 159201, 367167]) == 0
    assert solution.largestPerimeter([48416, 178747, 189062, 238701, 475987, 495163, 815688, 887571, 991186, 993696]) == 2872453
    assert solution.largestPerimeter([132338, 617043, 669733, 922448]) == 2209224
    assert solution.largestPerimeter([211221, 318890, 319614, 327563, 356211, 487229, 504893, 603766]) == 1595888
    assert solution.largestPerimeter([6236, 226330, 379500, 408961, 551358, 670150, 901282]) == 2122790
    assert solution.largestPerimeter([74226, 287293, 392452, 458470, 466433, 897222, 996405]) == 2360060
    assert solution.largestPerimeter([96174, 171258, 306072, 702083, 981555]) == 1989710
    assert solution.largestPerimeter([546, 217986, 373325, 720339, 845697]) == 1939361
    assert solution.largestPerimeter([67802, 581012, 828442]) == 0
    assert solution.largestPerimeter([65364, 86199, 129260, 552799, 811553, 901384]) == 2265736
    assert solution.largestPerimeter([309170, 311843, 388732, 496392, 504894, 758785, 822070, 938655]) == 2519510
    assert solution.largestPerimeter([13502, 101515, 173875, 195369, 261783, 357336, 449630, 585096, 648336, 984573]) == 2218005
    assert solution.largestPerimeter([139133, 171973, 526202, 633713, 708336, 722932, 883267, 918734]) == 2524933
    assert solution.largestPerimeter([122603, 218529, 249510, 343459, 452608, 627009, 921860]) == 2001477
    assert solution.largestPerimeter([219958, 342576, 399707, 404222, 406648, 424227, 544413, 548266]) == 1516906
    assert solution.largestPerimeter([158238, 398243, 423098, 455754, 497373, 712240, 736684, 835656, 897752]) == 2470092
    assert solution.largestPerimeter([41900, 96687, 375629, 817551]) == 0
    assert solution.largestPerimeter([194139, 403204, 566524, 637990, 777519, 810498, 822553, 958100, 989851]) == 2770504
    assert solution.largestPerimeter([149152, 288739, 639828, 648306]) == 1576873
    assert solution.largestPerimeter([285503, 772155, 805389, 819350]) == 2396894
    assert solution.largestPerimeter([196098, 482828, 492327, 493823, 703914]) == 1690064
    assert solution.largestPerimeter([141201, 242841, 535741, 564151, 798022, 840884, 910650, 944181]) == 2695715
    assert solution.largestPerimeter([8320, 315701, 340796, 369584, 497931, 623403, 747160, 754427, 985217]) == 2486804
    assert solution.largestPerimeter([161255, 203666, 284659, 538520, 642839, 654723, 847908, 941064, 964109]) == 2753081
    assert solution.largestPerimeter([461639, 564756, 760422, 872688]) == 2197866
    assert solution.largestPerimeter([60111, 103477, 193532, 314966, 555973, 706082, 879540]) == 2141595
    assert solution.largestPerimeter([529518, 580595, 613762, 839190, 874429, 963461]) == 2677080
    assert solution.largestPerimeter([69740, 163331, 165534, 184238, 217248, 241298, 470488, 600907]) == 1312693
    assert solution.largestPerimeter([146277, 202053, 332716, 337238, 581686, 702896, 955808]) == 2240390
    assert solution.largestPerimeter([60888, 89112, 314372, 936771]) == 0
    assert solution.largestPerimeter([287992, 291223, 477989, 750900, 782373]) == 2011262
    assert solution.largestPerimeter([174030, 182118, 204212, 314155, 457127, 513770, 516880, 547521, 610393, 934335]) == 2092249
    assert solution.largestPerimeter([137240, 213710, 417764, 457003, 552832, 605031, 648039, 659635, 980060]) == 2287734
    assert solution.largestPerimeter([198925, 202797, 480073, 515209]) == 1198079
    assert solution.largestPerimeter([30869, 575220, 683820, 722291]) == 1981331

def run_timed_tests(solution):
    assert solution.largestPerimeter([434493, 520440, 616438, 628268, 641965, 733236, 911253, 914728]) == 2559217
    assert solution.largestPerimeter([608071, 736445, 756933, 955948]) == 2449326
    assert solution.largestPerimeter([36475, 167373, 835988, 941551, 978698, 990801]) == 2911050
    assert solution.largestPerimeter([70684, 338019, 437643, 449586, 657144, 801441, 808814, 953428]) == 2563683
    assert solution.largestPerimeter([268601, 290001, 795414]) == 0
    assert solution.largestPerimeter([45749, 111306, 292786, 496571, 538713, 581649, 829562, 862150]) == 2273361
    assert solution.largestPerimeter([284366, 406781, 555606, 565983, 679101]) == 1800690
    assert solution.largestPerimeter([59286, 103391, 223733, 236758, 356538, 545933, 602009, 646218, 692645, 721108]) == 2059971
    assert solution.largestPerimeter([115292, 251534, 304386, 400006, 979045]) == 955926
    assert solution.largestPerimeter([381455, 390472, 527238, 540780, 625923, 737513, 806191, 915739, 957321]) == 2679251
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 976
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

        output += f'easy_976,{sys.argv[2]},'
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