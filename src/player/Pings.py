class Pings:
    def __init__(self, pings: dict[str, int]) -> None:
        self._pings: dict[str, int] = pings

    @property
    def all_in(self) -> int:
        return self._pings.get("ALL_IN_PINGS", -1)

    @property
    def assist_me(self) -> int:
        return self._pings.get("ASSIST_ME_PINGS", -1)

    @property
    def bait(self) -> int:
        return self._pings.get("BAIT_PINGS", -1)

    @property
    def basic(self) -> int:
        return self._pings.get("BASIC_PINGS", -1)
    
    @property
    def command(self) -> int:
        return self._pings.get("COMMAND_PINGS", -1)

    @property
    def danger(self) -> int:
        return self._pings.get("DANGER_PINGS", -1)

    @property
    def enemy_missing(self) -> int:
        return self._pings.get("ENEMY_MISSING_PINGS", -1)

    @property
    def enemy_vision(self) -> int:
        return self._pings.get("ENEMY_VISION_PINGS", -1)

    @property
    def get_back(self) -> int:
        return self._pings.get("GET_BACK_PINGS", -1)

    @property
    def need_vision(self) -> int:
        return self._pings.get("NEED_VISION_PINGS", -1)

    @property
    def hold(self) -> int:
        return self._pings.get("HOLD_PINGS", -1)

    @property
    def on_my_way(self) -> int:
        return self._pings.get("ON_MY_WAY_PINGS", -1)
    
    @property
    def push(self) -> int:
        return self._pings.get("PUSH_PINGS", -1)

    @property
    def retreat(self) -> int:
        return self._pings.get("RETREAT_PINGS", -1)

    @property
    def vision_cleared(self) -> int:
        return self._pings.get("VISION_CLEARED_PINGS", -1)