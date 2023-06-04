def firstUniqChar(s):
    char_count = {}

    # Update frequency count for each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    return -1

s = "loveleetcode" 
print(firstUniqChar(s)) # Output 2
s1 = "aabb"
print(firstUniqChar(s1)) # Output -1
s2='leetcode'
print(firstUniqChar(s2)) # Output 0

