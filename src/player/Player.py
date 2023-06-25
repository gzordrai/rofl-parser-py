from os import getcwd
from os.path import join
from sys import path

path.append(join(getcwd(), "src"))

from player import Pings


class Player:
    def __init__(self, uuid: str, username: str, pings: Pings) -> None:
        self.uuid: str = uuid
        self.username: str = username
        self.pings: Pings = pings

    @property
    def uuid(self) -> str:
        return self.uuid

    @property
    def username(self) -> str:
        return self.username

    @property
    def pings(self) -> Pings:
        return self.pings