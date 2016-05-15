# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [[] for _ in range(numCourses)]
        outdegree = [0] * numCourses
        for sample in prerequisites:
            outdegree[sample[0]] += 1
            indegree[sample[1]].append(sample[0])

        s = []
        for i in range(numCourses):
            if outdegree[i] == 0:
                s.append(i)

        res = []
        while s:
            x = s.pop(0)
            res.append(x)
            for i in indegree[x]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    s.append(i)
        if len(res) != numCourses:
            return []
        else:
            return res
