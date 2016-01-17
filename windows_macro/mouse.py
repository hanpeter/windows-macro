from __future__ import absolute_import
import time

import win32api
import win32con
import win32gui


class Mouse(object):

    IN_BETWEEN_DELAY = 0.05
    AFTER_DELAY = 0.1

    @classmethod
    def click(cls, x, y):
        win32api.SetCursorPos((x, y))
        time.sleep(cls.IN_BETWEEN_DELAY)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(cls.IN_BETWEEN_DELAY)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(cls.AFTER_DELAY)

    @classmethod
    def get_loc(cls):
        print win32api.GetCursorPos()
