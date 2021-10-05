# -*- encoding=utf8 -*-

__author__ = "LArto"

from airtest.core.api import *

using('Hero.air')
using('constants.air')

from constants import SECOND,THIRD
from Hero import Hero

auto_setup(__file__)


class DoubleHero:
    def __init__(self, positions = [1, THIRD]) -> None:
        self.heros = list(map(lambda order: Hero(order), positions))
        [self.mine, self.friend] = self.heros;
        
        
    def castingSkills(self, order, hero=None):
        self.mine.castingSkill(order, hero)
        sleep(1)
        self.friend.castingSkill(order, hero)

