# -*- encoding=utf8 -*-

__author__ = "LArto"

from airtest.core.api import *
using('Round.air')
using('Clothes.air')
using('ExchangeClothes.air')
using('constants.air')
using('utils.air');
using('Continue.air');

from Round import Round
from Clothes import Clothes
from ExchangeClothes import ExchangeClothes;
from constants import BEGIN_TASK,BEGIN_TASK,BEGIN_TASK_COOR,ATTACK_END,REJECT_FRIEND_COOR,REJECT_FRIEND_TIP,NEXT_STEP,STONE,NETWORK_ERROR,NETWORK_RETRY;
from utils import waitAction,handleSimpleClick;
from Continue import Continue;

auto_setup(__file__)


class Team:
    
    def __init__(self,again = False):
        self.carry = None;
        self.again = again;
        self.loop = True;
        self.continueAttack = Continue();
        self.clothes = ExchangeClothes();
        self.readys = [self.roundFirst, self.roundSecond, self.roundThird];
    
    
    def createRounds(self):
        return list(map(lambda ready: Round(ready), self.readys))

    
    def setRound(self, round):
        round.attack()
        round.choseInstruction(self.carry)
    

    def attack(self):
        rounds = self.createRounds();
        for round in rounds:
            self.setRound(round)


    def start(self):
        if self.again == True:
            waitAction();
        else:
            waitAction(BEGIN_TASK)
            handleSimpleClick(BEGIN_TASK_COOR)
            waitAction();
            
        
        self.attack()
        self.end()
    
    def beforeEnd(self):
        pass
    
    
    def handleSkepClick(self,coordinates = NEXT_STEP):
        handleSimpleClick(coordinates, 1.5)
            
    
    def experience(self):
        #羁绊结算
        sleep(40);
#         self.handleSkepClick();
        wait(ATTACK_END,60,5,self.handleSkepClick)
        #点击跳过经验结算
        handleSimpleClick(NEXT_STEP);
        #经验结算
        self.handleSkepClick()
        # 下一步
        self.handleSkepClick()

        
    
    def rejectFriend(self):
        if exists(REJECT_FRIEND_TIP):
            handleSimpleClick(REJECT_FRIEND_COOR);
        
    
    def roundFirst(self):
        pass


    def roundSecond(self):
        pass
        

    def roundThird(self):
        pass
    
    
    def afterEnd(self):
        pass
    
    
    def end(self):
        self.beforeEnd();
#         waitAction(ATTACK_END);
        self.experience();
        self.rejectFriend();
        self.eatApples();
        self.afterEnd();
        
        
    def eatApples(self):
        self.again = True
        if self.loop:
            self.loop = False;
            self.continueAttack.again();
            
    
    def networkError(self):
        if exists(NETWORK_ERROR):
            handleSimpleClick(NETWORK_RETRY);
            
    
if __name__ == '__main__':
    Team().end();





