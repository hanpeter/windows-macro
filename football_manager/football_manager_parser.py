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
    SELECT = {
        'clause': (1005, 525),
        'bonus': (340, 525),
    }
    ADD = {
        'clause': (1295, 475),
        'bonus': (630, 475),
    }
    SUBMIT = (1200, 1050)
    CLAUSE_GAP = 55
    CLAUSE_MATCH_REGEX = re.compile('^(clause|bonus)(\d+)$')
    OPTION_INTIAL_GAP = 30
    OPTION_GAP = 21

    _ALL_ACTIONS = ['increment', 'decrement', 'lock', 'delete', 'select', 'add', 'submit']

    @classmethod
    def _offset_click(cls, move, attribute, str_index):
        index = int(str_index) - 1
        x = move[attribute][0]
        y = move[attribute][1] + (cls.CLAUSE_GAP * index)

        Mouse.click(x, y)

        return (x, y)

    @classmethod
    def _parse_line(cls, line):
        if line['action'] in cls._ALL_ACTIONS:
            move = getattr(cls, line['action'].upper())
            match_obj = cls.CLAUSE_MATCH_REGEX.match(line['attribute'])
            repeat = 1

            if len(line['repeat']) > 0:
                repeat = int(line['repeat'])

            for i in range(0, repeat):
                if line['action'] == 'submit':
                    Mouse.click(*cls.SUBMIT)
                elif line['action'] == 'select':
                    x, y = cls._offset_click(move, match_obj.group(1), match_obj.group(2))

                    option_index = int(line['arg1']) - 1
                    y += cls.OPTION_INTIAL_GAP + (cls.OPTION_GAP * option_index)

                    Mouse.click(x, y)
                elif line['action'] == 'add':
                    x, y = move[line['attribute']]
                    Mouse.click(x, y)

                    option_index = int(line['arg1']) - 1
                    y += cls.OPTION_INTIAL_GAP + (cls.OPTION_GAP * option_index)

                    Mouse.click(x, y)
                else:
                    if line['attribute'] in move:
                        x, y = move[line['attribute']]
                        Mouse.click(x, y)
                    elif match_obj is not None:
                        cls._offset_click(move, match_obj.group(1), match_obj.group(2))
        else:
            super(FootballManagerParser, cls)._parse_line(line)

    @classmethod
    def parse(cls, file_path):
        Window.focus('Football Manager 2013')
        return super(FootballManagerParser, cls).parse(file_path)
