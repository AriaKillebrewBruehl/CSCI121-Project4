# -*- coding: utf-8 -*-
from pgl import GWindow, GCompound, GOval, GLabel
from EnigmaConstants import *

class EnigmaKey(GCompound):
    def __init__(self, letter):
        GCompound.__init__(self)
        
        key = GOval(KEY_RADIUS*2, KEY_RADIUS*2)
        key.setLineWidth(KEY_BORDER)
        key.setColor(KEY_BORDER_COLOR)
        key.setFillColor(KEY_BGCOLOR)
        self.add(key, -KEY_RADIUS, -KEY_RADIUS) # create design for keys 
        
        self.ch = GLabel(letter)
        self.ch.setColor(KEY_UP_COLOR)
        self.ch.setFont(KEY_FONT)
        
        self.add(self.ch, -self.ch.getWidth()/2, KEY_LABEL_DY)
        
    def setLetterColor(self, color): # change letter color if needed
        self.ch.setColor(color)
        
    def mousedownAction(self, enigma): # define mousedownAction
        self.setLetterColor(KEY_DOWN_COLOR)
        enigma.keyPressed(self)
        
    def mouseupAction(self, enigma): # define mouseupAction
        self.setLetterColor(KEY_UP_COLOR)
        enigma.keyReleased(self)
            
        
        
            
        

        