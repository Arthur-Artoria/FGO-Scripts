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

class Lilith(Team):
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
        
        
    def roundSecond(self):
        self.clothes.castingSkill(3,self.carry);
        

    def roundThird(self):
        self.carry.castingSkill(3);
        self.clothes.castingSkill(1, self.carry);
        
        
class ArtoriaArcher(Team):
    def __init__(self):
        super().__init__();
        self.artoriaArcher = Hero(2);
        self.artoriaRuler = Hero(3);
        self.doubleHero = DoubleHero();
        [self.mine, self.friend] = self.doubleHero.heros;
        
        
    def roundFirst(self):
        self.carry = self.artoriaRuler;
        self.mine.castingSkill(1);
        self.mine.castingSkill(2, self.artoriaArcher);
        self.mine.castingSkill(3, self.artoriaArcher);
        self.artoriaArcher.castingSkill(3);
        self.carry.castingSkill(1);
        self.carry.castingSkill(3);
        self.clothes.exchangeHero(1,4);
        self.mine.castingSkill(1);

        
    def roundSecond(self):
        self.carry = self.artoriaArcher;
        self.carry.castingSkill(1);
        self.artoriaRuler.castingSkill(2, self.mine);
        self.mine.castingSkill(3, self.carry);
        

    def roundThird(self):
        self.mine.castingSkill(2, self.carry);