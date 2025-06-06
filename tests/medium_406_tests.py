from medium_406_canon import Solution as SolutionCanon
from chatgpt_medium_406 import Solution as SolutionChatGPT
from claude_medium_406 import Solution as SolutionClaude
from gemini_medium_406 import Solution as SolutionGemini


def run_basic_tests(solution):
    assert solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    assert solution.reconstructQueue([[6,0], [5,0], [4,0], [3,2], [2,2], [1,4]]) == [[4,0], [5,0], [2,2], [3,2], [1,4], [6,0]]

def run_advanced_tests(solution):
    assert solution.reconstructQueue([[95, 1], [94, 4], [88, 3], [76, 4], [22, 0], [18, 2], [15, 2], [12, 2], [9, 5]]) == [[22, 0], [95, 1], [12, 2], [15, 2], [18, 2], [9, 5], [94, 4], [88, 3], [76, 4]]
    assert solution.reconstructQueue([[70, 1], [68, 1], [55, 0]]) == [[55, 0], [70, 1], [68, 1]]
    assert solution.reconstructQueue([[66, 1], [47, 1], [27, 0], [26, 0], [24, 1]]) == [[26, 0], [24, 1], [27, 0], [66, 1], [47, 1]]
    assert solution.reconstructQueue([[95, 0], [85, 5], [81, 2], [79, 4], [76, 3], [60, 1], [29, 0], [1, 0]]) == [[1, 0], [29, 0], [95, 0], [60, 1], [85, 5], [81, 2], [76, 3], [79, 4]]
    assert solution.reconstructQueue([[69, 1], [60, 0], [42, 1]]) == [[60, 0], [42, 1], [69, 1]]
    assert solution.reconstructQueue([[25, 0], [25, 0], [14, 0], [14, 1]]) == [[14, 0], [14, 1], [25, 0], [25, 0]]
    assert solution.reconstructQueue([[86, 0], [58, 3], [55, 0], [45, 2], [17, 2], [13, 4], [8, 1], [8, 3], [2, 4]]) == [[55, 0], [8, 1], [86, 0], [8, 3], [2, 4], [17, 2], [45, 2], [13, 4], [58, 3]]
    assert solution.reconstructQueue([[98, 3], [88, 1], [73, 0], [71, 4], [68, 0], [66, 0], [10, 0]]) == [[10, 0], [66, 0], [68, 0], [73, 0], [98, 3], [88, 1], [71, 4]]
    assert solution.reconstructQueue([[99, 0], [92, 1], [62, 0], [49, 0], [42, 0], [33, 2], [30, 1], [3, 0]]) == [[3, 0], [42, 0], [30, 1], [49, 0], [33, 2], [62, 0], [99, 0], [92, 1]]
    assert solution.reconstructQueue([[72, 1], [67, 2], [25, 0], [23, 0]]) == [[23, 0], [25, 0], [72, 1], [67, 2]]
    assert solution.reconstructQueue([[40, 0], [34, 1]]) == [[40, 0], [34, 1]]
    assert solution.reconstructQueue([[91, 2], [85, 1], [81, 0], [64, 0], [58, 2], [37, 2], [34, 2], [8, 7], [5, 0], [2, 1]]) == [[5, 0], [2, 1], [64, 0], [81, 0], [34, 2], [37, 2], [58, 2], [91, 2], [85, 1], [8, 7]]
    assert solution.reconstructQueue([[14, 1], [14, 1], [2, 0]]) == [[2, 0], [14, 1], [14, 1]]
    assert solution.reconstructQueue([[94, 5], [90, 2], [38, 0], [35, 0], [32, 4], [15, 1], [3, 1]]) == [[35, 0], [3, 1], [15, 1], [38, 0], [94, 5], [90, 2], [32, 4]]
    assert solution.reconstructQueue([[74, 0], [61, 1], [54, 3], [48, 3], [46, 1], [30, 2], [19, 1], [2, 1]]) == [[74, 0], [2, 1], [19, 1], [46, 1], [30, 2], [61, 1], [54, 3], [48, 3]]
    assert solution.reconstructQueue([[23, 0], [20, 0]]) == [[20, 0], [23, 0]]
    assert solution.reconstructQueue([[86, 3], [76, 0], [76, 5], [74, 2], [72, 3], [68, 8], [51, 3], [47, 0], [16, 4], [12, 1]]) == [[47, 0], [12, 1], [76, 0], [86, 3], [74, 2], [16, 4], [51, 3], [72, 3], [76, 5], [68, 8]]
    assert solution.reconstructQueue([[45, 0], [21, 1]]) == [[45, 0], [21, 1]]
    assert solution.reconstructQueue([[70, 0], [40, 0], [32, 0], [19, 0], [17, 2]]) == [[19, 0], [32, 0], [17, 2], [40, 0], [70, 0]]
    assert solution.reconstructQueue([[95, 2], [62, 1], [57, 1], [55, 2], [46, 0], [38, 0], [14, 1]]) == [[38, 0], [14, 1], [46, 0], [95, 2], [57, 1], [55, 2], [62, 1]]
    assert solution.reconstructQueue([[85, 2], [77, 0], [68, 3], [65, 3], [59, 0], [56, 0], [13, 5], [11, 1]]) == [[56, 0], [11, 1], [59, 0], [77, 0], [85, 2], [68, 3], [13, 5], [65, 3]]
    assert solution.reconstructQueue([[86, 0], [39, 0]]) == [[39, 0], [86, 0]]
    assert solution.reconstructQueue([[96, 4], [87, 3], [70, 0], [66, 4], [41, 0], [32, 1], [20, 0], [10, 1]]) == [[20, 0], [10, 1], [41, 0], [32, 1], [70, 0], [96, 4], [87, 3], [66, 4]]
    assert solution.reconstructQueue([[70, 2], [66, 0], [40, 3], [39, 0]]) == [[39, 0], [66, 0], [70, 2], [40, 3]]
    assert solution.reconstructQueue([[100, 8], [87, 0], [77, 0], [76, 0], [54, 1], [46, 6], [41, 1], [27, 0], [24, 2], [3, 1]]) == [[27, 0], [3, 1], [76, 0], [24, 2], [41, 1], [54, 1], [77, 0], [87, 0], [100, 8], [46, 6]]
    assert solution.reconstructQueue([[100, 4], [83, 1], [68, 1], [64, 4], [49, 6], [44, 2], [25, 1], [21, 0]]) == [[21, 0], [100, 4], [25, 1], [68, 1], [44, 2], [83, 1], [64, 4], [49, 6]]
    assert solution.reconstructQueue([[83, 2], [70, 1], [51, 5], [45, 4], [41, 0], [39, 1], [28, 0], [2, 4]]) == [[28, 0], [41, 0], [39, 1], [83, 2], [2, 4], [70, 1], [51, 5], [45, 4]]
    assert solution.reconstructQueue([[68, 1], [9, 0], [3, 0]]) == [[3, 0], [9, 0], [68, 1]]
    assert solution.reconstructQueue([[85, 2], [53, 3], [23, 2], [15, 0], [6, 0], [5, 4], [3, 5]]) == [[6, 0], [15, 0], [85, 2], [53, 3], [5, 4], [3, 5], [23, 2]]
    assert solution.reconstructQueue([[73, 1], [72, 0], [50, 0]]) == [[50, 0], [72, 0], [73, 1]]
    assert solution.reconstructQueue([[74, 1], [61, 0], [30, 1]]) == [[61, 0], [30, 1], [74, 1]]
    assert solution.reconstructQueue([[94, 6], [92, 0], [75, 0], [71, 1], [63, 6], [58, 1], [38, 8], [28, 2], [16, 2], [16, 9]]) == [[75, 0], [58, 1], [16, 2], [28, 2], [71, 1], [92, 0], [94, 6], [63, 6], [38, 8], [16, 9]]
    assert solution.reconstructQueue([[62, 1], [38, 0], [38, 0], [33, 1], [25, 0], [0, 1]]) == [[25, 0], [0, 1], [38, 0], [33, 1], [38, 0], [62, 1]]
    assert solution.reconstructQueue([[69, 2], [45, 0], [41, 1], [20, 0]]) == [[20, 0], [45, 0], [41, 1], [69, 2]]
    assert solution.reconstructQueue([[89, 0], [50, 1], [34, 0]]) == [[34, 0], [89, 0], [50, 1]]
    assert solution.reconstructQueue([[95, 0], [93, 0], [89, 2], [80, 0], [59, 4], [41, 1], [38, 4], [18, 1], [17, 2], [15, 3]]) == [[80, 0], [18, 1], [17, 2], [15, 3], [41, 1], [93, 0], [95, 0], [38, 4], [89, 2], [59, 4]]
    assert solution.reconstructQueue([[82, 0]]) == [[82, 0]]
    assert solution.reconstructQueue([[63, 0], [58, 2], [44, 3], [35, 1], [31, 0], [27, 0], [18, 0]]) == [[18, 0], [27, 0], [31, 0], [63, 0], [35, 1], [58, 2], [44, 3]]
    assert solution.reconstructQueue([[94, 0], [82, 2], [80, 2], [52, 3], [48, 0], [42, 0]]) == [[42, 0], [48, 0], [94, 0], [82, 2], [80, 2], [52, 3]]
    assert solution.reconstructQueue([[91, 0], [81, 0], [76, 1], [68, 0], [66, 2], [64, 0], [47, 3], [28, 2], [14, 2], [7, 0]]) == [[7, 0], [64, 0], [68, 0], [14, 2], [28, 2], [81, 0], [47, 3], [66, 2], [76, 1], [91, 0]]
    assert solution.reconstructQueue([[33, 0]]) == [[33, 0]]
    assert solution.reconstructQueue([[23, 2], [16, 1], [13, 0]]) == [[13, 0], [23, 2], [16, 1]]
    assert solution.reconstructQueue([[89, 0], [31, 0]]) == [[31, 0], [89, 0]]
    assert solution.reconstructQueue([[82, 0], [81, 1], [80, 3], [63, 2], [55, 7], [41, 1], [36, 2], [14, 3]]) == [[82, 0], [41, 1], [36, 2], [14, 3], [81, 1], [63, 2], [80, 3], [55, 7]]
    assert solution.reconstructQueue([[89, 0]]) == [[89, 0]]
    assert solution.reconstructQueue([[89, 0], [80, 3], [79, 0], [73, 0], [73, 0], [27, 0], [10, 2], [5, 3]]) == [[27, 0], [73, 0], [10, 2], [5, 3], [73, 0], [79, 0], [89, 0], [80, 3]]
    assert solution.reconstructQueue([[97, 1], [91, 3], [73, 0], [73, 1], [54, 0], [50, 8], [25, 0], [25, 1], [20, 1], [16, 6]]) == [[25, 0], [20, 1], [25, 1], [54, 0], [73, 0], [73, 1], [16, 6], [97, 1], [91, 3], [50, 8]]
    assert solution.reconstructQueue([[32, 0], [19, 1]]) == [[32, 0], [19, 1]]
    assert solution.reconstructQueue([[90, 0], [83, 7], [62, 2], [58, 4], [57, 1], [46, 2], [30, 3], [2, 0]]) == [[2, 0], [90, 0], [57, 1], [46, 2], [30, 3], [83, 7], [62, 2], [58, 4]]
    assert solution.reconstructQueue([[36, 0], [28, 0]]) == [[28, 0], [36, 0]]
    assert solution.reconstructQueue([[92, 4], [86, 4], [34, 7], [32, 0], [22, 0], [21, 0], [10, 0], [10, 2]]) == [[10, 0], [21, 0], [10, 2], [22, 0], [32, 0], [92, 4], [86, 4], [34, 7]]
    assert solution.reconstructQueue([[81, 0], [81, 5], [81, 6], [67, 4], [61, 0], [53, 2], [36, 5], [16, 0], [5, 6], [4, 2]]) == [[16, 0], [61, 0], [4, 2], [81, 0], [53, 2], [81, 5], [81, 6], [5, 6], [36, 5], [67, 4]]
    assert solution.reconstructQueue([[95, 1], [78, 0]]) == [[78, 0], [95, 1]]
    assert solution.reconstructQueue([[95, 0], [87, 0], [72, 3], [60, 1], [47, 0], [7, 1]]) == [[47, 0], [7, 1], [87, 0], [60, 1], [95, 0], [72, 3]]
    assert solution.reconstructQueue([[86, 1], [83, 0], [80, 4], [63, 2], [60, 0], [52, 2], [40, 1], [11, 7], [2, 0]]) == [[2, 0], [60, 0], [40, 1], [83, 0], [52, 2], [86, 1], [63, 2], [80, 4], [11, 7]]
    assert solution.reconstructQueue([[85, 0]]) == [[85, 0]]
    assert solution.reconstructQueue([[60, 1], [3, 0]]) == [[3, 0], [60, 1]]
    assert solution.reconstructQueue([[46, 1], [5, 0]]) == [[5, 0], [46, 1]]
    assert solution.reconstructQueue([[73, 1], [72, 2], [61, 1], [54, 3], [52, 0], [38, 0], [27, 1], [18, 8], [17, 1], [0, 5]]) == [[38, 0], [17, 1], [27, 1], [52, 0], [73, 1], [0, 5], [61, 1], [72, 2], [54, 3], [18, 8]]
    assert solution.reconstructQueue([[89, 2], [74, 3], [70, 0], [45, 1], [34, 3], [28, 1], [27, 5], [23, 6], [13, 2]]) == [[70, 0], [28, 1], [13, 2], [45, 1], [89, 2], [34, 3], [27, 5], [23, 6], [74, 3]]
    assert solution.reconstructQueue([[66, 3], [49, 5], [39, 4], [24, 0], [24, 0], [19, 0], [9, 0]]) == [[9, 0], [19, 0], [24, 0], [24, 0], [66, 3], [49, 5], [39, 4]]
    assert solution.reconstructQueue([[97, 2], [96, 1], [83, 1], [82, 1], [62, 1], [19, 0]]) == [[19, 0], [97, 2], [62, 1], [82, 1], [83, 1], [96, 1]]
    assert solution.reconstructQueue([[99, 2], [87, 9], [83, 0], [75, 1], [69, 3], [67, 1], [49, 2], [35, 4], [15, 4], [1, 5]]) == [[83, 0], [67, 1], [49, 2], [75, 1], [15, 4], [1, 5], [35, 4], [99, 2], [69, 3], [87, 9]]
    assert solution.reconstructQueue([[57, 1], [34, 3], [28, 0], [9, 0]]) == [[9, 0], [28, 0], [57, 1], [34, 3]]
    assert solution.reconstructQueue([[44, 0], [9, 1], [4, 0]]) == [[4, 0], [44, 0], [9, 1]]
    assert solution.reconstructQueue([[96, 0], [91, 3], [77, 0], [71, 6], [66, 5], [42, 2], [26, 0], [11, 2]]) == [[26, 0], [77, 0], [11, 2], [96, 0], [42, 2], [91, 3], [71, 6], [66, 5]]
    assert solution.reconstructQueue([[86, 0], [19, 0]]) == [[19, 0], [86, 0]]
    assert solution.reconstructQueue([[96, 0], [88, 3], [67, 4], [65, 1], [58, 2], [56, 3], [44, 1], [28, 0], [23, 2]]) == [[28, 0], [96, 0], [23, 2], [44, 1], [65, 1], [58, 2], [56, 3], [88, 3], [67, 4]]
    assert solution.reconstructQueue([[95, 0], [52, 2], [18, 0]]) == [[18, 0], [95, 0], [52, 2]]
    assert solution.reconstructQueue([[77, 2], [71, 2], [69, 4], [43, 0], [11, 0]]) == [[11, 0], [43, 0], [77, 2], [71, 2], [69, 4]]
    assert solution.reconstructQueue([[96, 0], [78, 0], [15, 0], [7, 0], [4, 2]]) == [[7, 0], [15, 0], [4, 2], [78, 0], [96, 0]]
    assert solution.reconstructQueue([[91, 0], [71, 0]]) == [[71, 0], [91, 0]]
    assert solution.reconstructQueue([[51, 0], [37, 2], [34, 0], [24, 2], [4, 2]]) == [[34, 0], [51, 0], [4, 2], [24, 2], [37, 2]]
    assert solution.reconstructQueue([[85, 0], [85, 3], [82, 2], [62, 0], [57, 0], [45, 8], [27, 7], [13, 0], [7, 1], [2, 1]]) == [[13, 0], [2, 1], [7, 1], [57, 0], [62, 0], [85, 0], [85, 3], [82, 2], [45, 8], [27, 7]]
    assert solution.reconstructQueue([[90, 3], [82, 0], [73, 5], [71, 3], [52, 0], [49, 0], [45, 1], [44, 4], [43, 0], [42, 7]]) == [[43, 0], [49, 0], [45, 1], [52, 0], [82, 0], [44, 4], [90, 3], [42, 7], [73, 5], [71, 3]]
    assert solution.reconstructQueue([[95, 3], [93, 4], [89, 6], [84, 1], [71, 1], [67, 2], [2, 0]]) == [[2, 0], [95, 3], [71, 1], [67, 2], [84, 1], [93, 4], [89, 6]]
    assert solution.reconstructQueue([[97, 1], [78, 3], [73, 3], [68, 2], [41, 1], [12, 2], [6, 0], [3, 0]]) == [[3, 0], [6, 0], [97, 1], [41, 1], [12, 2], [78, 3], [68, 2], [73, 3]]
    assert solution.reconstructQueue([[100, 0], [49, 1]]) == [[100, 0], [49, 1]]
    assert solution.reconstructQueue([[73, 2], [64, 1], [60, 0], [25, 2]]) == [[60, 0], [73, 2], [25, 2], [64, 1]]
    assert solution.reconstructQueue([[80, 2], [79, 1], [76, 3], [66, 0], [62, 0], [42, 2], [34, 1], [21, 1], [20, 5]]) == [[62, 0], [21, 1], [34, 1], [66, 0], [42, 2], [20, 5], [80, 2], [79, 1], [76, 3]]
    assert solution.reconstructQueue([[60, 0]]) == [[60, 0]]
    assert solution.reconstructQueue([[5, 0]]) == [[5, 0]]
    assert solution.reconstructQueue([[97, 1], [84, 0], [69, 0], [62, 1], [53, 0], [47, 0], [34, 1]]) == [[47, 0], [34, 1], [53, 0], [69, 0], [62, 1], [84, 0], [97, 1]]
    assert solution.reconstructQueue([[100, 0], [89, 0], [83, 4], [79, 3], [76, 4], [73, 3], [72, 2], [61, 0], [24, 6], [14, 5]]) == [[61, 0], [89, 0], [100, 0], [72, 2], [83, 4], [14, 5], [73, 3], [24, 6], [79, 3], [76, 4]]
    assert solution.reconstructQueue([[92, 0], [70, 1]]) == [[92, 0], [70, 1]]
    assert solution.reconstructQueue([[73, 1], [69, 1], [62, 0]]) == [[62, 0], [73, 1], [69, 1]]
    assert solution.reconstructQueue([[92, 0], [79, 1], [74, 0], [65, 1], [62, 6], [55, 4], [13, 5], [3, 0]]) == [[3, 0], [74, 0], [65, 1], [92, 0], [79, 1], [55, 4], [13, 5], [62, 6]]
    assert solution.reconstructQueue([[95, 6], [78, 6], [69, 0], [37, 4], [30, 1], [26, 3], [22, 3], [2, 1]]) == [[69, 0], [2, 1], [30, 1], [95, 6], [22, 3], [26, 3], [78, 6], [37, 4]]
    assert solution.reconstructQueue([[46, 1], [22, 0]]) == [[22, 0], [46, 1]]
    assert solution.reconstructQueue([[96, 1], [79, 0], [74, 7], [71, 4], [56, 0], [55, 2], [45, 6], [12, 0], [1, 0]]) == [[1, 0], [12, 0], [56, 0], [79, 0], [55, 2], [96, 1], [74, 7], [71, 4], [45, 6]]
    assert solution.reconstructQueue([[85, 0], [20, 1]]) == [[85, 0], [20, 1]]
    assert solution.reconstructQueue([[88, 0], [9, 0]]) == [[9, 0], [88, 0]]
    assert solution.reconstructQueue([[98, 2], [95, 2], [75, 0], [71, 2], [60, 4], [46, 6], [43, 3], [38, 0], [34, 2], [23, 1]]) == [[38, 0], [23, 1], [75, 0], [34, 2], [98, 2], [71, 2], [43, 3], [95, 2], [60, 4], [46, 6]]
    assert solution.reconstructQueue([[97, 3], [95, 1], [43, 0], [13, 0]]) == [[13, 0], [43, 0], [97, 3], [95, 1]]
    assert solution.reconstructQueue([[78, 4], [78, 4], [75, 2], [70, 4], [62, 2], [56, 1], [53, 2], [16, 0], [11, 0]]) == [[11, 0], [16, 0], [78, 4], [56, 1], [53, 2], [78, 4], [62, 2], [75, 2], [70, 4]]
    assert solution.reconstructQueue([[92, 0], [90, 0], [89, 7], [76, 5], [51, 4], [39, 0], [25, 0], [4, 0], [3, 0], [3, 4]]) == [[3, 0], [4, 0], [25, 0], [39, 0], [3, 4], [90, 0], [92, 0], [89, 7], [76, 5], [51, 4]]
    assert solution.reconstructQueue([[58, 0]]) == [[58, 0]]
    assert solution.reconstructQueue([[90, 1], [82, 0], [44, 0], [34, 0], [17, 3]]) == [[34, 0], [44, 0], [82, 0], [17, 3], [90, 1]]
    assert solution.reconstructQueue([[99, 0], [99, 3], [81, 0], [63, 3], [20, 1], [14, 2], [13, 0], [13, 6]]) == [[13, 0], [81, 0], [20, 1], [14, 2], [99, 0], [99, 3], [13, 6], [63, 3]]
    assert solution.reconstructQueue([[98, 0], [96, 0], [92, 5], [71, 1], [68, 0], [60, 2], [16, 6], [7, 4], [1, 0]]) == [[1, 0], [68, 0], [96, 0], [60, 2], [71, 1], [7, 4], [98, 0], [92, 5], [16, 6]]

