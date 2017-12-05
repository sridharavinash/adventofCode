#!/usr/local/bin/python3


def move(maze,offset_rule=False):
    steps=0
    jump=0
    pos = 0
    while pos < len(maze):
        jump = maze[pos]
        if offset_rule:
            if jump >= 3:
                maze[pos]-=1
            else:
                maze[pos]+=1
        else:
            maze[pos]+=1
        pos += jump
        steps += 1
        #print(maze)
    #print(steps)
    return steps

maze = [0,3,0,1,-3]
assert 5 == move(maze)

mazein = [ int(line) for line in open("maze.in")]
print(move(mazein))

#part 2
maze = [0,3,0,1,-3]    
assert 10 == move(maze,True)
mazein = [ int(line) for line in open("maze.in")]
print(move(mazein,True))
