from __future__ import absolute_import
from contextlib import contextmanager

import win32api
import win32con
import win32gui


class Keyboard(object):

    @contextmanager
    def _hold(self, key):
        if key is not None:
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)

        yield

        if key is not None:
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

    def press(self, char, shift = False, control = False, alt = False):
        hold_key = None
        if (shift):
            hold_key = win32con.VK_SHIFT
        if (control):
            hold_key = win32con.VK_CONTROL
        if (alt):
            hold_key = win32con.VK_MENU

        with self._hold(hold_key):
            for c in char:
                isUpper = False
                if (c >= 'A' and c <= 'Z'):
                    isUpper = True

                if (isUpper):
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)

                if isinstance(c, int):
                    key = c
                else:
                    key = ord(c.upper())

                print key

                win32api.keybd_event(key, 0, 0, 0)

                if (isUpper):
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
