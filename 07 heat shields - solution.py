# Sample solution for Coding Quest 2022 day 7
# Paul Baumgarten 2022
# codingquest.io

import time
import requests
import numpy

# Download and parse data
print("Downloading file")
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=7")
content = response.text.splitlines()
data = [[int(n) for n in line.split()] for line in content]

# Method 1 - Full coordinate space - 2 billion integers!!!!
# What most students will likely attempt
def brute_force(w,h,data):
    # Record start time
    t0 = time.time()
    # Create heat shield coordinate space
    print("Allocating memory")
    shield = [[0]*w for m in range(h)]

    # Map each tile onto the coordinate space
    print(len(shield), 'x', len(shield[0]))
    print("Placing tiles")
    for i in range(len(data)):
        t = data[i]
        print(i,t)
        for row in range(t[1], t[1] +t[3]):
            for col in range(t[0], t[0] + t[2]):
                shield[row][col] = 1

    # How many zeros are left?
    print("Counting gaps")
    filled = 0
    for row in shield:
        filled = filled + sum(row)
    spaces = (w*h - filled)
    print(f"Time taken: { time.time() - t0 }")
    return(spaces)

# Method 2 - Reduce coordinate space by data inspection
# Inspect the data and realise it consists of multiples of 10, reduce the problem dimensions accordingly
def brute_force_factored(w,h,data,factor):
    # Record start time
    t0 = time.time()
    # Create heat shield coordinate space
    print("Allocating memory")
    shield = [[1]*(w//factor) for m in range(h//factor)]

    # Map each tile onto the coordinate space
    print(len(shield), 'x', len(shield[0]))
    print("Placing tiles")
    for i in range(len(data)):
        t = data[i]
        # print(i,t)
        for row in range(t[1] // factor, t[1] // factor +t[3] // factor):
            for col in range(t[0] // factor, t[0] // factor + t[2] // factor):
                shield[row][col] = 0

    # How many zeros are left?
    print("Counting gaps")
    filled = 0
    for row in shield:
        filled = filled + sum(row)
    spaces = filled * factor * factor
    print(f"Time taken: { time.time() - t0 }")
    return(spaces)

# Method 3 - Full coordinate space but use numpy
# Demonstrates the power of using the right tool for the job!
def brute_force_numpy(w,h,data):
    # Record start time
    t0 = time.time()
    # Create coordinate space
    print("Allocating memory")
    shield = numpy.ones((h,w), dtype=numpy.int32) # Set entire coordinate space to 1s (uncovered) by default
    print(shield.shape)

    # Map each tile onto the coordinate space
    print("Placing tiles")
    for i in range(len(data)):
        t = data[i]
        # print(i,t)
        shield[ t[1]:t[1]+t[3], t[0]:t[0]+t[2] ] = 0
    # How many zeros are there?
    print("Counting gaps")
    spaces = shield.sum()
    print(f"Time taken: { time.time() - t0 }")
    return(spaces)

result = brute_force(20000, 100000, data) # 4:19 on Mac M1
print(result)

result = brute_force_factored(20000, 100000, data, factor=10) # 2.4s on Mac M1
print(result)

result = brute_force_numpy(20000, 100000, data) # 3.7s on Mac M1
print(result)

"""

For anyone interested in an approach better than brute forcing all coordinates in the space, look into line sweeeping algorithms. A couple of suggested starting points for this:

LINE SWEEP ALGORITHMS
https://www.topcoder.com/thrive/articles/Line%20Sweep%20Algorithms

Rectangle Area II | Geometry | Maths | Line Sweep | 850 LeetCode | Day 22
https://www.youtube.com/watch?v=TIojOkG1E4U

"""
