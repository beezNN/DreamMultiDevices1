# -*- coding: utf-8 -*-
__author__ = "无声"

import unittest
from tools import  Screencap
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


_print = print
def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

def Main(devices):
    print("{}进入unittest".format(devices))
    class TC101(unittest.TestCase):
        u'''测试用例101的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            print("我是setUp，在每条用例之前执行")

        def test_01_of_101(self):
            u'''用例test_01_of_101的操作步骤'''
            # 每个函数里分别实例poco，否则容易出现pocoserver无限重启的情况
            poco = AndroidUiautomationPoco()
            print("我是TC101的test_01_of_101方法")
            t = 1
            self.assertEquals(1, t)

        def test_02_of_101(self):
            u'''用例test_02_of_101的操作步骤'''
            # 每个函数里分别实例poco，否则容易出现pocoserver无限重启的情况
            poco = AndroidUiautomationPoco()
            time.sleep(5)
            print("我是TC102的test_02_of_101方法")
            Screencap.GetScreen(time.time(), devices, "test_02_of_101的描述")
            t = 1
            self.assertEquals(2, t)


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print("我是tearDown，在每条用例之后执行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC101)
    return srcSuite