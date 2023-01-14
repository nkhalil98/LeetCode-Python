"""
1779. Find Nearest Point That Has the Same X or Y Coordinate

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Constraints:

1 <= points.length <= 10^4
points[i].length == 2
1 <= x, y, a_i, b_i <= 10^4
"""

def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        min_dist = 20001
        min_point = [0,0]
        for point in points:
            if point[0]==x or point[1]==y:
                if distance([x, y], point) < min_dist:
                    min_dist = distance([x,y], point)
                    min_point = point
        if min_dist == 20001:
            return -1
        return points.index(min_point)

if __name__ == "__main__":
    # test cases
    assert nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]) == 2
    assert nearestValidPoint(3, 4, [[3,4]]) == 0
    assert nearestValidPoint(3, 4, [[2,3]]) == -1