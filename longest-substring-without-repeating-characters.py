def lengthOfLongestSubstring(s: str):
    start = 0
    end = 0
    hash = set()
    string_size = len(s)
    longest_substring = 0

    while end < string_size:
        if s[end] in hash:
            hash.remove(s[start])
            start += 1
        else:
            hash.add(s[end])
            end += 1
            longest_substring = max(len(hash), longest_substring)

    return longest_substring


s = "abcabcbb"
# s = "abc"
# s = "abbbbb"
# s = "pwwkew"
print(lengthOfLongestSubstring(s))
