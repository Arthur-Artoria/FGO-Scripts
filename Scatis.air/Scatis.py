# -*- encoding=utf8 -*-

__author__ = "LArto"

from airtest.core.api import *
using('Hero.air')
using('constants.air')

from constants import SECOND,THIRD
from Hero import Hero

auto_setup(__file__)


class Scatis:
    def __init__(self) -> None:
        self.scatis = list(map(lambda order: Hero(order), [SECOND, THIRD]))
        [self.scati, self.scatiFriend] = self.scatis;
        
        
    def castingScatiSkill(self, order, hero=None):
        self.scati.castingSkill(order, hero)
        sleep(1)
        self.scatiFriend.castingSkill(order, hero)