def run_timed_tests(solution):
    assert solution.reconstructQueue([[95, 1], [94, 4], [88, 3], [76, 4], [22, 0], [18, 2], [15, 2], [12, 2], [9, 5]]) == [[22, 0], [95, 1], [12, 2], [15, 2], [18, 2], [9, 5], [94, 4], [88, 3], [76, 4]]
    assert solution.reconstructQueue([[70, 1], [68, 1], [55, 0]]) == [[55, 0], [70, 1], [68, 1]]
    assert solution.reconstructQueue([[66, 1], [47, 1], [27, 0], [26, 0], [24, 1]]) == [[26, 0], [24, 1], [27, 0], [66, 1], [47, 1]]
    assert solution.reconstructQueue([[95, 0], [85, 5], [81, 2], [79, 4], [76, 3], [60, 1], [29, 0], [1, 0]]) == [[1, 0], [29, 0], [95, 0], [60, 1], [85, 5], [81, 2], [76, 3], [79, 4]]
    assert solution.reconstructQueue([[69, 1], [60, 0], [42, 1]]) == [[60, 0], [42, 1], [69, 1]]
    assert solution.reconstructQueue([[25, 0], [25, 0], [14, 0], [14, 1]]) == [[14, 0], [14, 1], [25, 0], [25, 0]]
    assert solution.reconstructQueue([[86, 0], [58, 3], [55, 0], [45, 2], [17, 2], [13, 4], [8, 1], [8, 3], [2, 4]]) == [[55, 0], [8, 1], [86, 0], [8, 3], [2, 4], [17, 2], [45, 2], [13, 4], [58, 3]]
    assert solution.reconstructQueue([[98, 3], [88, 1], [73, 0], [71, 4], [68, 0], [66, 0], [10, 0]]) == [[10, 0], [66, 0], [68, 0], [73, 0], [98, 3], [88, 1], [71, 4]]
    assert solution.reconstructQueue([[99, 0], [92, 1], [62, 0], [49, 0], [42, 0], [33, 2], [30, 1], [3, 0]]) == [[3, 0], [42, 0], [30, 1], [49, 0], [33, 2], [62, 0], [99, 0], [92, 1]]
    assert solution.reconstructQueue([[72, 1], [67, 2], [25, 0], [23, 0]]) == [[23, 0], [25, 0], [72, 1], [67, 2]]
        

def save_output(output: str):
    with open('../times.csv', 'a') as f:
        f.write(f'{output}\n')

if __name__ == '__main__':
    import sys
    problem_id = 406
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

        output += f'medium_406,{sys.argv[2]},'
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