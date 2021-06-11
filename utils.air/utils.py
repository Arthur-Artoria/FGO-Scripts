# -*- encoding=utf8 -*-

__author__ = "LArto"

from airtest.core.api import *

using('constants.air')

from constants import FIRST, SECOND, THIRD,BEGIN_ATTACK

auto_setup(__file__)


def getX(start, width, spacing, order):
    return start + (order - 1) * (width + spacing)


# 使用无需选择目标的技能或是指令卡
def handleSimpleClick(coordinates, skillTime=1):
    touch(coordinates)
    sleep(skillTime)

# 等待攻击开始


def waitAttackStart(timeout=60):
    return waitAction();


def waitAction(action = BEGIN_ATTACK, timeout = 60):
    return wait(action,timeout,3);    
