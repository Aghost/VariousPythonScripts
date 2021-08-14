#!/usr/bin/env python3

def print_pyramid(nr):
    z = 0
    for x in range(int(nr), 0, -1):
        print(x * ' ', end = '')

        z += 1
        for y in range(1, z+1, 1):
            print(str(y), end = ' ')
        print()

answer = input("Enter Pyramid Size:")
#answer = (int)answer
print_pyramid(answer)
