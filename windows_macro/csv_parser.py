from __future__ import absolute_import
import csv

import windows_macro


class CSVParser(object):

    @classmethod
    def _parse_line(cls, line):
        switch = {
            'focus': windows_macro.Window.focus,
            'click': windows_macro.Mouse.click,
            'press': windows_macro.Keyboard.press
        }

        if line[0] == 'focus':
            windows_macro.Window.focus(*line[1:])
        elif line[0] == 'click':
            x = int(line[1])
            y = int(line[2])
            windows_macro.Mouse.click(x, y)
        elif line[0] == 'press':
            windows_macro.Keyboard.press(line[1])

    @classmethod
    def parse(cls, file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=' ')
            for line in reader:
                cls._parse_line(line)
