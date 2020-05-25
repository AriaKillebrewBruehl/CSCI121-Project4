# -*- coding: utf-8 -*-

from pgl import GWindow, GCompound, GRect, GLabel
from EnigmaConstants import *


class EnigmaRotor(GCompound):
    def __init__(self, letter, perm, inverse):
        GCompound.__init__(self)
        
        rotor = GRect(ROTOR_WIDTH, ROTOR_HEIGHT)
        rotor.setColor(ROTOR_BGCOLOR)
        rotor.setFilled(True)
        self.add(rotor, -ROTOR_WIDTH/2, -ROTOR_HEIGHT/2) # create design for rotors
        
        self.ch = GLabel(letter)
        self.ch.setColor(ROTOR_COLOR)
        self.ch.setFont(ROTOR_FONT)
        self.add(self.ch, -self.ch.getWidth()/2, ROTOR_LABEL_DY)
        
        self.perm = perm
        self.inverse = inverse
        self.offset = 0
        self.rotor = rotor 
        
       
    
    
    def clickAction(self, enigma): # advance on click action of rotors
    
        self.advance()     
        
    def advance(self): # define advance 
        
        self.offset += 1 
        
        if self.offset == 26:
            self.offset = 0
            r =  True # tells that the rotor should carry 
        else: 
            r =  False # tells that the rotor should not carry 
        self.ch.setLabel(ALPHABET[self.offset])
            
        return r 
        
        
        
        
        
        
        