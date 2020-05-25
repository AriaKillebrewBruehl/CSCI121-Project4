#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:41:02 2019

@author: ariakillebrew
"""

def invertKey(s):
    
    invert = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for ch in alpha:
        
        i = s.find(ch)
        invert += alpha[i]
        
    return invert 
        
        
   