class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dik = {}
        n = len(strs)
        for i in range(n):
            key = "".join(sorted(strs[i]))
            if key in dik:
                dik[key].append(strs[i])
            else:
                dik[key] = [strs[i]]
        return list(dik.values())