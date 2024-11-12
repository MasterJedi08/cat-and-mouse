# cat-and-mouse
Red Team Tool that disconnects the mouse on a Debian Linux system

<h2>What it Does</h2>
mouse.py will install xlist and use it to disable the mouse drivers, then display ASCII art of a cat on the terminal. The goal is to disrupt blue team actions until they can bring back mouse functionality.

<h2>How to Use</h2>
mouse.py can be installed anywhere on the machine, and will need to be run in the directory the file is installed using the command "python3 ./mouse.py" When testing the script, uncomment the last section labeled "testing purposes only" as it will enable the mouse again after 10 seconds. 

fix-it.py should only be used to re-enable the devices and undoes the work of mouse.py. It should NOT be downloaded to the machine unless necessary.

<h5>Dependencies</h5>
<b>xinput</b> - xinput will need to be installed on the machine, otherwise it will not be able to disable the mouse. The script will attempt to install it using "root" as the default sudo password.
<b>X11</b> - xinput works only with X11, and likely will not work as expected if the system is using Wayland. 

<h2>Known Issues</h2>
<li>
  <ul>Will only display ASCII art if a terminal is already open</ul>
</li>
