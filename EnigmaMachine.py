# File: EnigmaMachine.py

"""
This module is the starter file for the EnigmaMachine class.
"""

from pgl import GImage
from EnigmaConstants import *

# Class: EnigmaMachine

class EnigmaMachine():
    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.  If you need to maintain any state information
    that must be shared among different parts of this implementation,
    you should define that information as part of this class and
    provide the necessary getters, setters, and other methods needed
    to manage that information.
    """

    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        enigmaImage = GImage("images/EnigmaTopView.png")
        gw.add(enigmaImage)
        
        self.keys = []
        self.lamps = []
        self.rotors = []

    def keyPressed(self, key):
        
        if self.rotors[2].advance(): # advance rotors on key press, carry if needed
            if self.rotors[1].advance():
                self.rotors[0].advance()

        ch = key.ch.getLabel()
        
        for i in range(3): # go forward through rotors
            chindex = ALPHABET.index(ch)
            index = self.applyPermutation(chindex, self.rotors[2-i].perm, self.rotors[2-i].offset)
            ch = ALPHABET[index]
        
        chindex = ALPHABET.index(ch)
        ch = REFLECTOR_PERMUTATION[index] # go through reflectors
        
        for i in range(3): # go backwards through rotors
            chindex = ALPHABET.index(ch)
            index = self.applyPermutation(chindex, self.rotors[i].inverse, self.rotors[i].offset)
            ch = ALPHABET[index]
            
        for lamp in self.lamps: # set lamp state to true for correct lamp 
            if lamp.ch.getLabel() == ch:
                lamp.setState(True)
            
    def keyReleased(self, key):
        ch = key.ch.getLabel()
        
        for i in range(3):
            chindex = ALPHABET.index(ch)
            index = self.applyPermutation(chindex, self.rotors[2-i].perm, self.rotors[2-i].offset)
            ch = ALPHABET[index]
        
        chindex = ALPHABET.index(ch)
        ch = REFLECTOR_PERMUTATION[index]
        
        for i in range(3):
            chindex = ALPHABET.index(ch)
            index = self.applyPermutation(chindex, self.rotors[i].inverse, self.rotors[i].offset)
            ch = ALPHABET[index]
            
        for lamp in self.lamps:
            if lamp.ch.getLabel() == ch:
                lamp.setState(False)
    
    def applyPermutation(self, index, permutation, offset): # apply permuation to get correct index 
        index = (index + offset) % 26 
        ch = permutation[index]
        index = (ALPHABET.index(ch) - offset)%26 
        return index 
        
        