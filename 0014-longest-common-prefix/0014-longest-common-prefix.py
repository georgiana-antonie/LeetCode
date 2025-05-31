class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sorted_strs = sorted(strs, key=len)
        min_str = sorted_strs[0]
        prefix = ""
        for i in range(len(min_str)):
            current_letter = min_str[i]
            for str in sorted_strs[1:]:
                if str[i] != current_letter:
                    return prefix
            prefix += current_letter
        return prefix

