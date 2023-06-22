from collections import namedtuple
from json import loads
from os import getcwd
from os.path import exists, isabs, join
from struct import unpack
from sys import path

path.append(join(getcwd(), "src"))

#from Game import Game
# from exeptions.InvalidFileException import InvalidFileException


class Parser:
    def __init__(self, file: str) -> None:
        self.file: str = file

        if not isabs(file):
            self.file = join(getcwd(), file)

        # if not exists(self.file):
        #     raise FileNotFoundError(f"The file does not exist: {self.file}")

        # if not self.file.endswith(".rofl"):
        #     raise InvalidFileException("Invalid file format. Expected a .rofl file")

    def parse(self):# -> Game:
        with open(self.file, "rb") as data:
            magic_numbers: bytes = data.read(4)
            FileInfo = namedtuple("FileInfo", ["file_length", "metadata_offset", "metadata_length", "payload_header_offset", "payload_header_length", "payload_offset"])
            file_info: FileInfo
            metadata: bytes

            # if magic_numbers != b"RIOT":
            #     raise InvalidFileException("Invalid .rofl file. The file does not meet the required format.")

            data.seek(262)
            file_info = FileInfo(*unpack("IIIIII", data.read(26)[2:]))
            data.seek(file_info.metadata_offset)

            print(loads(loads(data.read(file_info.metadata_length).decode("utf-8"))["statsJson"])[0])


            #metadata = self.parse_metadata(data.read(file_info.metadata_length))

        #return Game()

    def parse_metadata(self, data: bytes) -> None:
        metadata = loads(data.decode("utf-8"))

        print(metadata)

        players = loads(metadata["statsJson"].replace("\\", ""))
        # blue_players: list[Player] = []
        # red_players: list[Player] = []

        for player in players:
            if player["TEAM"] == "100":
                pass
            elif player["TEAM"] == "200":
                pass

parser: Parser = Parser("./data/EUW1-6455420055.rofl").parse()