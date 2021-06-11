# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

auto_setup(__file__)

EXP_WIDTH = 130;
EXP_HEIGHT = 130;
EXP_CLOUMN = 7;
# EXP_COUNT = 28;
EXP_COUNT = 20;

def checkExp(expCount):
    count = 0
    while count < expCount:
        x = 137 + (count % EXP_CLOUMN) * EXP_WIDTH;
        y = 240 + int(count / EXP_CLOUMN) * EXP_HEIGHT;
        touch([x,y]);
        count += 1;
        
def sellExps():
    checkExp(28)
    touch(Template(r"tpl1607755986545.png", record_pos=(0.399, 0.245), resolution=(1280, 720)));
    sleep(0.5)
    touch(Template(r"tpl1607756030127.png", record_pos=(0.152, 0.186), resolution=(1280, 720)))
    sleep(1)
    touch(Template(r"tpl1607756046556.png", record_pos=(-0.002, 0.188), resolution=(1280, 720)))

# checkExp(EXP_COUNT)
sellExps();
