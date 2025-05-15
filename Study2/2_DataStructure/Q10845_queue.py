import sys

def push(queue, x):
    queue.append(x)

def pop(queue):
    if queue:
        print(queue.pop(0))
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    if queue:
        print(0)
    else:
        print(1)

def front(queue):
    if queue:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if queue:
        print(queue[-1])
    else:
        print(-1)

queue = []
N = int(input())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(queue, int(command[1]))
    elif command[0] == 'pop':
        pop(queue)
    elif command[0] == 'size':
        size(queue)
    elif command[0] == 'empty':
        empty(queue)
    elif command[0] == 'front':
        front(queue)
    elif command[0] == 'back':
        back(queue)

    