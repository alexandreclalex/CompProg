import sys

labels = ['too low', 'right on', 'too high']
minimum = -1
maximum = 11
line = sys.stdin.readline().replace("\n", '')
while line != '0':
    guess = int(line)
    label = sys.stdin.readline().replace("\n", '')
    if label == labels[0]:
        if guess > minimum:
            minimum = guess
    elif label == labels[2]:
        if guess < maximum:
            maximum = guess
    elif label == labels[1]:
        if guess < maximum and guess > minimum:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        minimum = -1
        maximum = 11
    line = sys.stdin.readline().replace("\n", '')