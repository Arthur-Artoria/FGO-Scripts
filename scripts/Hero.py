# -*- encoding=utf8 -*-
__author__ = "LArto"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",], project_root="D:/work-space/Airtest/scripts")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

def test():
    touch(Template(r"tpl1617893801058.png", record_pos=(0.423, 0.247), resolution=(1280, 720)))

# test()