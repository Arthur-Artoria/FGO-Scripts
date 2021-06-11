# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *
using('Hero.air');
using('constants.air');
using('Round.air');
using('Lancelot.air')
using('Team.air')
using('Clothes.air')
using('LancelotAndArtoriaLancer.air')
using('Friend.air')
using('MonaLisa.air')
using('utils.air');
using('Game.air');

from Hero import Hero
from Round import Round
from constants import FIRST,SECOND,THIRD,KONGMING_NAME_IMG,SCATI_NAME_IMG;
from Lancelot import Lancelot
from Clothes import Clothes
from LancelotAndArtoriaLancer import LancelotAndArtoriaLancer
from Friend import Friend
from MonaLisa import MonaLisa
from utils import waitAction,handleSimpleClick
from Game import GameActivity;

auto_setup(__file__)

# Lancelot = Scati = ScatiFriend = None;


class InstanceZones:
    def __init__(self,Team,friend,totalCount = None, loop = False):
        self.team = Team();
#         self.team.again = True
        self.friend = Friend(friend)
        self.totalCount = totalCount;
        self.team.afterEnd = self.afterEnd
        self.count = 0;
        self.loop = loop;
        
    
    def beforeStart(self):
        self.count = self.count + 1;
        if self.totalCount == None: return;
        if self.count > self.totalCount: return;
        if self.loop == False: return;    
        self.team.loop = True;
        
        
    def start(self):
        self.beforeStart();
        self.friend.chose();
        self.team.start();
        
        
    def afterEnd(self):
        self.start()
            

if __name__ == '__main__':
    InstanceZones(GameActivity,SCATI_NAME_IMG,totalCount = 2,loop = True).start();
#     InstanceZones(MonaLisa,KONGMING_NAME_IMG).afterEnd();

















