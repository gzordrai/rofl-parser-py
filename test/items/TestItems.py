from unittest import main, TestCase
from os.path import abspath, dirname, join
from sys import path

root_path: str = abspath(join(dirname(__file__), "../../"))
path.append(root_path)

from src.player.Items import Items


items: dict[str, int] = {
    "ITEM0": 0,
    "ITEM1": 0,
    "ITEM2": 1,
    "ITEM3": 2,
    "ITEM4": 3,
    "ITEM5": 4,
    "ITEM6": 5
}

class TestMissingItems(TestCase):
    def setUp(self) -> None:
        self.items: Items = Items(items)

    def test_item_0(self) -> None:
        self.assertEqual(items.get("ITEM0"), self.items.item_0)

    def test_item_1(self) -> None:
        self.assertEqual(items.get("ITEM1"), self.items.item_1)

    def test_item_2(self) -> None:
        self.assertEqual(items.get("ITEM2"), self.items.item_2)

    def test_item_3(self) -> None:
        self.assertEqual(items.get("ITEM3"), self.items.item_3)

    def test_item_4(self) -> None:
        self.assertEqual(items.get("ITEM4"), self.items.item_4)

    def test_item_5(self) -> None:
        self.assertEqual(items.get("ITEM5"), self.items.item_5)

    def test_item_6(self) -> None:
        self.assertEqual(items.get("ITEM6"), self.items.item_6)

if __name__ == "__main__":
    main()