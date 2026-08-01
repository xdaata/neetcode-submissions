class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        dict_ = defaultdict(int)
        wind_dict = defaultdict(int)
        for i in range(len(s1)):
            dict_[s1[i]] += 1
            wind_dict[s2[i]] += 1
        
        if wind_dict == dict_:
            return True

        for i in range(len(s1), len(s2)):
            wind_dict[s2[i]] += 1
            wind_dict[s2[i - len(s1)]] -= 1
            if wind_dict[s2[i - len(s1)]] == 0:
                del wind_dict[s2[i - len(s1)]]
            if wind_dict == dict_:
                return True

        return False