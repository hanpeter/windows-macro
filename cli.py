from __future__ import absolute_import
import csv

from argparse import ArgumentParser

from windows_macro import CSVParser


class Application(object):

    def __init__(self):
        self._set_parser()
        self.args = self.parser.parse_args()

    def _set_parser(self):
        self.parser = ArgumentParser()

        self.parser.add_argument(
            'script',
            type=str,
            help='Macro script to be run',
        )

    def run(self):
        CSVParser.parse(self.args.script)


def main():
    app = Application()
    app.run()
