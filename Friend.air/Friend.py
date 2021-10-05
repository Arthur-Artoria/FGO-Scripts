# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('utils.air')
using('constants.air')

from utils import handleSimpleClick
from constants import SCATI_NAME_IMG,KONGMING_NAME_IMG

auto_setup(__file__)

class Friend:
    
    refreshConfirm = [1060, 700]
    
    refenshTip = Template(r"tpl1615117399147.png",
                                  record_pos=(0.163, -0.18), resolution=(1280, 720));
    refenshSuccess = Template(r"tpl1621150663962.png", record_pos=(0.103, -0.18), resolution=(1280, 720));
    
    def __init__(self,friend):
        self.friend = friend;
        
    
    def emptyFriend(self):
        return exists(Template(r"tpl1621150128550.png", record_pos=(-0.011, 0.066), resolution=(1280, 720)))
            
        
    def chose(self,isSwipe = True):
        
        if self.emptyFriend():
            self.refreshFriends();
        else:
            friend = exists(self.friend)
            if friend:
                touch(friend)
            elif isSwipe:
                swipe([585, 585], vector=[0, -1])
                sleep(2)
                self.chose(False)
            else:
                self.refreshFriends();
        
            
    def refreshFriends(self):
        refresh = exists(self.refenshTip)

        if refresh:
            handleSimpleClick(refresh)
            handleSimpleClick(self.refreshConfirm)
            wait(self.refenshSuccess,60,3)
            self.chose()
        else:
            sleep(10)
            self.refreshFriends()
            
            
if __name__ == '__main__':
    friend = Friend(KONGMING_NAME_IMG)
    friend.chose();
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


