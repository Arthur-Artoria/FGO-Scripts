# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('Skill.air');
using('constants.air');
using('utils.air')

from Skill import Skill;
import constants;
from constants import FIRST,SECOND,THIRD
from utils import handleSimpleClick,getX

auto_setup(__file__)


class Hero:
    
    def __init__(self,order):
        self.order = order;
        self.skills = {};
        self.x = getX(constants.HERO_X,constants.HERO_WIDTH,constants.HERO_SPACING,self.order)
        self.ultimateX = getX(constants.ULTIMATE_X,constants.ULTIMATE_WIDTH,constants.ULTIMATE_SPACING,order);
        self.selectX = getX(constants.SELECT_HERO_X,constants.SELECT_HERO_WIDTH,constants.SELECT_HERO_SPACING,self.order)
        list(map(lambda order: self.setSkill(order), [FIRST,SECOND,THIRD]))
    
    
    def setSkill(self,order,timeConsuming = 4):
        x = getX(self.x + constants.SKILL_WIDTH / 2,constants.SKILL_WIDTH,constants.SKILL_SPACING,order)
        self.skills[order] = Skill([x,constants.SKILL_Y],timeConsuming);
    
    
    def castingSkill(self,order,hero = None):
        self.skills[order].casting(hero);
        
    def castingUltimate(self):
        handleSimpleClick([self.ultimateX,constants.ULTIMATE_Y])

    def getSelectPosition(self):
        return [self.selectX,constants.SELECT_HERO_Y];
