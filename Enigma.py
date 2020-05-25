# File: Enigma.py

"""
This module is the main program for the Enigma machine.  You should
not need to change this file unless you are implementing extensions.
"""

from pgl import GWindow, GCompound, GOval
from EnigmaMachine import EnigmaMachine
from EnigmaConstants import *
from EnigmaKey import * 
from EnigmaLamp import * 
from EnigmaRotor import * 
from InvertKey import * 

# Main program

def Enigma():
    rotor = [] # create blank list of rotors
    n = int(input("Enter the first rotor you'd like to use (0 - 4). (Enter 0 for default). "))
    rotor.append(ROTOR_PERMUTATIONS[n]) # add first rotor 
    n = int(input("Enter the second rotor you'd like to use (0 - 4). (Enter 1 for default). "))
    rotor.append(ROTOR_PERMUTATIONS[n]) # add second rotor 
    n = int(input("Enter the third rotor you'd like to use (0 - 4). (Enter 2 for default). "))
    rotor.append(ROTOR_PERMUTATIONS[n]) # add thrid rotor
    
    def mousedownAction(e):
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "mousedownAction", None) is not None:
                gobj.mousedownAction(enigma)

    def mouseupAction(e):
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "mouseupAction", None) is not None:
                gobj.mouseupAction(enigma)

    def clickAction(e):
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "clickAction", None) is not None:
                gobj.clickAction(enigma)
    
    def addKeys(enigma): # create keys
        for i in range(26):
            newKey = EnigmaKey(ALPHABET[i])
            x, y = KEY_LOCATIONS[i]
            enigma.keys.append(newKey)
            gw.add(newKey,x, y)
    def addLamps(enigma): # create lamps
        for i in range(26):
            newLamp = EnigmaLamp(ALPHABET[i])
            x, y = LAMP_LOCATIONS[i]
            enigma.lamps.append(newLamp)
            gw.add(newLamp,x, y)
    def addRotors(enigma): # create rotors
        for i in range(3):
            ROTOR_INVERSE = invertKey(rotor[i])
            newRotor = EnigmaRotor(ALPHABET[0], rotor[i], ROTOR_INVERSE)
            x, y = ROTOR_LOCATIONS[i]
            enigma.rotors.append(newRotor)
            gw.add(newRotor,x, y)

    gw = GWindow(ENIGMA_WIDTH, ENIGMA_HEIGHT)
    enigma = EnigmaMachine(gw)
    gw.addEventListener("mousedown", mousedownAction)
    gw.addEventListener("mouseup", mouseupAction)
    gw.addEventListener("click", clickAction)
    
    addKeys(enigma) # add keys 
    addLamps(enigma) # add lamps
    addRotors(enigma) # add rotors

# Startup code

if __name__ == "__main__":
    
    Enigma()
