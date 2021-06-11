# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('utils.air')
from utils import handleSimpleClick
auto_setup(__file__)


class Skill:
    def __init__(self,coordinates,timeConsuming):
        self.coordinates = coordinates;
        self.timeConsuming = timeConsuming;
        
        
    def setTimeConsuming(self,time:int):
        self.timeConsuming = time;
    
    def casting(self,hero):
        handleSimpleClick(self.coordinates,0)
        if hero:
            sleep(1)
            touch(hero.getSelectPosition())
            sleep(self.timeConsuming)
        else:
            sleep(self.timeConsuming)

#         技能分以下几种：
#           1、无需选择目标；2、选择目标后置；3、需提前指定敌人

