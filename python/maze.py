#!/usr/local/bin/python3


def move(maze):
    steps=0
    jump=0
    pos = 0
    while pos < len(maze):
        jump = maze[pos]
        maze[pos]+=1
        pos += jump
        steps += 1
        #print(maze)
    return steps

maze = [0,3,0,1,-3]
assert 5 == move(maze)

mazein = [ int(line) for line in open("maze.in")]
print(move(mazein))
    
