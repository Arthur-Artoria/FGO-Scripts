# -*- encoding=utf8 -*-

__author__ = "LArto"

from airtest.core.api import *

using('Scatis.air')
using('Hero.air')
using('constants.air')
using('utils.air')
using('Round.air')
using('Team.air')
using('Clothes.air')

from Hero import Hero
from Clothes import Clothes
from Scatis import Scatis
from Round import Round
from constants import FIRST, SECOND, THIRD
from Team import Team
from utils import waitAttackStart
auto_setup(__file__)


class Lancelot(Team):
    
    def __init__(self):
        super().__init__()
        self.carry = Hero(1);
        self.scatis = Scatis();
        [self.scati,self.scatiFriend] = self.scatis.scatis;
        
        
    def roundFirst(self):
        self.carry.castingSkill(3)
        self.scatis.castingScatiSkill(1, self.carry)


    def roundSecond(self):        
        self.scati.castingSkill(3,self.carry);
        

    def roundThird(self):
        self.scatis.castingScatiSkill(2)
        self.scatiFriend.castingSkill(3,self.carry)
        self.clothes.castingSkill(2, self.carry);


if __name__ == '__main__':
    lancelot = Lancelot()
    lancelot.attack(lancelot.rounds)
#     waitAttackStart();
    