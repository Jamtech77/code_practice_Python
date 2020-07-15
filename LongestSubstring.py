class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    tmp = ""
    high_score = 0
    for i in range(len(s)):
        print(s[i:])
        for i in s[i:]:
            if high_score < len(tmp):
                high_score = len(tmp)
            if i in tmp:
                tmp = ""
                break
            tmp += i
    return high_score

print( Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx') )
# 10
