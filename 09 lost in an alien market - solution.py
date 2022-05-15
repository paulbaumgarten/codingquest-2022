# Sample solution for Coding Quest 2022 day 9
# Paul Baumgarten 2022
# codingquest.io

import time
import requests

print("Downloading file")
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=9")
maze = response.text.splitlines()
maze = [[c for c in line] for line in maze] # Convert to 2d array of characters

START = [0,199]     # Starting pixel coordinates
FINISH = [400,201]  # Finishing pixel coordinates

def solve(maze, y0, x0, distance=0): # Breath first search!
    paths = []
    paths.append((y0-1, x0, distance+1)) # up
    paths.append((y0+1, x0, distance+1)) # down
    paths.append((y0, x0-1, distance+1)) # left
    paths.append((y0, x0+1, distance+1)) # right
    while len(paths) > 0:
        y,x,distance = paths.pop()
        if y < 0 or x < 0 or y >= len(maze) or x >= len(maze[y]): # Can't go off boundary
            continue
        if maze[y][x] == "#": # Can't go into a wall
            continue
        if maze[y][x] == ".": # Can't return to previous place
            continue
        maze[y][x] = "." # Mark this square so we don't return to it
        if y==FINISH[0] and x==FINISH[1]: # Found the end point
            print("solved")
            return distance+1
        paths.append((y-1, x, distance+1)) # up
        paths.append((y+1, x, distance+1)) # down
        paths.append((y, x-1, distance+1)) # left
        paths.append((y, x+1, distance+1)) # right 

# Let's do this!
t = time.time()
print(solve(maze, START[0], START[1]))
print(time.time() - t)
