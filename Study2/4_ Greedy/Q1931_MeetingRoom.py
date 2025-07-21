import sys
input = sys.stdin.readline

def count_meeting(meeting_times):

    meeting_times.sort(key=lambda x:(x[1], x[0]))
    
    count = 1
    last_end_time = meeting_times[0][1]
    
    for i in range(1, len(meeting_times)):
        if meeting_times[i][0] >= last_end_time:
            count += 1
            last_end_time = meeting_times[i][1]
            
    print(count)


def solve():
    n = int(input())
    meeting_times= []
    for i in range(n): 
        meeting_times.append(list(map(int, input().split())))
    count_meeting(meeting_times)
    
solve()