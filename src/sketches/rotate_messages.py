#!/usr/bin/python
from collections import deque


def main():
    print("hello")
    messages = ["1st message", "2nd message", "hoooray, im third!", "i guess im last...?"]
    indexes = deque(list(range(len(messages))))
    print(indexes)
    indexes.rotate(-1)
    print(indexes)
    print(messages[indexes[0]])
    print(messages[indexes[1]])
    indexes.rotate(1)
    print(indexes)
    print(messages[indexes[0]])
    print(messages[indexes[1]])


if __name__ == '__main__':
    main()
