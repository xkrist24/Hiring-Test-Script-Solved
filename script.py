#!/usr/bin/env python3

# Kristek Lukáš
# Hiring-Test-Script-Solved
# 7.3.2023

import sys
import re


def f1(file_name="D327971_fc1.i"):

    find_float = re.compile(r'X(.*?)Y(.*?)(?:T|$)(.*|$)')

    instructions = []
    block = 0

    with open('cnc.txt', 'w') as output:
        with open(file_name, "r") as file:

            # reading file line by line
            for line in file:

                # try finding instuction using regex
                values = find_float.search(line)

                # line with instruction
                if values:
                    # new block (Txx)
                    if values.group(3):
                        block = int(values.group(3))
                        while len(instructions) < block:
                            instructions.append([])

                    # check if found value is inside instuction block (in this case skips lines 4-7)
                    if block != 0:
                        instructions[block-1].append([float(values.group(1)), float(values.group(
                            2)) if float(values.group(2)) <= 10 else float(values.group(2)) + 10])
                    else:
                        output.write(line)

                # no instructin on line
                else:
                    # at end of instuction block print all instuctions
                    if block != 0:
                        for i, block in enumerate(instructions):
                            output.write(f"X{block[0][0]:.3f}Y{block[0][1]:.3f}T{i+1:02d}\r\n")
                            for instruction in block[1:]:
                                output.write(f"X{instruction[0]:.3f}Y{instruction[1]:.3f}\r\n")
                        block = 0
                    # no instuction => print line to output
                    output.write(line)

            # print(instructions)


def f2(file_name="D327971_fc1.i"):

    find_float = re.compile(r'X(.*?)Y(.*?)(?:T|$)(.*|$)')
    arr = []

    with open(file_name, "r") as file:
        for line in file:

            values = find_float.search(line)

            # no value found and in list are values = end of instructions
            if not values and arr:
                print(f"Min_X = {min(x[0] for x in arr)}\nMax_X = {max(x[0] for x in arr)}\n" +
                      f"Min_Y = {min(y[1] for y in arr)}\nMax_Y = {max(y[1] for y in arr)}")
                exit()

            if values:
                # pass until beggining of first instuction block
                if not values.group(3) and not arr:
                    pass
                # insert values into list
                else:
                    arr.append([float(values.group(1)), float(values.group(2))])


if __name__ == "__main__":
    if sys.argv[len(sys.argv)-1] == "-funkce1":
        f1()
    elif sys.argv[len(sys.argv)-1] == "-funkce2":
        f2()
    else:
        print("expected argument [-funkce1 | -funkce2] (" + (
            f"got: {sys.argv[len(sys.argv)-1]})" if len(sys.argv) > 1 else "no argument given)"))
