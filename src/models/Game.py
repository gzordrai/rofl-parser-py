from os.path import abspath, dirname, join
from sys import path

path.append(abspath(join(dirname(__file__), "../../")))

from src.player.Player import Player

class Game:
    def __init__(self, info: dict[str, str | int], players: list[Player]) -> None:
        self._info: dict[str, any] = info
        self._players: list[Player] = players

    def get_duration(self) -> int:
        return self._info.get("gameLength", -1)

    def get_last_game_chunk_id(self) -> int:
        return self._info.get("lastGameChunkId", -1)

    def get_last_key_frame_id(self) -> int:
        return self._info.get("lastKeyFrameId", -1)

    def get_version(self) -> str:
        return self._info.get("gameVersion", -1)