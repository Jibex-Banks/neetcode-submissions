class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        sets = list(set(nums))
        output = []

        for i in range(len(sets)):
            counts[sets[i]] = nums.count(sets[i])
        
        # Sort the items (key-value pairs) by value in descending order
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
       
        for i in range(k):
            # Append the key (the element) from the sorted items
            output.append(sorted_items[i][0])
        return output