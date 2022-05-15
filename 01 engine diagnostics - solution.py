# Sample solution for Coding Quest 2022 day 1
# Paul Baumgarten 2022
# codingquest.io

"""
Note: To use a local file for input instead of downloading, use...

with open("01 engine diagnostics - input.txt", "r") as f:
    numbers = [int(n) for n in f.read().splitlines()]
"""

import requests
print("Downloading file")
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=1")
if response.status_code != 200:
    print("Error downloading data. Terminating.")
    exit()
numbers = [int(n) for n in response.text.splitlines()]

count = 0
total = sum(numbers[0:60])
for i in range(60, len(numbers)):
    total = total - numbers[i-60] + numbers[i]
    rolling_ave = total / 60
    if rolling_ave < 1500 or rolling_ave > 1600:
        count += 1
print(count)
