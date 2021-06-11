# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *
using('Clothes.air')
using('utils.air')
using('constants.air')
from Clothes import Clothes
from utils import getX, handleSimpleClick,waitAttackStart

from constants import EXCHANGE_Y,EXCHANGE_WIDTH,EXCHANGE_X,EXCHANGE_SPACING,EXCHANGE_ACTION

auto_setup(__file__)

class ExchangeClothes(Clothes):
    def __init__(self):
        super().__init__();

    def exchangeHero(self, current,target):
        self.skills[2].setTimeConsuming(1);
        self.castingSkill(3);
        currentX = getX(EXCHANGE_X,EXCHANGE_WIDTH,EXCHANGE_SPACING,current);
        targetX = getX(EXCHANGE_X,EXCHANGE_WIDTH,EXCHANGE_SPACING,target);
        handleSimpleClick([currentX,EXCHANGE_Y])
        handleSimpleClick([targetX,EXCHANGE_Y])
        handleSimpleClick(EXCHANGE_ACTION);
        waitAttackStart();
    