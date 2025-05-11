from collections import deque
import sys

def push_front(d, x):
    d.appendleft(x)

def push_back(d, x):
    d.append(x)

def pop_front(d):
    if d:
        print(d.popleft())
    else:
        print(-1)

def pop_back(d):
    if d:
        print(d.pop())
    else:
        print(-1)

def size(d):
    print(len(d))

def empty(d):
    if d:
        print(0)
    else:
        print(1)

def front(d):
    if d:
        print(d[0])
    else:
        print(-1)

def back(d):
    if d:
        print(d[-1])
    else:
        print(-1)

d = deque()
N = int(input())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        push_front(d, int(command[1]))
    elif command[0] == 'push_back':
        push_back(d, int(command[1]))
    elif command[0] == 'pop_front':
        pop_front(d)
    elif command[0] == 'pop_back':
        pop_back(d)
    elif command[0] == 'size':
        size(d)
    elif command[0] == 'empty':
        empty(d)
    elif command[0] == 'front':
        front(d)
    elif command[0] == 'back':
        back(d)

    