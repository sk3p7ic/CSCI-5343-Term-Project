from typing import *
from collections import *
from itertools import *
from functools import *
from operator import *
from bisect import *
from heapq import *
from math import *

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for v in cnt.values():
            ans += v - (v & 1)
            ans += (ans & 1 ^ 1) and (v & 1)
        return ans