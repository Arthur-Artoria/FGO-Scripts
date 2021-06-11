# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *

using('Hero.air');

from Hero import Hero;

auto_setup(__file__)

Hero.test();