class Items:
    def __init__(self, items: dict[str, int]) -> None:
        self.items: dict[str, int] = items

    @property
    def item_0(self) -> int:
        return self.items.get("ITEM0", -1)

    @property
    def item_1(self) -> int:
        return self.items.get("ITEM1", -1)

    @property
    def item_2(self) -> int:
        return self.items.get("ITEM2", -1)

    @property
    def item_3(self) -> int:
        return self.items.get("ITEM3", -1)

    @property
    def item_4(self) -> int:
        return self.items.get("ITEM4", -1)

    @property
    def item_5(self) -> int:
        return self.items.get("ITEM5", -1)

    @property
    def item_6(self) -> int:
        return self.items.get("ITEM6", -1)