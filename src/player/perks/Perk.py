class Perk:
    def __init__(self, perk: dict[str, int]) -> None:
        self.perk: dict[str, int] = perk

    @property
    def id(self) -> int:
        return 0

    @property
    def var_1(self) -> int:
        return 0

    @property
    def var_2(self) -> int:
        return 0

    @property
    def var_3(self) -> int:
        return 0