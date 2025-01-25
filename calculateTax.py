# Time :O(n)
# Space:O(1)// stack space for recursion
# Leetcode:Yes
# Issues:No

# 2 ms
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        idx = 0
        lower = 0

        while income > 0:
            br = brackets[idx]
            upper = br[0]               
            perc = br[1]

            taxable = min(income,upper-lower)           # 15k vs 20k

            tax += taxable*(perc/100.00)

            lower = upper
            idx +=1
            income = income - taxable

        
        return tax
    
# recursion 0ms 
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        return self.helper(brackets,income,0,0)     
    def helper(self,brackets,income,lower,idx):
        # Basecase
        if income <= 0: return 0
        #logic

        tax = 0
        br = brackets[idx]
        upper = br[0]
        percent = br[1]

        taxable = min(income,upper-lower)
        tax += taxable * (percent/100) +     self.helper(brackets,income- taxable, upper,idx+1) # call helper
        return tax    