# -*- coding: utf-8 -*-
"""
python file that contains a collection of reusable functions

    Author: P077448 - Nick Lopez
    Creation Date : 20190131
    Last Updated Date : 20190131
    Release 0.1
    
    Release 0.1 Notes:
        * Initial creation
        * Generic Utilities : reusable functions    
"""


def printbanner(bannertext="", filler="-", size=80, padtop=0, padbot=0):
    
    if padtop:
        print()
    
    print(filler*size)
    
    if bannertext:
        banlpad = int((size - int(len(bannertext))-1) / 2)
        banrpad = int((size - int(len(bannertext))-2) / 2)
        print((filler*banlpad)+" " + bannertext + " "+(filler*banrpad))
    else:
        print(filler*size)
    
    print(filler*size)
    
    if padbot:
        print()
        