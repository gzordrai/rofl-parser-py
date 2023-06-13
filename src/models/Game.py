class Game:
    def __init__(self, duration: int, last_game_chunk_id: int, last_key_frame_id: int, version: str) -> None:
        self.duration: int = duration
        self.last_game_chunk_id: int = last_game_chunk_id
        self.last_key_frame_id: int = last_key_frame_id
        self.version: str = version

    def get_duration(self) -> int:
        return self.duration

    def get_last_game_chunk_id(self) -> int:
        return self.last_game_chunk_id

    def get_last_key_frame_id(self) -> int:
        return self.last_key_frame_id

    def get_version(self) -> str:
        return self.version