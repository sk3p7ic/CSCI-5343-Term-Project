from easy_680_canon import Solution as SolutionCanon

def run_basic_tests(solution):
    
    assert solution.validPalindrome("aba") == True
    assert solution.validPalindrome("abca") == True
    assert solution.validPalindrome("abc") == False
    


def run_advanced_tests(solution):
    assert solution.validPalindrome("ycmhojj") == False
    assert solution.validPalindrome("gxopvboat") == False
    assert solution.validPalindrome("vr") == True
    assert solution.validPalindrome("yccnizg") == False
    assert solution.validPalindrome("tfjoxv") == False
    assert solution.validPalindrome("gxqwe") == False
    assert solution.validPalindrome("oh") == True
    assert solution.validPalindrome("kyhbmehb") == False
    assert solution.validPalindrome("wbduqxov") == False
    assert solution.validPalindrome("xu") == True
    assert solution.validPalindrome("k") == True
    assert solution.validPalindrome("rcvbugugf") == False
    assert solution.validPalindrome("jypntavcd") == False
    assert solution.validPalindrome("ze") == True
    assert solution.validPalindrome("i") == True
    assert solution.validPalindrome("pdjfdjmnjh") == False
    assert solution.validPalindrome("iv") == True
    assert solution.validPalindrome("yyyrnoydag") == False
    assert solution.validPalindrome("iynfjdeara") == False
    assert solution.validPalindrome("glmnyojf") == False
    assert solution.validPalindrome("paqtnzrkb") == False
    assert solution.validPalindrome("goqc") == False
    assert solution.validPalindrome("axs") == False
    assert solution.validPalindrome("qisyfdbeae") == False
    assert solution.validPalindrome("gnxlglunr") == False
    assert solution.validPalindrome("rkvdzweo") == False
    assert solution.validPalindrome("xmtywcv") == False
    assert solution.validPalindrome("jjfirfjeay") == False
    assert solution.validPalindrome("egkg") == True
    assert solution.validPalindrome("xsfojfqelr") == False
    assert solution.validPalindrome("klofknpilw") == False
    assert solution.validPalindrome("nnpvwtw") == False
    assert solution.validPalindrome("qsnbmweqa") == False
    assert solution.validPalindrome("vkubdr") == False
    assert solution.validPalindrome("gxnvmvr") == False
    assert solution.validPalindrome("os") == True
    assert solution.validPalindrome("feorphhq") == False
    assert solution.validPalindrome("lriq") == False
    assert solution.validPalindrome("sq") == True
    assert solution.validPalindrome("pfogqzr") == False
    assert solution.validPalindrome("ypsprs") == False
    assert solution.validPalindrome("o") == True
    assert solution.validPalindrome("ckoblcgal") == False
    assert solution.validPalindrome("fhyder") == False
    assert solution.validPalindrome("zknxn") == False
    assert solution.validPalindrome("haiyg") == False
    assert solution.validPalindrome("tsupjx") == False
    assert solution.validPalindrome("fghntgud") == False
    assert solution.validPalindrome("rfkbdvxhx") == False
    assert solution.validPalindrome("err") == True
    assert solution.validPalindrome("ljvzvd") == False
    assert solution.validPalindrome("uwfgbtdjs") == False
    assert solution.validPalindrome("zdqzzxevul") == False
    assert solution.validPalindrome("chvne") == False
    assert solution.validPalindrome("qs") == True
    assert solution.validPalindrome("byuk") == False
    assert solution.validPalindrome("humwhk") == False
    assert solution.validPalindrome("vuvykc") == False
    assert solution.validPalindrome("hql") == False
    assert solution.validPalindrome("kcasnwtqe") == False
    assert solution.validPalindrome("qmmpk") == False
    assert solution.validPalindrome("igw") == False
    assert solution.validPalindrome("fak") == False
    assert solution.validPalindrome("uobdsicsi") == False
    assert solution.validPalindrome("jdaku") == False
    assert solution.validPalindrome("uz") == True
    assert solution.validPalindrome("ylajjnibwf") == False
    assert solution.validPalindrome("t") == True
    assert solution.validPalindrome("mxnjehwvcd") == False
    assert solution.validPalindrome("hsxencyo") == False
    assert solution.validPalindrome("rwjipl") == False
    assert solution.validPalindrome("xaazq") == False
    assert solution.validPalindrome("n") == True
    assert solution.validPalindrome("xvyynycml") == False
    assert solution.validPalindrome("qfawwgbmpe") == False
    assert solution.validPalindrome("zk") == True
    assert solution.validPalindrome("pnpukfde") == False
    assert solution.validPalindrome("rnr") == True
    assert solution.validPalindrome("uom") == False
    assert solution.validPalindrome("whapzzlb") == False
    assert solution.validPalindrome("qpyc") == False
    assert solution.validPalindrome("vve") == True
    assert solution.validPalindrome("ewfao") == False
    assert solution.validPalindrome("w") == True
    assert solution.validPalindrome("gxure") == False
    assert solution.validPalindrome("vhgr") == False
    assert solution.validPalindrome("goavwewl") == False
    assert solution.validPalindrome("wntsscl") == False
    assert solution.validPalindrome("pyreq") == False
    assert solution.validPalindrome("rbrfkbjd") == False
    assert solution.validPalindrome("kyklr") == False
    assert solution.validPalindrome("xorgclrf") == False
    assert solution.validPalindrome("itgkgzdcl") == False
    assert solution.validPalindrome("webzn") == False
    assert solution.validPalindrome("qftnlqwixz") == False
    assert solution.validPalindrome("ucoxt") == False
    assert solution.validPalindrome("hjupfdps") == False
    assert solution.validPalindrome("toescorfn") == False
    assert solution.validPalindrome("roudolimv") == False
    assert solution.validPalindrome("zxcbfhbq") == False

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
