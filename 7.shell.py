import os
import sys
import subprocess
import shutil

print("Shell command ready: ")
while 1:
    cmd = input("Enter your command: ")
    if cmd == "exit":
        break
    try:
        exec(cmd)
print("Goodbye")

"""myCmd = os.popen('ls -la').read()
print(myCmd)
MyOut = subprocess.Popen["ls", "-l", "."]
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
stdout,stderr = MyOut.communicate()
print(stdout)
print(stderr) """
