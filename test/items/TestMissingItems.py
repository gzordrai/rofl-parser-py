from unittest import main, TestCase
from os.path import abspath, dirname, join
from sys import path

root_path: str = abspath(join(dirname(__file__), "../../"))
path.append(root_path)

from src.player.Items import Items


class TestMissingItems(TestCase):
    def setUp(self) -> None:
        self.items: Items = Items({})

    def test_missing_item_0(self) -> None:
        self.assertEqual(-1, self.items.item_0)

    def test_missing_item_1(self) -> None:
        self.assertEqual(-1, self.items.item_1)

    def test_missing_item_2(self) -> None:
        self.assertEqual(-1, self.items.item_2)

    def test_missing_item_3(self) -> None:
        self.assertEqual(-1, self.items.item_3)

    def test_missing_item_4(self) -> None:
        self.assertEqual(-1, self.items.item_4)

    def test_missing_item_5(self) -> None:
        self.assertEqual(-1, self.items.item_5)

    def test_missing_item_6(self) -> None:
        self.assertEqual(-1, self.items.item_6)

if __name__ == "__main__":
    main()