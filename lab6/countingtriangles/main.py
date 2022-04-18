import sys

def in_bounds(v, b1, b2):
    if b1 > b2:
        b1, b2 = b2, b1
    return v >= b1 and v <= b2
    

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersection(l1, l2):
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
    num_lines = int(sys.stdin.readline()[:-1])

    while num_lines > 0:
        lines = []
        for i in range(num_lines):
            lines.append(list(map(float, sys.stdin.readline()[:-1].split(' '))))
        count = 0
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                ij = intersection(lines[i], lines[j])
                if ij is not None:
                    for k in range(j+1, len(lines)):
                        jk = intersection(lines[j], lines[k])
                        ik = intersection(lines[i], lines[k])
                        if jk is not None and ik is not None and ij != jk and ij != ik and ik != jk:
                            count += 1
                        
        print(count)
                    
        num_lines = int(sys.stdin.readline()[:-1])
