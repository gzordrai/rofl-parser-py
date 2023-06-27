from collections import namedtuple
from json import loads
from os import getcwd
from os.path import abspath, dirname, exists, isabs, join
from struct import unpack
from typing import List, Tuple
from sys import path

path.append(abspath(join(dirname(__file__), "../../")))

from src.exeptions.InvalidFileException import InvalidFileException

FIELDS: list[list[str]] = [
    [
        "ALL_IN_PINGS",
        "ASSIST_ME_PINGS",
        "BAIT_PINGS",
        "BASIC_PINGS",
        "COMMAND_PINGS",
        "DANGER_PINGS",
        "ENEMY_MISSING_PINGS",
        "ENEMY_VISION_PINGS",
        "GET_BACK_PINGS",
        "NEED_VISION_PINGS",
        "HOLD_PINGS",
        "ON_MY_WAY_PINGS",
        "PUSH_PINGS",
        "PUSH_PINGS",
        "RETREAT_PINGS",
        "VISION_CLEARED_PINGS"
    ]
]


class Parser:
    def __init__(self, file: str) -> None:
        self.file: str = file

        if not isabs(file):
            self.file = join(getcwd(), file)

        if not self.file.endswith(".rofl"):
            raise InvalidFileException("Invalid file format. Expected a .rofl file")

        if not exists(self.file):
            raise FileNotFoundError(f"The file does not exist: {self.file}")

    def parse(self) -> Game:
        with open(self.file, "rb") as rofl_file:
            magic_numbers: bytes = rofl_file.read(4)
            FileInfo = namedtuple("FileInfo", ["file_length", "metadata_offset", "metadata_length", "payload_header_offset", "payload_header_length", "payload_offset"])
            file_info: FileInfo
            metadata: Tuple[List[str], List[str]]

            if magic_numbers != b"RIOT":
                raise InvalidFileException("Invalid .rofl file. The file does not meet the required format.")

            rofl_file.seek(262)
            file_info = FileInfo(*unpack("IIIIII", rofl_file.read(26)[2:]))
            rofl_file.seek(file_info.metadata_offset)

            metadata = self.parse_metadata(rofl_file.read(file_info.metadata_length))

        return Game()

    def parse_metadata(self, data: bytes) -> List[dict[str, any]]:
        metadata = loads(data.decode("utf-8"))
        players = loads(metadata["statsJson"].replace("\\", ""))
        stats: list[dict[str, str]] = []

        for player in players:
            for fields in FIELDS:
                stats.append({ key: int(value) if value.isdigit() else value for key, value in player.items() if key in fields })

        return stats