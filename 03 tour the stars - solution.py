# Sample solution for Coding Quest 2022 day 3
# Paul Baumgarten 2022
# codingquest.io

import random, math

# Reading and parsing data
import requests
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=3")
points = [[int(n) for n in line.split()] for line in response.text.splitlines()] # 2d array of integers

print("Generating starmap")
distance = 0
for i in range(1, len(points)):
    p0 = points[i-1]
    p1 = points[i]
    # Find difference between the points
    dx = p0[0] - p1[0]
    dy = p0[1] - p1[1]
    dz = p0[2] - p1[2]
    # A little pythagoras...
    hf = math.sqrt(math.pow(dx,2)+math.pow(dy,2)+math.pow(dz,2))
    hi = int(hf)
    print(p0,p1,hf,hi,dx)
    distance += hi
print(distance)
