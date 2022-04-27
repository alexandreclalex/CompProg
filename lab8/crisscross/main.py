import sys
from math import sqrt
from fractions import Fraction

minimum, maximum = -1000000, 1000000

y_axis = [0, minimum, 0, maximum]
x_axis = [minimum, 0, maximum, 0]

def in_bounds(v, b1, b2):
    '''Find whether v is between b1 and b2'''
    if b1 > b2:
        b1, b2 = b2, b1
    return v >= b1 and v <= b2
    

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersection(l1, l2):
    '''Find the point of intersection of 2 lines, given 2 line segments of the form [x1, y1, x2, y2], return None otherwise'''
    # Find determinant
    D = (l1[0] - l1[2])*(l2[1] - l2[3]) - (l1[1] - l1[3])*(l2[0] - l2[2])
    if D == 0:
        return None, False
    
    
    # Calculate intersection points
    x = Fraction(((l1[0]*l1[3] - l1[1]*l1[2])*(l2[0] - l2[2]) - (l1[0] - l1[2])*(l2[0]*l2[3] - l2[1]*l2[2])), D)
    y = Fraction(((l1[0]*l1[3] - l1[1]*l1[2])*(l2[1] - l2[3]) - (l1[1] - l1[3])*(l2[0]*l2[3] - l2[1]*l2[2])), D)
    
    # Verify intersection is in the segment
    within_bounds = in_bounds(x, l1[0], l1[2]) and in_bounds(x, l2[0], l2[2]) and in_bounds(y, l1[1], l1[3]) and in_bounds(y, l2[1], l2[3])
    return (x, y), within_bounds

def coincident(l1, l2):
    '''Find if 2 parallel lines are coincident'''
    # if lines are vertical, check x intercept, otherwise y intercept
    axis = y_axis
    if(l1[0] == l1[2]):
        axis = x_axis
        
    # Calculate axis intercepts
    int_1, _ = intersection(l1, axis)
    int_2, _ = intersection(l2, axis) 
    
    # If intercepts are the same, the lines are coincident
    return int_1 == int_2

def dist(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return sqrt(dx*dx + dy*dy)
    
def is_joint_coincident(l1, l2):
    '''Check if 2 coincident lines are only touching at one point, or no points, None if there are inf points'''
    # Create list of all points
    points = [(l1[0], l1[1]),
            (l1[2], l1[3]),
            (l2[0], l2[1]),
            (l2[2], l2[3])]
    
    # Find the max distance between 2 points, and the sum of the line segments
    sum_of_seg = dist(l1[0:2], l2[2:4]) + dist(l1[0:2], l2[2:4])
    max_dist = 0
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d > max_dist:
                max_dist = d
    
    # There must be an overlap
    if sum_of_seg > max_dist:
        return None

    # 1 if joint, 0 otherwise
    return 1 if max_dist == sum_of_seg else 0

if __name__ == '__main__':
    # Read in number of lines
    num_lines = int(sys.stdin.readline()[:-1])

    lines = []
    
    # Iterate through the lines in the test case, and read them in
    for i in range(num_lines):
        lines.append(tuple(map(int, sys.stdin.readline().split())))

    points = set()
    
    # Iterate through pairs of lines
    for i in range(num_lines - 1):
        for j in range(i+1, num_lines):
            # Find intersection
            isect, valid = intersection(lines[i], lines[j])
            
            # Lines are parallel, need to check coincidence
            if isect is None:
                if coincident(lines[i], lines[j]):
                    ijc = is_joint_coincident(lines[i], lines[j])
                    if ijc == None:
                        print(-1)
                        exit(0)
                    if ijc == 1:
                        points.add(isect)
                        
            # Lines actually intersect
            elif valid:
                points.add(isect)
                
    
    print(len(points))