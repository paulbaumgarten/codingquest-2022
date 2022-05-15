# Sample solution for Coding Quest 2022 day 6
# Paul Baumgarten 2022
# codingquest.io

# Debug an op code machine

import requests

# Get problem data
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=6")
instr = response.text.replace("\n\n","\n").splitlines()

# Create memory locations for the interpreter
registers = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0 }
pc = 0              # Program counter register
lastCompare = False # Result of last CEQ or CGE comparison

# Execute the program
while instr[pc] != "END":
    cir = instr[pc].split(" ") # Current instruction register
    print(pc, cir, lastCompare, registers) # - Debugging print
    pc += 1                    # Increment program counter

    if cir[0] == "ADD":
        target = cir[1]
        if cir[2].isalpha():
            source = cir[2]
            registers[target] += registers[source]
        else:
            registers[target] += int(cir[2])

    elif cir[0] == "MOD":
        target = cir[1]
        if cir[2].isalpha():
            source = cir[2]
            registers[target] %= registers[source]
        else:
            registers[target] %= int(cir[2])

    elif cir[0] == "DIV":
        target = cir[1]
        if cir[2].isalpha():
            source = cir[2]
            registers[target] //= registers[source]
        else:
            registers[target] //= int(cir[2])

    elif cir[0] == "MOV":
        target = cir[1]
        if cir[2].isalpha():
            source = cir[2]
            registers[target] = registers[source]
        else:
            registers[target] = int(cir[2])

    elif cir[0] == "JMP":
        pc += int(cir[1])-1

    elif cir[0] == "JIF":
        if lastCompare:
            pc += int(cir[1])-1

    elif cir[0] == "CEQ":
        lastCompare = False
        if cir[1].isalpha():
            source1 = registers[cir[1]]
        else:
            source1 = int(cir[1])
        if cir[2].isalpha():
            source2 = registers[cir[2]]
        else:
            source2 = int(cir[2])
        if source1 == source2:
            lastCompare = True

    elif cir[0] == "CGE":
        lastCompare = False
        if cir[1].isalpha():
            source1 = registers[cir[1]]
        else:
            source1 = int(cir[1])
        if cir[2].isalpha():
            source2 = registers[cir[2]]
        else:
            source2 = int(cir[2])
        if source1 >= source2:
            lastCompare = True

    elif cir[0] == "OUT":
        if cir[1].isalpha():
            source = cir[1]
            print( registers[ cir[1] ] )
        else:
            print( cir[1] )
