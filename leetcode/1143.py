def longestCommonSubsequence(text1: str, text2: str) -> int:
    shorter_str = text1 if len(text1) <= len(text2) else text2
    longer_str = text2 if len(text1) <= len(text2) else text1
    for i in range(0, len(shorter_str)-1):
        for j in range(len(shorter_str), 1, -1):
            search_str = shorter_str[i:j]
            if search_str in longer_str:
                return len(search_str)
    return 0
longestCommonSubsequence("abcde","ace")