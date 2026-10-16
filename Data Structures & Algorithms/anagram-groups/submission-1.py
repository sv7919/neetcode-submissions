class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        answer = []

        for string in strs:
            sorted_copy = "".join(sorted(string))
            if sorted_copy not in groups:
                groups[sorted_copy] = [string]
            else:
                groups[sorted_copy].append(string)
        
        for item in groups.values():
            answer.append(item)

        return answer
        