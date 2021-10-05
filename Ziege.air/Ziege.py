# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('DoubleHero.air')
using('Hero.air')
using('constants.air')
using('utils.air')
using('Round.air')
using('Team.air')
using('Clothes.air')

from Hero import Hero
from DoubleHero import DoubleHero
from Round import Round
from Team import Team
from utils import waitAttackStart,handleSimpleClick

auto_setup(__file__)

class Ziege(Team):
    def __init__(self):
        super().__init__();
        self.carry = Hero(2);
        self.doubleHero = DoubleHero();
        [self.mine, self.friend] = self.doubleHero.heros;
        
        
    def roundFirst(self):
        self.doubleHero.castingSkills(1);
        self.doubleHero.castingSkills(2, self.carry);
        self.doubleHero.castingSkills(3, self.carry);
        self.carry.castingSkill(1);
        self.carry.castingSkill(2);
        

    def roundThird(self):
        self.clothes.castingSkill(2, self.carry);
