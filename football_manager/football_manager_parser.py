from __future__ import absolute_import
import re

from windows_macro import Mouse, Window
from windows_macro.csv_parser import CSVParser


class FootballManagerParser(CSVParser):

    INCREMENT = {
        'wage': (1320, 355),
        'year': (1320, 385),
        'loyalty': (1320, 415),
        'agent': (1320, 445),
        'clause': (1320, 525),
        'bonus': (660, 525),
    }
    DECREMENT = {
        'wage': (1295, 355),
        'year': (1295, 385),
        'loyalty': (1295, 415),
        'agent': (1295, 445),
        'clause': (1295, 525),
        'bonus': (630, 525),
    }
    LOCK = {
        'wage': (1005, 355),
        'year': (1005, 385),
        'loyalty': (1005, 415),
        'agent': (1005, 445),
        'status': (345, 415),
        'clause': (1330, 500),
        'bonus': (665, 500),
    }
    DELETE = {
        'clause': (700, 500),
        'bonus': (35, 500),
    }
    SUBMIT = (1200, 1050)
    CLAUSE_GAP = 55
    CLAUSE_MATCH_REGEX = re.compile('^(clause|bonus|delete)(\d+)$')

    @classmethod
    def _parse_line(cls, line):
        switch = {
            'increment': cls.INCREMENT,
            'decrement': cls.DECREMENT,
            'lock': cls.LOCK,
            'delete': cls.DELETE,
        }
        move = None
        repeat = 1

        if len(line) > 2:
            print line[2]
            repeat = int(line[2])

        if line[0] in switch:
            for i in range(0, repeat):
                move = switch[line[0]]
                match_obj = cls.CLAUSE_MATCH_REGEX.match(line[1])

                if line[1] in move:
                    pos = move[line[1]]
                    Mouse.click(*pos)
                elif match_obj is not None:
                    index = int(match_obj.group(2)) - 1
                    x = move[match_obj.group(1)][0]
                    y = move[match_obj.group(1)][1] + (cls.CLAUSE_GAP * index)
                    Mouse.click(x, y)

            return
        elif line[0] == 'submit':
            Mouse.click(*cls.SUBMIT)
            return

        return super(FootballManagerParser, cls)._parse_line(line)

    @classmethod
    def parse(cls, file_path):
        Window.focus('Football Manager 2013')
        return super(FootballManagerParser, cls).parse(file_path)
