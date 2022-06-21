def minWindow(s: str, t: str) -> str:
    start = 0
    end = 0
    head = 0
    hash_table = dict()
    length_t = len(t)
    length_s = len(s)
    min_len = length_s + 1
    for char in t:
        hash_table[char] = hash_table.get(char, 0) + 1

    while end < length_s:
        if s[end] in hash_table:
            if hash_table[s[end]] > 0:
                length_t -= 1
            hash_table[s[end]] -= 1
        end += 1
        while length_t == 0:
            if end-start < min_len:
                min_len = end - start
                head = start
            if s[start] in hash_table:
                hash_table[s[start]] += 1
                if hash_table[s[start]] > 0:
                    length_t += 1
            start += 1
    return s[head : head + min_len] if min_len < length_s + 1 else ""


s = "ADOBECODEBANC"
t = "AOBC"
# t = "ABC"
# s = "a"
# t = "a"
# s = "a"
# t = "aa"
print(minWindow(s, t))
