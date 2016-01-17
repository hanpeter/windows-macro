from __future__ import absolute_import
import csv

import windows_macro


class CSVParser(object):

    @classmethod
    def _parse_line(cls, line):
        if line['action'] == 'focus':
            windows_macro.Window.focus(line['arg1'])
        elif line['action'] == 'click':
            x = int(line['arg1'])
            y = int(line['arg2'])
            windows_macro.Mouse.click(x, y)
        elif line['action'] == 'press':
            windows_macro.Keyboard.press(line['arg1'])

    @classmethod
    def parse(cls, file_path):
        with open(file_path, 'rb') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                cls._parse_line(line)
