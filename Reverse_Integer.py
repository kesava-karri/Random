class Solution(object):
  def reverse(self, x):
    # based on x, s gives -1, 0 or 1;
    # False=0; True=1
    s = (x > 0) - (x < 0)
    # Making it positive no matter whether it's -ve or +ve
    r = int(str(x*s)[::-1])
    # We multiply to with s again which makes the int to return to it's original sign
    return s*r * (r < 2**31)
      

jk = Solution()

print(jk.reverse(-123))
print(jk.reverse(2147483648))
print(jk.reverse(-2147483648))
print(jk.reverse(0))
print(jk.reverse(1200))
print(jk.reverse(21))