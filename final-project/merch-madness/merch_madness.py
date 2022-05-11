import sys


def execute():
    x, y = sys.stdin.readline().strip("\n").split(" ")
    print(f"{x} {y}")


if __name__ == "__main__":
    execute()