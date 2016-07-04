__author__ = 'Minyi'
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==0 or numRows==1:
            return s
        ans = ''
        i = 0;
        n = len(s)
        while (i<n and i<numRows):
            index = i
            ans += s[index]
            j = 1
            while index < n:
                if (i==0 or i==numRows-1):
                    index += 2*numRows-2
                else:
                    if j%2!=0:
                        index += 2*(numRows-1-i)
                    else:
                        index += 2*i
                if index < n:
                    ans += s[index]

                j += 1
            i += 1
        return ans