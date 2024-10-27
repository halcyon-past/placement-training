"""
273. Integer to English Words
Solved
Hard
Topics
Companies
Hint
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""

class Solution:
    eng = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    eng2 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    eng3 = ["", "Thousand", "Million", "Billion"]

    def toEnglish(self,num):
        ans = ""
        if num>=100:
            q,r = divmod(num,100)
            ans += self.eng[q]+" Hundred "
            num = r
        
        if num>=20:
            q2,r2 = divmod(num,10)
            ans += self.eng2[q2]
            if r2>0:
                ans += " "+self.eng[r2]
        
        elif num>0:
            ans += self.eng[num]

        if ans and ans[-1] == ' ':
            ans = ans[:-1]
        
        return ans

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ans = ""
        count = 0
        
        while num > 0:
            num, r = divmod(num, 1000)
            if r > 0:
                part = self.toEnglish(r) + " " + self.eng3[count]
                ans = part.strip() + " " + ans.strip()
            count += 1
        
        return ans.strip()

# Test Cases

test = Solution()
assert test.numberToWords(123) == "One Hundred Twenty Three"
assert test.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
assert test.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

print("All passed")