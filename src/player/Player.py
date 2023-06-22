from os import getcwd
from os.path import join
from sys import path

path.append(join(getcwd(), "src"))

from player import Pings


class Player:
    def __init__(self, champion: str, pings: Pings) -> None:
        self.champion: str = champion
        self.pings: Pings = pings

    @property
    def champion(self) -> str:
        return self.champion

    @property
    def pings(self) -> Pings:
        return self.pings