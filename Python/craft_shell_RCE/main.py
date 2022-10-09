#!/usr/bin/python3

import sys

def craft(command):
    space = "__=$'\\111\\106\\123'&&" # IFS
    obfuscated = ""

    if b' ' in command:
        obfuscated += space
    
    for i in range(len(command)):
        if command[i] == ord(' '):
            obfuscated += "${!__}"
            
        elif command[i] in b'|;#abcdefghijklmnopqrstuvwxyz':
            obfuscated += f"$'\{command[i]:o}'"
        else:
            obfuscated += f"{command[i]:c}"
    # obfuscated += "'"
    return obfuscated

print(craft(sys.argv[1].encode()))
