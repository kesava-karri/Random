class Solution:
  def isPalindrome_betterWay(self, x: int) -> bool:
    # rather than inverting the entire num, 
    # we can decide it going half way through.
    temp = x
    reversed_num = 0
    if x<0 or (x>0 and x%10 == 0):
      return False
    
    while reversed_num < x:
      reversed_num = reversed_num * 10 + temp%10
      temp = temp//10
      
    return True if (reversed_num == x or reversed_num//10 == x) else False


  def isPalindrome(self, x: int) -> bool:
    temp = x
    num_len = len(str(temp))
    reversed_num = 0
    # iterate through length of the number
    for _ in range(num_len):
      # get one's place value
      rem = temp%10
      # floor division to get digits other than one's place value
      temp = temp//10
      # multiplying remainder(rem) with 10^(len-1) to reverse it
      reversed_num = reversed_num + rem*10**(num_len-1) 
      num_len-=1
    return True if x == reversed_num else False

  def isPalindrome_stringMethod(self, x: int) -> bool:
    return True if str(x)[::-1] == str(x) else False





obj = Solution()
print(obj.isPalindrome(123))
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))
print(obj.isPalindrome(-101))