class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index, small = self.findSmallestString(strs)
        smallest_word = str(strs[index])

        length = small

        if len(strs) == 1:
            return smallest_word

        if length == 1:
            for i in strs:
                if smallest_word[0] != i[0]:
                    return ""
            return smallest_word
        else:
            ans = 0
            truth_table = []
            prefix = smallest_word
            for k in range(1,length+1):
                stop = length - k + 1
                print(stop)
                prefix = smallest_word[:stop]
                for a in strs:
                    if a.startswith(prefix):
                        truth_table.append(1)
                    else:
                        truth_table.append(0)
                ans = 0     
                print(truth_table)
                for t in truth_table:
                    ans += t
                truth_table = []
                print("Ans: ",ans)
                if ans == len(strs):
                    return prefix
                
            return ""


            
    def findSmallestString(self, strings: List[str]) -> int:
        lengths = []
        for i in strings:
            lengths.append(len(i))
        smallest_length = min(lengths)
        index = lengths.index(smallest_length)
        return index, smallest_length
