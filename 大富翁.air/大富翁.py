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
from Scatis import Scatis
from Round import Round
from Team import Team

auto_setup(__file__)


class GameActivity(Team):
    
    def __init__(self):
        super().__init__()
        self.alash = Hero(1);
        self.gold = Hero(1);
        self.carry = self.alash;
        self.kongMing = Hero(3);
        self.scatis = Scatis();
        [self.scati,self.scatiFriend] = self.scatis.scatis;
        
        
    def roundFirst(self):
        pass;


    def roundSecond(self):
        self.carry = self.gold;
        self.carry.castingSkill(1);
        self.scatis.castingScatiSkill(1, self.carry);
        self.scatis.castingScatiSkill(3, self.carry)
        

    def roundThird(self):
        self.clothes.exchangeHero(3,4);
        self.carry.castingSkill(2);
        self.kongMing.castingSkill(1,self.carry);
        self.kongMing.castingSkill(3);

        
        
if __name__ == '__main__':
    game = GameActivity()
    game.attack(game.rounds)