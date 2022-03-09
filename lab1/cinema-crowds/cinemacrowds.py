firstline = input()
capacity, groups = map(int, firstline.split(' '))
secondline = input()
for groupsize in map(int, secondline.split(' ')):
    if groupsize <= capacity:
        capacity -= groupsize;
        groups -= 1
print(groups)
