from os import getcwd
from os.path import join
from sys import path

path.append(join(getcwd(), "src"))

from player import Pings


class Player:
    def __init__(self, pings: Pings) -> None:
        self.pings: Pings = pings

    @property
    def pings(self) -> Pings:
        return self.pings