from __future__ import absolute_import

import win32api
import win32con
import win32gui


class Window(object):

    @staticmethod
    def focus(name):
        win32gui.SetForegroundWindow(win32gui.FindWindow(None, name))
