from os import getcwd
from os.path import join
from sys import path

path.append(join(getcwd(), "src"))

from player import Pings


class Player:
    def __init__(self, uuid: str, name: str, pings: Pings) -> None:
        self.uuid: str = uuid
        self.name: str = name
        self.pings: Pings = pings

    @property
    def uuid(self) -> str:
        return self.uuid

    @property
    def name(self) -> str:
        return self.name

    @property
    def pings(self) -> Pings:
        return self.pings