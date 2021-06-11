# -*- encoding=utf8 -*-
from Team import Team
from utils import createScatis
from constants import FIRST, SECOND, THIRD
from Hero import Hero
from Round import Round
__author__ = "LArto"
from Scatis import Scatis
from airtest.core.api import *

using('Scatis.air')
using('Hero.air')
using('constants.air')
using('utils.air')
using('Round.air')
using('Team.air')


auto_setup(__file__)


class Lancelot(Scatis, Team):
    def __init__(self):
        super().__init__()
        self.lancelot = Hero('兰斯洛特', FIRST)
        self.rounds = self.createRounds([self.roundFirst, self.roundSecond])

    def setRound(self, round):
        round.attack()
        round.choseInstruction(self.lancelot)

    def roundFirst(self):
        self.lancelot.castingSkill(THIRD)
        self.castingScatiSkill(FIRST, self.lancelot)

    def roundSecond(self):
        self.scati.castingSkill(THIRD, self.lancelot)

    def roundThird(self):
        self.castingScatiSkill(SECOND)
        self.scatiFriend.castingSkill(THIRD, self.lancelot)

    def start(self):
        self.attack(self.rounds)


if __name__ == '__main__':

    # 使用无需选择目标的技能或是指令卡
    def handleSimpleClick(coordinates, skillTime=1):
        touch(coordinates)
        sleep(skillTime)

    # 使用需要选择目标的技能

    def handleDirectionSkillClick(skillCoordinates, targetCoordinates, skillTime=3):
        handleSimpleClick(skillCoordinates, 2)
        touch(targetCoordinates)
        sleep(skillTime)

    # 点击御主技能图标

    def handleMasterSkillClick():
        handleSimpleClick([1190, 320])
        handleDirectionSkillClick([1000, 300], [340, 450])

    # 华美新年-新年初阳

    def handleMasterNewYearSun():
        handleSimpleClick([1190, 320])
        handleSimpleClick([900, 300], 2)

    # 点击兰斯洛特第三技能

    def handleFirstThirdClick():
        handleSimpleClick([250, 580], 3)

    # 点击斯卡蒂技能

    def handleSkadySkillClick(coordinates):
        handleDirectionSkillClick(coordinates, [340, 450], 4)

    # 点击攻击

    def handleAttackClick():
        touch(Template(r"tpl1615114541021.png", record_pos=(
            0.384, 0.191), resolution=(1280, 720)))
        sleep(3)

    # 选择兰斯洛特的宝具

    def checkLancelotUniqueSkill():
        handleSimpleClick([415, 220])

    # 斯卡蒂降防

    def checkSkadySecondSkill():
        time = 3
        handleSimpleClick([480, 580], time)
        handleSimpleClick([800, 580], time)

    # 选择随机的指令卡

    def checkRandomInstructionCard():
        handleSimpleClick([140, 520])
        handleSimpleClick([380, 520])

    # 等待攻击结束

    def waitAttackEnd(timeout=60):
        wait(Template(r"tpl1615114541021.png", record_pos=(
            0.384, 0.191), resolution=(1280, 720)), timeout, 3)

    # 点击跳过

    def handleSkepClick(coordinates=[1120, 666]):
        handleSimpleClick(coordinates)

    # 第一回合

    def roundFirst():
        # 点击兰斯洛特第三技能
        handleFirstThirdClick()
        # 点击斯卡蒂第一技能
        handleSkadySkillClick([390, 580])
        # 点击第二个斯卡蒂第一技能
        handleSkadySkillClick([700, 580])
        # 点击攻击
        handleAttackClick()
    #   # 选择兰斯洛特的宝具
        checkLancelotUniqueSkill()
    #   # 选择剩余的指令卡
        checkRandomInstructionCard()
    #   # 等待攻击结束
        waitAttackEnd()

    # 第二回合

    def roundSecond():
        #   #斯卡蒂充能
        #   handleSkadySkillClick([880,580]);
        # 御主充能
        handleMasterSkillClick()
        # 点击攻击
        handleAttackClick()
        # 选择兰斯洛特的宝具
        checkLancelotUniqueSkill()
        # 选择剩余的指令卡
        checkRandomInstructionCard()
        # 等待攻击结束
        waitAttackEnd()

    # 第三回合

    def roundThird():
        #     斯卡蒂充能
        handleSkadySkillClick([560, 580])
        handleSkadySkillClick([880, 580])
    #     御主充能
    #   handleMasterSkillClick();
    #   新年初阳
        handleMasterNewYearSun()
    #     斯卡蒂降防
        checkSkadySecondSkill()
        # 点击攻击
        handleAttackClick()
        # 选择兰斯洛特的宝具
        checkLancelotUniqueSkill()
        # 选择剩余的指令卡
        checkRandomInstructionCard()
        # 等待攻击结束
        handleFightFinish()

    # 开始任务

    def beginFight():
        begin = exists(Template(r"tpl1615117806195.png",
                                record_pos=(0.428, 0.246), resolution=(1280, 720)))
        if begin:
            touch(begin)
            waitAttackEnd()
            beginFight()
        else:
            waitAttackEnd()
            beginAttack()

    # 刷新助战

    def refreshFriends():
        refresh = exists(Template(r"tpl1615117399147.png",
                                  record_pos=(0.163, -0.18), resolution=(1280, 720)))
        if refresh:
            handleSimpleClick(refresh)
            handleSimpleClick([850, 560], 2)
            checkFriend()
        else:
            sleep(10)
            refreshFriends()

    # 选择助战

    def checkFriend():
        skady = exists(Template(r"tpl1615117150166.png",
                                record_pos=(-0.154, 0.08), resolution=(1280, 720)))
        if skady:
            touch(skady)
            sleep(3)
            beginFight()
        else:
            refreshFriends()

    # 战斗结束

    def handleFightFinish():
        wait(Template(r"tpl1615120972447.png",
                      record_pos=(-0.357, -0.137), resolution=(1280, 720)), 50, 3)
    #   羁绊结算
        handleSkepClick()
    #   点击跳过经验结算
        handleSkepClick([1120, 466])
    #   经验结算
        handleSkepClick()
    #   下一步
        handleSkepClick()
    #     连续出击
        fightAgain()

    # 连续出击

    def fightAgain():
        again = wait(Template(r"tpl1615122121952.png", record_pos=(
            0.155, 0.161), resolution=(1280, 720)))
        if again:
            handleSimpleClick(again)
    #         eatApples();
            wait(Template(r"tpl1615122298615.png", record_pos=(
                0.397, -0.255), resolution=(1280, 720)))
            checkFriend()

    # 吃苹果

    def eatApples():
        if exists(Template(r"tpl1615554190341.png", record_pos=(-0.209, -0.141), resolution=(1280, 720))):
            swipe([370, 320], vector=[0, -1])
            sleep(2)
            handleSimpleClick([400, 500])
            wait(Template(r"tpl1615556577657.png", record_pos=(
                0.156, 0.155), resolution=(1280, 720)))
            handleSimpleClick([850, 560])

    def beginAttack():
        roundFirst()
        roundSecond()
        roundThird()

    # beginAttack();

    # handleFightFinish();

    checkFriend()

    # eatApples();
