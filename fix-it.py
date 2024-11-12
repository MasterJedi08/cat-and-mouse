#!/usr/bin/env python3
# imports
import subprocess as sp
import os

# getting mouse devices
output = sp.run("xinput list", capture_output=True, text=True, shell=True)
#print("output: ", output)
cleaned = output.stdout.split("\n")
#print("cleaned: ", cleaned)

# get the id of the mouse devices
ids = []
for line in cleaned:
    # split lines to search in for loop
    tokens = line.split()
    # find id
    for token in tokens:
        print(token)
        if token.startswith("id="):
            # get the id value from 'id=<number>'
            ids.append(token.split('=')[1])  

print("ids found: ", ids)

# disable ALL of the ids, since you dont know what the actual one is
for id in ids:
    try:
        os.system(f"xinput enable {id}")
        print(f"enabled {id}")
    except Exception as e:
        print(f"error occured during enabling id {id}: {e}")

