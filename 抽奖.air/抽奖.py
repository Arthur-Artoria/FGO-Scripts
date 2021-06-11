# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

auto_setup(__file__)


    
#礼物盒清理
def clearGiftBox():
    touch([870, 561])
    sleep()
    touch(Template(r"tpl1607754891800.png", record_pos=(0.361, -0.11), resolution=(1280, 720)));
    sleep(1.0)
    touch(Template(r"tpl1607754944937.png", record_pos=(0.152, 0.158), resolution=(1280, 720)))
    
    if exists(Template(r"tpl1607755059729.png", record_pos=(-0.013, -0.062), resolution=(1280, 720))):
        touch(Template(r"tpl1607757191858.png", record_pos=(-0.23, 0.081), resolution=(1280, 720)))
        sleep()
        while exists(Template(r"tpl1607755939188.png", record_pos=(-0.288, -0.085), resolution=(1280, 720))):
            count = 0;
            while count < 7 :
                sleep(0.3)
                touch([137 + 130*count , 238]);
                count += 1;
            touch(Template(r"tpl1607755986545.png", record_pos=(0.399, 0.245), resolution=(1280, 720)));
            sleep(0.5)
            touch(Template(r"tpl1607756030127.png", record_pos=(0.152, 0.186), resolution=(1280, 720)))
            sleep(1)
            touch(Template(r"tpl1607756046556.png", record_pos=(-0.002, 0.188), resolution=(1280, 720)))
            sleep(1)







    

    


def getGift(resetGift):
    
#     初始化抽奖
    if exists(Template(r"tpl1607751809656.png", record_pos=(-0.278, 0.089), resolution=(1600, 900))):
        touch(Template(r"tpl1607752435076.png", record_pos=(-0.17, 0.088), resolution=(1280, 720)))
        sleep(2)
        touch([430, 606])
        sleep(1)
        touch([430, 606])
        sleep(0.5)


        
        
        
#     循环抽奖
    while exists(Template(r"tpl1607350862109.png", record_pos=(-0.167, 0.087), resolution=(1440, 810))):
        touch([420, 461])
        sleep(1)
        touch([430, 606])
        sleep(0.5)
        
        
        
#   校验是否清空礼物盒
    if exists(Template(r"tpl1607754638602.png", record_pos=(0.172, 0.159), resolution=(1280, 720))):
        print(1)
#         clearGiftBox()
#         getGift(resetGift)
#         print(1)
        
#   校验是否重置礼物池
    elif wait(Template(r"tpl1607351729421.png", record_pos=(-0.265, 0.086), resolution=(1440, 810))):
        resetGift()

 
# 重置礼物池
def resetGift():
    if wait(Template(r"tpl1607351729421.png", record_pos=(-0.265, 0.086), resolution=(1440, 810))):
        touch(Template(r"tpl1607351763677.png", record_pos=(0.388, -0.091), resolution=(1440, 810)))
        sleep(2)
        touch(Template(r"tpl1607351804928.png", record_pos=(0.154, 0.156), resolution=(1440, 810)))
        sleep(2)
        touch(Template(r"tpl1607353109102.png", record_pos=(-0.003, 0.159), resolution=(1440, 810)))
        sleep(2)
        getGift(resetGift)

getGift(resetGift)
# resetGift()

# if exists(Template(r"tpl1607350862109.png", record_pos=(-0.167, 0.087), resolution=(1440, 810))):
#     touch(Template(r"tpl1607351056195.png", record_pos=(-0.166, 0.085), resolution=(1440, 810)))

# sleep(1.5)
# touch([500,500])
# # sleep(2)
# wait(Template(r"tpl1607351056195.png", record_pos=(-0.166, 0.085), resolution=(1440, 810)))
# touch(Template(r"tpl1607351056195.png", record_pos=(-0.166, 0.085), resolution=(1440, 810)))