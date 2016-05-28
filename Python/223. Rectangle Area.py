# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Assume that the total area is never beyond the maximum possible value of int.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E >= C or A >= G or B >= H or F >= D:
            return (C - A) * (D - B) + (G - E) * (H - F)
        elif E < A and G > C and F < B and H > D:
            return (G - E) * (H - F)
        elif E > A and G < C and F > B and H < D:
            return (C - A) * (D - B)
        else:
            width = min(C, G) - max(A, E)
            height = min(H, D) - max(B, F)
            return (C - A) * (D - B) + (G - E) * (H - F) - width * height
