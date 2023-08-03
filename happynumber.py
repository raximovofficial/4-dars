class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_square_sum(number):
            return sum(int(digit) ** 2 for digit in str(number))
       
        seen_numbers = set()
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = calculate_square_sum(n)
        
        return n == 1
       
       
        # digits = [int(digit) for digit in str(n)]
    
        # while True:
        #     for i in range(len(digits)-1):
        #         digits[i] ** 2 + digits[i+1] ** 2 == 100
            
            

a = Solution()
print(a.isHappy(n = "19"))
print(a.isHappy(n = "2"))

