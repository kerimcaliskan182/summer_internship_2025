#Task 3: Longest Substring Without Repeating Characters

def LongestSubstring(s):
    seen = {}
    l = 0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        length = max(length, r - l + 1)
        seen[char] = r
    return length

# Testler 
test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("abcdef", 6),
    ("abba", 2),
]
    
for s, expected in test_cases:
    result = LongestSubstring(s)
    print(f"Input: {s} → Output: {result} (Expected: {expected})")
