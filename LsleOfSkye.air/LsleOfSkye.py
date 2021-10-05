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
from utils import waitAttackStart,handleSimpleClick,waitAttackStart
from constants import BEGIN_ATTACK,ATTACK_BACK;
auto_setup(__file__)


class TeamOne(Team):
    def __init__(self):
        super().__init__();
        self.artoria = Hero(1);
        self.artoriaXX = Hero(2);
        self.artoriaCaster1 = Hero(3);
        self.artoriaCaster2 = Hero(3);
    
    
    def roundFirst(self):
        self.carry = self.artoria;
        self.artoriaCaster1.castingSkill(2, self.artoriaXX);
        self.artoriaCaster1.castingSkill(3, self.artoriaXX);
        self.artoria.castingSkill(1);
        self.artoriaCaster1.castingSkill(1);
        
        
    def roundSecond(self):
        self.carry = self.artoriaXX;
        self.carry.castingSkill(1);
        self.carry.castingSkill(3);
#         self.artoriaCaster1.castingSkill(2, self.carry);
#         self.artoriaCaster1.castingSkill(3, self.carry);
        self.clothes.exchangeHero(3, 4);
        self.artoriaCaster2.castingSkill(1);
        self.artoriaCaster1.castingSkill(2, self.artoria);
        self.artoriaCaster1.castingSkill(3, self.carry);
        
        
    def roundThird(self):
        self.carry = self.artoria;
        self.carry.castingSkill(2);
        self.carry.castingSkill(3);
        self.artoriaXX.castingSkill(2);
        self.clothes.castingSkill(1);
        
    
    def test(self):
        self.carry = self.artoriaXX;
        self.artoriaCaster1.castingSkill(2, self.carry);
        
        
class TeamTwo(Team):
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
        self.carry.castingSkill(3);

        
    def roundSecond(self):
        pass;
    
    
    def roundThird(self):
        self.clothes.castingSkill(2, self.carry);
        
        
class TeamThree(Team):
    
    def __init__(self):
        super().__init__();
        self.carry = Hero(2);
        self.doubleHero = DoubleHero();
        self.kongMing = Hero(3);

        
    def roundFirst(self):
        self.doubleHero.castingSkills(1);
        self.doubleHero.castingSkills(2, self.carry);
        self.doubleHero.castingSkills(3, self.carry);
        self.carry.castingSkill(1);
        
    
    def roundSecond(self):
        self.clothes.exchangeHero(3, 4);
        self.carry.castingSkill(3);
        self.kongMing.castingSkill(1,self.carry);
        self.kongMing.castingSkill(2);
        self.kongMing.castingSkill(3);
        
        
    def roundThird(self):
        self.carry.castingSkill(2);
        self.clothes.castingSkill(1);
        
        
        

class TeamFourth(Team):
    def __init__(self):
        super().__init__();
        self.artoria = Hero(1);
        self.artoriaRuler = Hero(2);
        self.artoriaCaster = Hero(3);
        
        self.artoria.setCardB(Template(r"tpl1632493076338.png", record_pos=(-0.401, 0.125), resolution=(1630, 934)));
        self.artoria.setCardA(Template(r"tpl1632493254381.png", record_pos=(0.182, 0.122), resolution=(1630, 934)));
        
        
        
    def attack(self):
        rounds = self.createRounds();
        rounds[0].attack();
        

    def skillDefault(self):
        self.artoria.castingSkill(1);
        self.artoria.castingSkill(3);
        self.artoriaRuler.castingSkill(1);
        self.artoriaCaster.castingSkill(1);
        
    
    def skillOne(self):
        self.skillDefault();
        self.artoriaCaster.castingSkill(2,self.artoriaRuler);
        self.artoriaCaster.castingSkill(3,self.artoria);
        self.clothes.castingSkill(2,self.artoriaRuler);

        
    def skillTwo(self):
        self.skillDefault();
        self.artoriaCaster.castingSkill(2,self.artoria);
        self.artoriaCaster.castingSkill(3,self.artoriaRuler);
        self.clothes.castingSkill(2,self.artoria);

        
    def skillThree(self):
        self.skillDefault();
        self.artoriaRuler.castingSkill(3);
        self.artoriaCaster.castingSkill(2,self.artoriaRuler);
        self.artoriaCaster.castingSkill(3,self.artoria);
        self.clothes.castingSkill(2,self.artoriaRuler);
        
        
    def setExtra(self, hero):
        handleSimpleClick(hero.cardBList[0]);
        handleSimpleClick(hero.cardBList[1] or hero.cardBList[1] or hero.cardQList[0]);
        handleSimpleClick(hero.cardAList[0]);
        
        
    def roundFirst(self):
        handleSimpleClick(BEGIN_ATTACK,2);
        
        self.artoria.getCardList();
        
        if self.artoria.cardCountA > 0 and self.artoria.cardCountB > 0:
            if self.artoria.cardCountA > 1 or self.artoria.cardCountB > 1:
                handleSimpleClick(ATTACK_BACK);
                self.skillOne();
                handleSimpleClick(BEGIN_ATTACK,2);
                self.setExtra(self.artoria);
                
#             print("力指令卡列表:",self.artoria.cardBList);

#             print("技指令卡列表:",self.artoria.cardAList);

        
        
        
        
        
if __name__ == '__main__':
    TeamFourth().attack();


