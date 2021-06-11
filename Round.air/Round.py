# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('utils.air');
using('Hero.air');
using('constants.air');

from Hero import Hero
from utils import getX,waitAttackStart,handleSimpleClick

from constants import FIRST,SECOND,INSTRUCTION_X,INSTRUCTION_Y,INSTRUCTION_WIDTH,INSTRUCTION_SPACING,BEGIN_ATTACK;

auto_setup(__file__)

class Round:
    
    def __init__(self,ready = None):
        self.ready = ready;
    
        
    def attack(self):
        waitAttackStart();
        if self.ready : 
            self.ready();
        handleSimpleClick(BEGIN_ATTACK,2)

        
    def choseInstruction(self, one, two = FIRST,three = SECOND):
        list = [one,two,three];
        for instruction in list:
            self.clickInstruction(instruction);
        
    
    def clickInstruction(self,instruction):
        if type(instruction) == int :
            x = getX(INSTRUCTION_X,INSTRUCTION_WIDTH,INSTRUCTION_SPACING,instruction);
            handleSimpleClick([x,INSTRUCTION_Y])
        elif type(instruction) == Hero:
            instruction.castingUltimate()
            
