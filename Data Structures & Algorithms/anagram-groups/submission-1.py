class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = dict()
        for string in strs:
            sortedStrings = sorted(string)
            label = "".join(sortedStrings)
            if label not in sublist:
                sublist[label] = []
            sublist[label].append(string)
        return list(sublist.values())