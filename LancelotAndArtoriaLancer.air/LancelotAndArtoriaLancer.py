# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('Lancelot.air')
using('Hero.air')
using('ExchangeClothes.air')
using('Team.air')
using('Scatis.air')

from Lancelot import Lancelot
from Hero import Hero
from ExchangeClothes import ExchangeClothes
from Team import Team;
from Scatis import Scatis
auto_setup(__file__)

class LancelotAndArtoriaLancer(Team):
    def __init__(self):
        super().__init__();
        self.ArtoriaLancer = Hero(1)
        self.als = Hero(2);
        self.carry = self.als;
        self.kongMing = Hero(3);
        self.scatis = Scatis();
#         [self.scati,self.scatiFriend] = self.scatis.scatis;
        
    def roundFirst(self):
        self.ArtoriaLancer.castingSkill(2);
        self.kongMing.castingSkill(3)
        
        
    def roundSecond(self):
        self.carry = self.ArtoriaLancer;
        self.carry.castingSkill(3)
        self.kongMing.castingSkill(1,self.carry);
        self.kongMing.castingSkill(2)
        
#         self.clothes.exchangeHero(1,4);
#         self.clothes.castingSkill(1);
#         self.castingScatiSkill(2)
#         self.scatiFriend.castingSkill(3, self.carry)
    
    def roundThird(self):
        self.clothes.exchangeHero(3,4);
        self.carry.castingSkill(1)
        self.scatis.castingScatiSkill(2)
        self.scatis.castingScatiSkill(3,self.carry);
        
if __name__ == '__main__':
    monaLisa = LancelotAndArtoriaLancer()
    monaLisa.attack(monaLisa.rounds)