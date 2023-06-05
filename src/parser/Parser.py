from collections import namedtuple
from json import loads
from os.path import exists
from struct import unpack

from Game import Game
from exeptions.InvalidFileException import InvalidFileException


class Parser:
    def __init__(self, file: str) -> None:
        self.file: str = file

        if not exists(self.file):
            raise FileNotFoundError(f"The file does not exist: {self.file}")

        if not self.file.endswith(".rofl"):
            raise InvalidFileException("Invalid file format. Expected a .rofl file")

    def parse(self) -> Game:
        magic_numbers: bytes
        metadata: bytes
        file = namedtuple("length_fields", ["file_length", "metadata_offset", "metadata_length", "payload_header_offset", "payload_header_length", "payload_offset"])

        with open(self.file, "rb") as data:
            magic_numbers = data.read(4)

            if magic_numbers != b"RIOT":
                raise InvalidFileException("Invalid .rofl file. The file does not meet the required format.")

            data.seek(262)
            file(*unpack("IIIIII"), data.read(26))
            data.seek(file.metadata_offset)

            metadata = self.parse_metadata(data.read(file.metadata_length))

        return Game()

    def parse_metadata(self, data: bytes) -> None:
        metadata = loads(data.decode("utf-8"))
        players = loads(metadata["statsJson"].replace("\\", ""))
        blue_players: list[Player] = []
        red_players: list[Player] = []

        for player in players:
            if player["TEAM"] == "100":
                pass
            elif player["TEAM"] == "200":
                pass