# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('Team.air')
using('Hero.air')
using('Scatis.air')

from Hero import Hero
from Team import Team
from Scatis import Scatis

auto_setup(__file__)

class MonaLisa(Team):
    
    def __init__(self):
        super().__init__()
        self.carry = Hero(1);
        self.kongMing = Hero(2);
        self.scatis = Scatis();
        [self.scati,self.scatiFriend] = self.scatis.scatis;
#         self.scati = Hero(3);
#         self.kongMingFriend = Hero(2);
        
        
    def roundFirst(self):
        self.carry.castingSkill(1)
        self.scatiFriend.castingSkill(2)
#         self.kongMing.castingSkill(1,self.carry);
#         self.kongMing.castingSkill(2);
#         self.kongMing.castingSkill(3);
#         self.scati.castingSkill(3, self.carry)

        self.scatis.castingScatiSkill(3, self.carry)



    def roundSecond(self):
#         self.clothes.exchangeHero(2,4);
#         self.kongMingFriend.castingSkill(2);
#         self.kongMingFriend.castingSkill(3);
        
        self.carry.castingSkill(3)
        self.scati.castingSkill(2);
        self.clothes.exchangeHero(2,4);
        self.kongMing.castingSkill(2);
        self.kongMing.castingSkill(3);
        self.clothes.castingSkill(1)
        

    def roundThird(self):
#         self.kongMingFriend.castingSkill(1,self.carry);
#         self.scati.castingSkill(2)
        
        self.kongMing.castingSkill(1,self.carry);
        
        
        
        
if __name__ == '__main__':
#     MonaLisa().start()
    monaLisa = MonaLisa()
    monaLisa.attack()
