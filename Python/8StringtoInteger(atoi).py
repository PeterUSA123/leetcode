__author__ = 'minyi'
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str)==0:
            return 0
        maxInt = 2**31-1
        minInt = -2**31

        for i in range(len(str)):
            if str[i]!=' ':
                break
        str = str[i:]

        ans = 0
        positive = 1
        if str[0]=='-':
            positive = -1
        elif str[0]=='+':
            positive = 1
        elif ord(str[0])-ord('0')>=0 and ord(str[0])-ord('0')<=9:
            ans = ord(str[0])-ord('0')
        else:
            return 0
        i=1
        while i<len(str):
            if ord(str[i])-ord('0')>=0 and ord(str[i])-ord('0')<=9:
                ans = ans*10 +ord(str[i])-ord('0')
                if ans > maxInt:
                    break
            else:
                break
            i +=1
        ans *= positive
        if ans>maxInt or ans <minInt:
            if ans>0:
                return  maxInt
            else:
                return minInt
        return ans

s= Solution()
print
print (s.myAtoi("1532526"))