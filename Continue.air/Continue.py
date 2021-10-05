# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('constants.air')
using('utils.air');

from constants import CONTINUE_ATTACK,STONE,COPPER_APPLE,SILVER_APPLE,GOLD_APPLE;
from utils import handleSimpleClick,waitAction;

auto_setup(__file__)

class Continue:
    def __init__(self, isEatApple = False, eatCount = 1):
        self.isEatApple = isEatApple;
        self.eatCount = eatCount;
        
        
    def again(self):
        coordinates = exists(CONTINUE_ATTACK)
        
        if coordinates :
            handleSimpleClick(coordinates,2);
            self.eatApple();
            
        
    def eatApple(self):
        if self.isEatApple == False:pass;
        if exists(STONE):
#             swipe(STONE, vector=[0, -1])
#             sleep(2)
            handleSimpleClick(GOLD_APPLE)
            confirm = waitAction(Template(r"tpl1615556577657.png", record_pos=(
                0.156, 0.155), resolution=(1280, 720)))
            handleSimpleClick(confirm)
        pass;
    
    
if __name__ == '__main__':
    Continue().eatApple();
    
        


