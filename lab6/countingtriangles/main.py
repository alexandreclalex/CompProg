import sys

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
        return None
    
    # Calculate intersection points
    x = ((l1[0]*l1[3] - l1[1]*l1[2])*(l2[0] - l2[2]) - (l1[0] - l1[2])*(l2[0]*l2[3] - l2[1]*l2[2])) / D
    y = ((l1[0]*l1[3] - l1[1]*l1[2])*(l2[1] - l2[3]) - (l1[1] - l1[3])*(l2[0]*l2[3] - l2[1]*l2[2])) / D
    
    # Verify intersection is in the segment
    if in_bounds(x, l1[0], l1[2]) and in_bounds(x, l2[0], l2[2]) and in_bounds(y, l1[1], l1[3]) and in_bounds(y, l2[1], l2[3]):
        return (x, y)



if __name__ == '__main__':
    # Read in number of lines
    num_lines = int(sys.stdin.readline()[:-1])

    while num_lines > 0:
        lines = []
        
        #Iterate through the lines in the test case, and read them in
        for i in range(num_lines):
            lines.append(list(map(float, sys.stdin.readline()[:-1].split(' '))))
        count = 0
        
        #In order to make a triangle, we need 3 lines to intersect with each other
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                
                #If the first lines dont intersect, we can short-circuit, and dont need to check any other lines, as they will not form a triangle
                if intersection(lines[i], lines[j]) is not None:
                    for k in range(j+1, len(lines)):
                        
                        # Check that the other 2 lines intersect, to form a triangle
                        if intersection(lines[j], lines[k]) is not None and intersection(lines[i], lines[k]) is not None:
                            count += 1
                        
        print(count)
                    
        # Read in next test case
        num_lines = int(sys.stdin.readline()[:-1])
