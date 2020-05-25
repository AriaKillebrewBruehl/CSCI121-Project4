# -*- coding: utf-8 -*-

from pgl import GWindow, GCompound, GOval, GLabel
from EnigmaConstants import *

class EnigmaLamp(GCompound):
    def __init__(self, letter):
        GCompound.__init__(self)
        
        lamp = GOval(LAMP_RADIUS*2, LAMP_RADIUS*2)
        lamp.setColor(LAMP_BORDER_COLOR)
        lamp.setFillColor(LAMP_BGCOLOR)
        self.add(lamp, -LAMP_RADIUS, -LAMP_RADIUS) # create design for lamps
        
        self.ch = GLabel(letter)
        self.ch.setColor(LAMP_OFF_COLOR)
        self.ch.setFont(LAMP_FONT)
        self.add(self.ch, -self.ch.getWidth()/2, LAMP_LABEL_DY)
        
    def setState(self, state): # set state of lamp to be on or off
        if state:
            self.ch.setColor(LAMP_ON_COLOR)
        else:
            self.ch.setColor(LAMP_OFF_COLOR)
    
    def getState(self): # get state of lamp )(n or off)
        if self.ch.getColor() == LAMP_ON_COLOR:
            return True
        else: 
            return False 
            
    