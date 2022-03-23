from main import *

vertices = [
    [0,0,0],
    [1,0,0],
    [1,1,0],
    [1.5, 1, 0],
    [0,1,0]
]

point = [0, 0, 2]

print(get_face_volume(vertices, point))