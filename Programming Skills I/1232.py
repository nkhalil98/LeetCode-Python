"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

def checkStraightLine(coordinates: list[list[int]]) -> bool:
        x0 = coordinates[0][0]
        x1 = coordinates[1][0]

        if x0 == x1:
            for i in coordinates:
                if i[0] != x0:
                    return False
            return True

        y0 = coordinates[0][1]
        y1 = coordinates[1][1]

        slope = (y1-y0)/(x1-x0)

        def myline(x):
            return slope*(x-x0)+y0

        for i in coordinates:
            if myline(i[0]) != i[1]:
                return False
        return True

if __name__ == "__main__":
    # test cases
    assert checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True
    assert checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False  