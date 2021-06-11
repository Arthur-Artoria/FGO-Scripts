# -*- encoding=utf8 -*-
from airtest.core.api import *

using('constants.air')
using('Skill.air')
using('utils.air')

from utils import getX, handleSimpleClick
from Skill import Skill
from constants import CLOTHES_X, CLOTHES_Y, CLOTHES_SKILL_X, CLOTHES_SKILL_Y, CLOTHES_SKILL_WIDTH, CLOTHES_SKILL_SPACING, FIRST, THIRD
__author__ = "LArto"


auto_setup(__file__)


class Clothes:
    def __init__(self) -> None:
        self.skills = list(
            map(lambda order: self.createSkill(order), range(FIRST, THIRD + 1)))

    def createSkill(self, order: int):
        x = getX(CLOTHES_SKILL_X, CLOTHES_SKILL_WIDTH, CLOTHES_SKILL_SPACING, order)
        return Skill([x, CLOTHES_SKILL_Y], 4)

    def clickClothes(self):
        handleSimpleClick([CLOTHES_X, CLOTHES_Y])

    def castingSkill(self, order: int, hero=None):
        self.clickClothes()
        self.skills[order - 1].casting(hero)

