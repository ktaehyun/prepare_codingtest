import sys
import math

input = sys.stdin.readline

def round(n):
    return int((n*10 + 5)/10)

def ccw(p1, p2, p3):
    return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def monotonechain(dots):
    dots.sort()
    if len(dots) <=1:
        return dots

    lower = []
    for d in dots:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], d) <= 0:
            lower.pop()
        lower.append(d)

    upper = []
    for d in reversed(dots):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], d) <= 0:
            upper.pop()
        upper.append(d)
    return lower[:-1] + upper[:-1]

def getDist(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n,l = map(int, input().split())
buildings = [[int(i) for i in input().split()] for _ in range(n)]
convexHull = monotonechain(buildings)
s = 0
for i in range(len(convexHull)):
    s += getDist(convexHull[i-1], convexHull[i])
s += 2*math.pi*l
print(round(s))