class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_list = []
        new_strs = ["".join(sorted(k.lower())) for k in strs]
        for i in range(len(strs)):
            new_list = []
            for j in range(len(strs)):
                if i == j:
                    new_list.append(strs[i])
                elif new_strs[i] == new_strs[j]:
                    new_list.append(strs[j])
            return_list.append(new_list)
        return_lists = []
        ans = [return_lists.append(z) for z in return_list if z not in return_lists]
        return return_lists