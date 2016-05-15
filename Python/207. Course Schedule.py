# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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

        cnt = 0
        while s:
            x = s.pop(0)
            cnt += 1
            for i in indegree[x]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    s.append(i)
        return cnt == numCourses
