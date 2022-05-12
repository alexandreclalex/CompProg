import sys
import math

stores = dict()
people = dict()


def get_distance(x1, y1, x2, y2):
    return int(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))


def find_closest_store(person):
    for y in stores:
        distance = get_distance(person[0], person[1], stores[y][0], stores[y][1])
        if person[2] > distance:
            person[2] = distance
            person[3] = y


def get_total_distance():
    return "TODO"


def execute():
    rows, cols = sys.stdin.readline().strip("\n").split(" ")
    num_stores = int(sys.stdin.readline())
    for x in range(num_stores):
        store = sys.stdin.readline().strip("\n").split(" ")
        stores[int(store[0])] = [int(store[1]), int(store[2]), int(store[3])]
    num_people = int(sys.stdin.readline())
    for x in range(num_people):
        person = sys.stdin.readline().strip("\n").split(" ")
        people[x] = [int(person[0]), int(person[1]), sys.maxsize, -1]
    for x in people:
        person = people[x]
        find_closest_store(person)
    print(get_total_distance())


if __name__ == "__main__":
    execute()
