from unittest import main, TestCase
from os.path import abspath, dirname, join
from sys import path

root_path: str = abspath(join(dirname(__file__), "../../"))
path.append(root_path)

from src.player.Items import Items


class TestItems(TestCase):
    def setUp(self) -> None:
        self.items: Items = Items({})

if __name__ == "__main__":
    main()