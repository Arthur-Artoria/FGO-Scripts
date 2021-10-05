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
from utils import waitAttackStart,handleSimpleClick

auto_setup(__file__)


class SummerMonaLisa(Team):
    
    def __init__(self):
        super().__init__()
        self.alash = Hero(1);
        self.monaLisa = Hero(1);
        self.fox = Hero(2);
        self.scati = Hero(2);
        self.kongMing = Hero(3);
        self.carry = self.alash;
        self.readys = [self.roundSecond, self.roundThird,self.roundFourth];
        
        
    def setRound(self, round):
        round.attack()
        round.choseInstruction(self.carryry)
        if round.lastHit :
            round.lastHit(round);

        
    def createRounds(self):
        return list(map(lambda ready,lastHit: Round(ready,lastHit), self.readys,[None]))
    
    
    def roundFirst(self):
        self.carry.castingSkill(3);


    def roundSecond(self):
        self.carry = self.monaLisa;
        self.carry.castingSkill(1);
        self.carry.castingSkill(3);
        self.fox.castingSkill(1);
        self.fox.castingSkill(3,self.carry);
        self.kongMing.castingSkill(3);
        

    def roundThird(self):
        self.clothes.exchangeHero(2,4);
        self.kongMing.castingSkill(1,self.carry);
        self.scati.castingSkill(2);
        self.clothes.castingSkill(1);
    
    
    def roundFourth(self):
        self.scati.castingSkill(3,self.carry);
    
    
    def roundFirstLastHit(self,round):
        
        waitAttackStart();
        if exists(Template(r"tpl1624163077731.png", record_pos=(-0.081, -0.244), resolution=(1600, 900))):
            round.attack()
            round.choseInstruction();
            self.roundFirstLastHit(round);

        
    
if __name__ == '__main__':
    monaLisa = SummerMonaLisa()
    monaLisa.attack()
#     monaLisa.roundFirstLastHit();
