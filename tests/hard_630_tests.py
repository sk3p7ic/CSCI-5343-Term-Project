from hard_630_canon import Solution as SolutionCanon

def run_basic_tests(solution):
    
    assert solution.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
    assert solution.scheduleCourse([[1, 2]]) == 1
    assert solution.scheduleCourse([[3, 2], [4, 3]]) == 0
    


def run_advanced_tests(solution):
    assert solution.scheduleCourse([[55, 76], [96, 154], [61, 254], [75, 277], [27, 399], [44, 479], [23, 514], [28, 955]]) == 7
    assert solution.scheduleCourse([[54, 474], [34, 594], [98, 630], [6, 787], [62, 955], [8, 970]]) == 6
    assert solution.scheduleCourse([[51, 115], [34, 302], [98, 305], [49, 417], [1, 745], [60, 921], [80, 933]]) == 7
    assert solution.scheduleCourse([[49, 165], [97, 172], [49, 625], [70, 632], [93, 759], [97, 853], [70, 924]]) == 7
    assert solution.scheduleCourse([[66, 141], [80, 755], [57, 788]]) == 3
    assert solution.scheduleCourse([[85, 117], [41, 133], [79, 148], [82, 641], [87, 754], [79, 789], [34, 893]]) == 6
    assert solution.scheduleCourse([[7, 63], [100, 75], [91, 189], [11, 235], [2, 314]]) == 4
    assert solution.scheduleCourse([[23, 277], [89, 387]]) == 2
    assert solution.scheduleCourse([[50, 129], [44, 609], [29, 667], [39, 939], [73, 990]]) == 5
    assert solution.scheduleCourse([[67, 20], [30, 32], [24, 387], [13, 775], [88, 827]]) == 4
    assert solution.scheduleCourse([[44, 122], [59, 529], [41, 937], [95, 952]]) == 4
    assert solution.scheduleCourse([[94, 868], [80, 946]]) == 2
    assert solution.scheduleCourse([[58, 148], [94, 208], [88, 966]]) == 3
    assert solution.scheduleCourse([[3, 251], [67, 485], [94, 517], [75, 1001]]) == 4
    assert solution.scheduleCourse([[76, 33], [31, 203], [59, 347], [80, 401], [37, 877]]) == 4
    assert solution.scheduleCourse([[98, 99], [48, 248], [87, 301], [60, 336], [42, 411], [27, 634], [46, 702], [72, 800], [44, 840], [61, 878]]) == 10
    assert solution.scheduleCourse([[91, 805], [65, 915]]) == 2
    assert solution.scheduleCourse([[55, 751]]) == 1
    assert solution.scheduleCourse([[70, 114], [2, 147], [25, 793], [85, 982]]) == 4
    assert solution.scheduleCourse([[5, 540], [3, 546], [40, 811], [46, 817], [39, 838], [17, 865]]) == 6
    assert solution.scheduleCourse([[95, 62], [60, 388], [76, 592], [96, 608], [58, 665], [25, 882]]) == 5
    assert solution.scheduleCourse([[32, 277], [80, 323], [24, 531], [69, 849]]) == 4
    assert solution.scheduleCourse([[86, 195], [45, 704]]) == 2
    assert solution.scheduleCourse([[14, 250], [9, 460], [91, 544], [86, 704], [25, 730], [16, 919]]) == 6
    assert solution.scheduleCourse([[40, 127], [23, 263], [20, 295], [84, 440], [12, 579], [94, 686]]) == 6
    assert solution.scheduleCourse([[101, 66], [47, 70], [34, 78], [39, 88], [90, 99], [49, 217], [19, 720], [30, 807]]) == 5
    assert solution.scheduleCourse([[71, 27], [62, 107], [59, 108], [98, 241], [86, 297], [79, 615], [59, 710], [78, 768], [82, 938], [71, 947]]) == 8
    assert solution.scheduleCourse([[96, 51], [31, 665]]) == 1
    assert solution.scheduleCourse([[91, 200], [26, 388], [36, 563], [94, 934], [60, 995]]) == 5
    assert solution.scheduleCourse([[68, 26], [32, 59], [86, 382], [70, 449], [83, 821], [5, 865], [53, 868]]) == 6
    assert solution.scheduleCourse([[95, 141], [21, 383], [99, 396], [20, 422], [53, 426], [5, 467], [22, 470], [33, 498], [46, 953]]) == 9
    assert solution.scheduleCourse([[88, 69], [10, 218], [70, 349], [61, 359], [27, 415], [53, 645]]) == 5
    assert solution.scheduleCourse([[97, 778]]) == 1
    assert solution.scheduleCourse([[14, 58], [72, 175], [89, 511], [19, 519], [2, 750], [26, 953]]) == 6
    assert solution.scheduleCourse([[20, 356], [27, 382], [3, 459], [92, 478], [38, 688], [100, 820]]) == 6
    assert solution.scheduleCourse([[61, 385], [66, 389], [100, 563], [14, 665]]) == 4
    assert solution.scheduleCourse([[39, 420], [19, 443], [13, 492], [44, 542], [51, 591], [40, 607], [5, 713], [44, 986]]) == 8
    assert solution.scheduleCourse([[3, 67], [32, 199], [1, 401], [5, 751], [47, 819], [20, 974]]) == 6
    assert solution.scheduleCourse([[96, 410], [51, 582], [50, 591], [26, 602], [69, 679]]) == 5
    assert solution.scheduleCourse([[57, 74], [1, 486], [53, 526], [63, 795], [33, 822], [35, 864], [70, 988]]) == 7
    assert solution.scheduleCourse([[101, 101]]) == 1
    assert solution.scheduleCourse([[84, 332], [50, 364], [25, 430], [46, 637], [52, 659], [78, 732], [28, 810], [32, 857], [48, 948]]) == 9
    assert solution.scheduleCourse([[51, 64], [72, 643]]) == 2
    assert solution.scheduleCourse([[68, 484]]) == 1
    assert solution.scheduleCourse([[29, 278], [98, 316], [85, 829], [40, 959], [69, 964]]) == 5
    assert solution.scheduleCourse([[85, 418]]) == 1
    assert solution.scheduleCourse([[89, 262], [22, 380], [74, 596]]) == 3
    assert solution.scheduleCourse([[12, 80], [4, 101], [46, 519], [62, 810]]) == 4
    assert solution.scheduleCourse([[40, 257], [44, 323], [1, 717], [12, 749], [19, 929]]) == 5
    assert solution.scheduleCourse([[55, 118], [68, 454], [14, 961], [19, 990]]) == 4
    assert solution.scheduleCourse([[34, 322], [58, 395], [17, 419], [1, 521], [66, 628], [37, 696], [72, 777]]) == 7
    assert solution.scheduleCourse([[94, 140], [75, 266], [48, 367], [12, 927]]) == 4
    assert solution.scheduleCourse([[84, 260], [65, 361], [2, 483], [73, 527], [101, 613], [51, 775], [56, 833]]) == 7
    assert solution.scheduleCourse([[4, 131], [57, 254], [68, 470], [65, 508], [99, 514], [98, 982], [41, 998]]) == 7
    assert solution.scheduleCourse([[19, 36], [4, 239], [21, 436], [49, 486], [26, 649], [84, 746], [44, 830], [41, 836], [15, 942]]) == 9
    assert solution.scheduleCourse([[7, 207], [68, 408], [81, 750], [34, 769]]) == 4
    assert solution.scheduleCourse([[77, 442]]) == 1
    assert solution.scheduleCourse([[82, 188]]) == 1
    assert solution.scheduleCourse([[67, 22], [31, 276], [35, 534], [80, 578], [58, 615], [20, 645], [100, 683], [86, 897], [15, 905]]) == 8
    assert solution.scheduleCourse([[22, 47], [64, 93], [89, 274], [59, 431], [97, 570], [84, 658], [14, 783], [23, 803], [12, 828], [21, 884]]) == 10
    assert solution.scheduleCourse([[6, 174], [23, 243], [69, 331], [10, 336], [78, 376], [6, 636], [64, 664], [67, 793]]) == 8
    assert solution.scheduleCourse([[77, 31], [41, 222], [28, 344], [62, 497], [65, 794], [10, 977], [34, 986], [37, 989]]) == 7
    assert solution.scheduleCourse([[3, 63], [77, 83], [56, 191], [69, 197], [92, 673], [6, 706], [91, 863], [2, 883]]) == 7
    assert solution.scheduleCourse([[29, 403], [92, 490]]) == 2
    assert solution.scheduleCourse([[46, 210], [82, 388], [63, 573], [82, 684], [101, 790], [26, 953]]) == 6
    assert solution.scheduleCourse([[15, 156], [23, 431], [69, 582], [63, 851], [43, 922]]) == 5
    assert solution.scheduleCourse([[62, 58], [76, 365], [89, 558], [91, 599], [76, 639], [81, 676], [18, 732], [22, 769], [47, 880], [89, 883]]) == 9
    assert solution.scheduleCourse([[7, 349]]) == 1
    assert solution.scheduleCourse([[75, 938]]) == 1
    assert solution.scheduleCourse([[74, 806], [45, 979]]) == 2
    assert solution.scheduleCourse([[31, 384], [21, 559], [95, 785], [25, 931]]) == 4
    assert solution.scheduleCourse([[34, 411], [68, 456], [76, 845], [86, 993]]) == 4
    assert solution.scheduleCourse([[24, 28], [69, 118], [47, 463], [56, 516], [12, 535], [90, 748], [29, 781], [101, 952]]) == 8
    assert solution.scheduleCourse([[23, 471]]) == 1
    assert solution.scheduleCourse([[3, 80], [94, 120], [9, 369], [99, 431], [19, 435], [85, 543], [9, 565], [39, 700], [52, 762], [44, 827]]) == 10
    assert solution.scheduleCourse([[73, 216], [18, 342], [22, 411], [22, 794], [75, 868]]) == 5
    assert solution.scheduleCourse([[22, 147], [7, 252], [11, 277], [37, 445], [92, 599], [101, 600], [53, 832], [92, 853]]) == 8
    assert solution.scheduleCourse([[58, 415], [34, 513]]) == 2
    assert solution.scheduleCourse([[19, 288], [93, 724], [5, 992]]) == 3
    assert solution.scheduleCourse([[2, 175], [28, 387], [56, 453], [69, 466], [33, 955]]) == 5
    assert solution.scheduleCourse([[97, 798], [53, 929]]) == 2
    assert solution.scheduleCourse([[3, 31], [81, 239], [22, 247], [75, 353], [86, 541], [96, 554], [35, 597], [55, 912], [88, 920], [13, 936]]) == 10
    assert solution.scheduleCourse([[31, 7], [7, 95], [50, 363], [81, 557], [66, 891], [33, 899]]) == 5
    assert solution.scheduleCourse([[33, 221], [59, 234], [33, 376], [54, 409], [83, 426], [30, 598]]) == 6
    assert solution.scheduleCourse([[69, 884]]) == 1
    assert solution.scheduleCourse([[77, 154], [80, 315], [59, 691], [58, 725]]) == 4
    assert solution.scheduleCourse([[8, 41], [72, 61], [92, 78], [74, 355], [86, 413], [46, 458], [13, 639], [6, 810]]) == 6
    assert solution.scheduleCourse([[5, 79], [50, 147], [54, 151], [63, 249], [69, 366], [2, 431], [101, 494]]) == 7
    assert solution.scheduleCourse([[100, 17], [69, 165], [34, 493], [33, 760], [1, 797], [100, 861]]) == 5
    assert solution.scheduleCourse([[48, 34], [70, 36], [3, 42], [9, 68], [72, 396], [53, 402], [40, 435], [44, 803], [46, 850]]) == 7
    assert solution.scheduleCourse([[10, 985]]) == 1
    assert solution.scheduleCourse([[38, 644], [49, 751], [17, 980]]) == 3
    assert solution.scheduleCourse([[97, 202], [52, 665]]) == 2
    assert solution.scheduleCourse([[49, 150], [61, 239], [24, 733], [15, 902], [14, 910], [23, 928], [100, 964]]) == 7
    assert solution.scheduleCourse([[73, 431], [21, 754]]) == 2
    assert solution.scheduleCourse([[33, 140], [37, 220], [11, 360], [70, 428], [9, 565], [88, 619]]) == 6
    assert solution.scheduleCourse([[88, 632], [69, 759], [88, 817], [47, 828]]) == 4
    assert solution.scheduleCourse([[95, 239], [84, 351], [6, 458], [18, 485], [13, 490], [39, 537], [50, 687], [63, 721]]) == 8
    assert solution.scheduleCourse([[11, 398], [71, 488], [63, 496], [54, 526], [11, 917]]) == 5
    assert solution.scheduleCourse([[35, 46]]) == 1

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'test':
        canon = SolutionCanon()
        run_basic_tests(canon)
        run_advanced_tests(canon)
    if sys.argv[1] == 'time':
        import time, statistics
        canon_times = []

        canon = SolutionCanon()
        for _ in range(int(sys.argv[2])):
            start = time.time()
            run_basic_tests(canon)
            run_advanced_tests(canon)
            end = time.time()
            canon_times.append(end - start)
        
        canon_avg = statistics.mean(canon_times)
        print(f'Canonical Average Time: {canon_avg:.4E}')
