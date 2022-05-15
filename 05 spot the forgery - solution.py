# Sample solution for Coding Quest 2022 day 5
# Paul Baumgarten 2022
# codingquest.io

import hashlib, time
import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=5")
data = response.text.splitlines()
blocks = [line.split("|") for line in data]

# Find the forgery
for i in range(len(blocks)):
    data = blocks[i][0] + "|" + blocks[i][1] + "|" + blocks[i][2]
    original_hash = blocks[i][3]
    calculated_hash = hashlib.sha256(data.encode("utf-8")).hexdigest()
    if original_hash != calculated_hash:
        print("original:        ",original_hash)
        print("calculatted:     ",calculated_hash)
        print("Fraudulant item: ",blocks[i][0])
        break

# Calculate the corrected blockchain
t = time.time()
for j in range(i, len(blocks)):
    mined = False
    nonce=0
    blocks[j][2] = blocks[j-1][3] # Copy across the previous hash
    print("Calculating hash for ",blocks[j][0]+"|"+str(nonce)+"|"+blocks[j][2])
    while not mined:
        message = blocks[j][0]+"|"+str(nonce)+"|"+blocks[j][2]
        h = hashlib.sha256(message.encode("utf-8")).hexdigest()
        if h.startswith("000000"): 
            mined=True
        else:
            nonce += 1
    prev = h
    blocks[j][3] = h
    print(message+"|"+h,"  ",(round(time.time()-t)))
print("done")
print(time.time()-t)

# Print the resulting blockchain
for i in blocks:
    print(i)
