class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        l = 0
        res = ''
        dict_ = defaultdict(int)
        wind_dict = defaultdict(int)
        for i in range(len(t)):
            dict_[t[i]] += 1

        need = len(dict_)
        have = 0
        for r in range(0, len(s)):
            wind_dict[s[r]] += 1
            if s[r] in dict_ and wind_dict[s[r]] == dict_[s[r]]:
                have += 1

            while need == have:
                if len(s[l : r + 1]) < len(res) or res == '':
                    res = s[l : r + 1]
                wind_dict[s[l]] -= 1
                if wind_dict[s[l]] < dict_[s[l]]:
                    have -= 1
                l += 1

        return res