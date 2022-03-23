import sys
import math

def get_centroid(volume):
    x, y, z = 0, 0, 0
    count = 0
    for face in volume:
        for vertex in face:
            count += 1
            x += vertex[0]
            y += vertex[1]
            z += vertex[2]
    return [x/count, y/count, z/count]

def cross(a, b, c):
    ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
    ac = [c[0] - a[0], c[1] - a[1], c[2] - a[2]]
    return [ab[1]*ac[2] - ab[2]*ac[1],
         ab[2]*ac[0] - ab[0]*ac[2],
         ab[0]*ac[1] - ab[1]*ac[0]]

def dot(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

def get_magnitude(n):
    return math.sqrt(sum([x**2 for x in n]))

def get_norm(face):
    n = cross(face[0], face[1], face[2])
    mag = get_magnitude(n)
    for i in range(len(n)):
        n[i] /= mag
    return n

def get_distance(face, point):
    v = [point[i] - face[0][i] for i in range(len(point))]
    return abs(dot(v, get_norm(face)))

def triangle_area(a, b, c):
    return get_magnitude(cross(a, b, c))/2

def get_area(vertices):
    root = vertices[0]
    area = 0
    for i in range(1, len(vertices)-1):
        area += triangle_area(root, vertices[i], vertices[i+1])
    return area

def get_face_volume(face, point):
    face_area = get_area(face)
    height = get_distance(face, point)
    return (face_area * height)/3


if __name__ == '__main__':
    # Read in data
    total_volume = 0
    num_volumes = int(sys.stdin.readline())
    for volume in range(num_volumes):
        new_volume = []
        num_faces = int(sys.stdin.readline())
        for face in range(num_faces):
            new_face = []
            data = list(map(float, sys.stdin.readline().split(' ')))
            for i in range(1, len(data), 3):
                new_face.append(data[i:i+3])
            new_volume.append(new_face)

        centroid = get_centroid(new_volume)
        for face in new_volume:
            total_volume += get_face_volume(face, centroid)
    print('{val:.2f}'.format(val = total_volume))
    
