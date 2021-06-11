# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

auto_setup(__file__)

# 英雄间的间距,宽度
# 第一个英雄的X坐标
# 技能间的间距
# 第一个技能的中心坐标
# 技能选择目标时 英雄的间距
# 技能选择目标时 初始英雄坐标
# 英雄顺序
# 技能顺序
#

HERO_X = 50
HERO_WIDTH = 300
HERO_SPACING = 100

SELECT_HERO_WIDTH = 280
SELECT_HERO_X = 270 + SELECT_HERO_WIDTH / 2
SELECT_HERO_Y = 560
SELECT_HERO_SPACING = 100

SKILL_WIDTH = 80
SKILL_Y = 720
SKILL_SPACING = 30
SKILL_DEFAULT = 1
SKILL_DIRECTION = 2

ULTIMATE_WIDTH = 190
ULTIMATE_X = 420 + ULTIMATE_WIDTH / 2
ULTIMATE_Y = 250
ULTIMATE_SPACING = 130

INSTRUCTION_WIDTH = 190
INSTRUCTION_X = 65 + INSTRUCTION_WIDTH / 2
INSTRUCTION_Y = 600
INSTRUCTION_SPACING = 130

FIRST = 1
SECOND = 2
THIRD = 3

CLOTHES_X = 1500
CLOTHES_Y = 400;
CLOTHES_SKILL_WIDTH = 80
CLOTHES_SKILL_X = 1090 + CLOTHES_SKILL_WIDTH / 2
CLOTHES_SKILL_Y = 400
CLOTHES_SKILL_SPACING = 25

EXCHANGE_Y = 430;
EXCHANGE_WIDTH = 200
EXCHANGE_X = 65 + EXCHANGE_WIDTH / 2;
EXCHANGE_SPACING = 50
EXCHANGE_ACTION = [800,780]


# 开始任务
BEGIN_TASK_COOR = [1480,840];
# 拒绝好友
REJECT_FRIEND_COOR = [430,770]; 

# 下一步
NEXT_STEP = [1400,840];

CONTINUE_ATTACK = Template(r"tpl1622819688809.png", record_pos=(0.156, 0.161), resolution=(1600, 900));

SCATI_NAME_IMG = Template(r"tpl1615117150166.png",
                                record_pos=(-0.154, 0.08), resolution=(1280, 720))
KONGMING_NAME_IMG = Template(r"tpl1621151116274.png", record_pos=(-0.113, 0.198), resolution=(1280, 720))
BEGIN_TASK = Template(r"tpl1615117806195.png",
                                record_pos=(0.428, 0.246), resolution=(1280, 720))
BEGIN_ATTACK = Template(r"tpl1615114541021.png", record_pos=(
        0.384, 0.191), resolution=(1280, 720))

A = Template(r"tpl1615120972447.png",
                      record_pos=(-0.357, -0.137), resolution=(1280, 720));

ATTACK_END = Template(r"tpl1622825649397.png", record_pos=(-0.001, 0.224), resolution=(1600, 900))

REJECT_FRIEND_TIP = Template(r"tpl1621154035653.png", record_pos=(0.009, 0.145), resolution=(1280, 720))
STONE = Template(r"tpl1615554190341.png", record_pos=(-0.209, -0.141), resolution=(1280, 720))

COPPER_APPLE = Template(r"tpl1622822958084.png", record_pos=(-0.209, 0.109), resolution=(1600, 900))

SILVER_APPLE = Template(r"tpl1623079626986.png", record_pos=(-0.209, 0.088), resolution=(1600, 900));






