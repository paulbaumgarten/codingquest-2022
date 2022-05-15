# Sample solution for Coding Quest 2022 day 2
# Paul Baumgarten 2022
# codingquest.io

# Read and parse data
import requests
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=2")
data = [[int(n) for n in line.split()] for line in response.text.splitlines()] # 2d array of integers

winning_numbers = [12, 48, 30, 95, 15, 55, 97]
prize = 0
for i in range(len(data)):
    this = data[i]
    # Count the number of numbers in the winning set
    contained = 0
    for n in this:
        if n in winning_numbers:
            contained += 1
    if contained == 3: prize += 1
    if contained == 4: prize += 10
    if contained == 5: prize += 100
    if contained == 6: prize += 1000
    if contained == 7: prize += 10000
    if contained >= 3: print(contained, this)
print("solution",prize)

