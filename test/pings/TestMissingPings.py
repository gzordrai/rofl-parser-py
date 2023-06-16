from unittest import main, TestCase
from os import getcwd
from os.path import join
from sys import path

path.append(join(getcwd(), "src"))

from player.Pings import Pings


class TestPings(TestCase):
    def setUp(self) -> None:
        self.pings: Pings = Pings({})

    def test_missing_all_in_pings(self) -> None:
        self.assertEqual(-1, self.pings.all_in)

    def test_missing_assist_me_pings(self) -> None:
        self.assertEqual(-1, self.pings.assit_me)

    def test_missing_bait_pings(self) -> None:
        self.assertEqual(-1, self.pings.bait)

    def test_missing_basic_pings(self) -> None:
        self.assertEqual(-1, self.pings.basic)

    def test_missing_command_pings(self) -> None:
        self.assertEqual(-1, self.pings.command)

    def test_missing_danger_pings(self) -> None:
        self.assertEqual(-1, self.pings.danger)

    def test_missing_enemy_missing_pings(self) -> None:
        self.assertEqual(-1, self.pings.enemy_missing)

    def test_missing_enemy_vision_pings(self) -> None:
        self.assertEqual(-1, self.pings.enemy_vision)

    def test_missing_get_back_pings(self) -> None:
        self.assertEqual(-1, self.pings.get_back)

    def test_missing_need_vision_pings(self) -> None:
        self.assertEqual(-1, self.pings.need_vision)

    def test_missing_hold_pings(self) -> None:
        self.assertEqual(-1, self.pings.hold)

    def test_missing_on_my_way_pings(self) -> None:
        self.assertEqual(-1, self.pings.on_my_way)
    
    def test_missing_push_pings(self) -> None:
        self.assertEqual(-1, self.pings.push)

    def test_missing_retreat_pings(self) -> None:
        self.assertEqual(-1, self.pings.retreat)

    def test_missing_vision_cleared_pings(self) -> None:
        self.assertEqual(-1, self.pings.vision_cleared)

if __name__ == "__main__":
    main()