class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1.0
        elif n<0: return 1.0/self.myPow(x,-n)
#        else: return self.myPow(x,n-1)*x # maximum recursion depth exceeded!
        elif n%2==0: return self.myPow(x*x,n/2) # to avoid above error, this and the following line have to be used
        else: return self.myPow(x*x,n/2)*x
