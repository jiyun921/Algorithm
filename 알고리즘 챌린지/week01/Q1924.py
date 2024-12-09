x,y = map(int,input().split())

day = [31,28,31,30,31,30,31,31,30,31,30,31]
L = ['MON','TUE','WED','THU','FRI','SAT','SUN']

print(L[(sum(day[:x-1])+y-1)%7])