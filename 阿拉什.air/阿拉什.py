# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

auto_setup(__file__)


# 使用无需选择目标的技能或是指令卡
def handleSimpleClick(coordinates,skillTime = 1):
    touch(coordinates);
    sleep(skillTime);
    
    
# 使用需要选择目标的技能
def handleDirectionSkillClick(skillCoordinates,targetCoordinates,skillTime = 3):
    handleSimpleClick(skillCoordinates,2);
    touch(targetCoordinates);
    sleep(skillTime);
    
def handleClickClothes():
    handleSimpleClick([1190,320]);
    
# 点击御主技能加攻击
def handleMasterSkillClick():
    handleSimpleClick([1190,320]);
    handleDirectionSkillClick([900,300],[340,450]);
    
        
# 点击御主换人
def handleChangeHeroClick():
    handleClickClothes();
    handleSimpleClick([1080,300],2);
    handleSimpleClick([540,350]);
    handleSimpleClick([740,350]);
    handleSimpleClick([650,620]);
    waitAttackEnd();
    
# 阿尔托莉雅-alter第一技能
def handleFirstThirdClick():
    handleSimpleClick([75,580],3);

# 阿尔托莉雅-alter第三技能
def handleArtoriaThirdClick():
    handleSimpleClick([250,580],3);
    
# 点击斯卡蒂技能
def handleSkadySkillClick(coordinates):
    handleDirectionSkillClick(coordinates,[340,450],4);
    

# 点击攻击
def handleAttackClick():
    touch(Template(r"tpl1615114541021.png", record_pos=(0.384, 0.191), resolution=(1280, 720)));
    sleep(3)
    

# 选择阿尔托莉雅的宝具
def checkArtoriaXAlterUniqueSkill():
    handleSimpleClick([415,220]);
    

# 斯卡蒂降防
def checkSkadySecondSkill():
    time = 3;
    handleSimpleClick([480,580],time);
    
    
# 选择随机的指令卡
def checkRandomInstructionCard():
    handleSimpleClick([140,520]);
    handleSimpleClick([380,520]);
    
    
# 等待攻击结束
def waitAttackEnd(timeout = 60):
    wait(Template(r"tpl1615114541021.png", record_pos=(0.384, 0.191), resolution=(1280, 720)),timeout,3);


# 点击跳过
def handleSkepClick(coordinates = [1120,666]):
    handleSimpleClick(coordinates);
    
    
# 第一回合
def roundFirst():
    # 阿尔托莉雅的三个技能
    handleSimpleClick([240,580],3);
    # 斯卡蒂充能
    handleSkadySkillClick([560,580]);
    # 斯卡蒂降防
    checkSkadySecondSkill(); 
    # 孔明充能
    handleSimpleClick([800,580],4);
    handleSimpleClick([888,580],4);
    # 御主加攻击
    handleMasterSkillClick();
    # 点击攻击
    handleAttackClick();
#   # 选择阿尔托莉雅的宝具
    checkArtoriaXAlterUniqueSkill();
#   # 选择剩余的指令卡
    checkRandomInstructionCard();
    # 等待攻击结束
    handleFightFinish();
       
    
# 开始任务
def beginFight():
    begin = exists(Template(r"tpl1615117806195.png", record_pos=(0.428, 0.246), resolution=(1280, 720)));
    if begin:
        touch(begin);
        waitAttackEnd();
        beginFight();
    else:
        waitAttackEnd();
        beginAttack();

    
    
# 刷新助战
def refreshFriends():
    refresh = exists(Template(r"tpl1615117399147.png", record_pos=(0.163, -0.18), resolution=(1280, 720)));
    if refresh:
        handleSimpleClick(refresh);
        handleSimpleClick([850,560],2);
        checkFriend();
    else:
        sleep(10);
        refreshFriends();
        


# 选择助战
def checkFriend():
    skady = exists(Template(r"tpl1615117150166.png", record_pos=(-0.154, 0.08), resolution=(1280, 720)));

    if skady:
        touch(skady);
        sleep(3);
        beginFight();
    else:
        refreshFriends();
        
    
    
# 战斗结束
def handleFightFinish():
    wait(Template(r"tpl1615120972447.png", record_pos=(-0.357, -0.137), resolution=(1280, 720)),50,3);
#   羁绊结算
    handleSkepClick();
#   点击跳过经验结算
    handleSkepClick([1120,466]);
#   经验结算
    handleSkepClick();
#   下一步
    handleSkepClick();
    # 点数结算
    handleSkepClick();
    
    unApplyFriend();
#   连续出击
    fightAgain();
    
    
# 连续出击
def fightAgain():
    again = wait(Template(r"tpl1615122121952.png", record_pos=(0.155, 0.161), resolution=(1280, 720)))
    if again:
        handleSimpleClick(again);
        eatApples();
        wait(Template(r"tpl1615122298615.png", record_pos=(0.397, -0.255), resolution=(1280, 720)));
        checkFriend();
    

# 吃苹果
def eatApples():
    if exists(Template(r"tpl1615554190341.png", record_pos=(-0.209, -0.141), resolution=(1280, 720))):
        swipe([370,320], vector=[0, -1]);
        sleep(2);
        handleSimpleClick([400,500]);
        wait(Template(r"tpl1615556577657.png", record_pos=(0.156, 0.155), resolution=(1280, 720)));
        handleSimpleClick([850,560])

# 结束好友申请        
def unApplyFriend():
    end = exists(Template(r"tpl1617033820770.png", record_pos=(-0.245, 0.198), resolution=(1280, 720)));
    if end:
        handleSimpleClick(end);
        
    
def beginAttack():
    roundFirst();
    
# beginAttack();

# handleFightFinish();

checkFriend();
# roundFirst();

# eatApples();
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



