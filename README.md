# cat-and-mouse
Red Team Tool that disconnects the mouse on a Debian 10.1.x.x Linux system

<h2>What it Does</h2>
mouse.py will install xlist and use it to disable the mouse drivers, then open a new terminal with ASCII art of a cat. The goal is to disrupt blue team actions until they can bring back mouse functionality.

<h2>How to Use</h2>
Currently, mouse.py needs to be on the machine and would need to be run using the command line. 

mouse.py can be installed anywhere on the machine, and will need to be run in the directory the file is installed using the command "python3 ./mouse.py"

<h5>Dependencies</h5>
<b>xinput</b> - xinput will need to be installed on the machine, otherwise it will not be able to disable the mouse. The script will attempt to install it using "root" as the default sudo password.
<b>X11</b> - xinput works best with X11, and likely will not work as expected if the system is using Wayland. 

<h2>Known Issues</h2>
<li>
  <ul>Currently does not have the terminal containing the ASCII cat stay up.</ul>
</li>
