from __future__ import absolute_import

import windows_macro.cli
from football_manager.football_manager_parser import FootballManagerParser


class Application(windows_macro.cli.Application):

    def run(self):
        FootballManagerParser.parse(self.args.csv)


def main():
    app = Application()
    app.run()
