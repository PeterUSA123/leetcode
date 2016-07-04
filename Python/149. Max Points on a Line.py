# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length < 3:
            return length
        ans = -1
        for i in range(length):
            dic = {'inf':0}
            samePointNums = 1
            for j in range(length):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    dic['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k not in dic:
                        dic[k] = 1
                    else:
                        dic[k] += 1
                else:
                    samePointNums += 1
            ans = max(ans,max(dic.values()) + samePointNums)
        return ans