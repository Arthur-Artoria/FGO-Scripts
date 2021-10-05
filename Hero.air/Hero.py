# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('Skill.air');
using('constants.air');
using('utils.air')

from Skill import Skill;
import constants;
from constants import FIRST,SECOND,THIRD
from utils import handleSimpleClick,getX

auto_setup(__file__)


class Hero:
    
    cardQ = None;
    
    def __init__(self,order):
        self.order = order;
        self.skills = {};
        self.x = getX(constants.HERO_X,constants.HERO_WIDTH,constants.HERO_SPACING,self.order)
        self.ultimateX = getX(constants.ULTIMATE_X,constants.ULTIMATE_WIDTH,constants.ULTIMATE_SPACING,order);
        self.selectX = getX(constants.SELECT_HERO_X,constants.SELECT_HERO_WIDTH,constants.SELECT_HERO_SPACING,self.order)
        list(map(lambda order: self.setSkill(order), [FIRST,SECOND,THIRD]))
        self.cardAList = [];
        self.cardBList = [];
        self.cardQList = [];
    
    
    def setSkill(self,order,timeConsuming = 4):
        x = getX(self.x + constants.SKILL_WIDTH / 2,constants.SKILL_WIDTH,constants.SKILL_SPACING,order)
        self.skills[order] = Skill([x,constants.SKILL_Y],timeConsuming);
    
    
    def castingSkill(self,order,hero = None):
        self.skills[order].casting(hero);
        
    def castingUltimate(self):
        handleSimpleClick([self.ultimateX,constants.ULTIMATE_Y])

    def getSelectPosition(self):
        return [self.selectX,constants.SELECT_HERO_Y];


    def setCardB(self,img):
        self.cardB = img;

    def setCardA(self,img):
        self.cardA = img;
        
    def setCardQ(self,img):
        self.cardQ = img;
        
        
    def __getCardList__(self,card):
        
        cardList = [None,None,None];
        count = 0;
        
        if card:
            cardList = find_all(card);

            cardList = list(map( lambda item: item['result'], filter(lambda cardResulr: cardResulr['confidence'] > 0.95, cardList)))
            count = len(cardList);
            cardList.append(None);
            cardList.append(None);
            cardList.append(None);
            
        return {'count':count,'list':cardList};
    
    def getCardList(self):
#         dataA = self.__getCardList__('cardA','cardCountA');
#         self.__getCardList__('cardB','cardCountB');
#         self.__getCardList__('cardQ','cardCountQ');

        
        dataA = self.__getCardList__(self.cardA);
        dataB = self.__getCardList__(self.cardB);
        dataQ = self.__getCardList__(self.cardQ);
        
        self.cardAList = dataA['list'];
        self.cardBList = dataB['list'];
        self.cardQList = dataQ['list'];
        
        self.cardCountA = dataA['count'];
        self.cardCountB = dataB['count'];
        self.cardCountQ = dataQ['count'];
        
#         self.cardCountA = len(self.cardAList);
#         self.cardCountB = len(self.cardBList);
#         self.cardCountQ = len(self.cardQList);

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    