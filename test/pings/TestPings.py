from unittest import main, TestCase
from os.path import abspath, dirname, join
from sys import path

root_path: str = abspath(join(dirname(__file__), "../../"))
path.append(root_path)

from src.player.Pings import Pings


pings: dict[str, int] = {
    "ALL_IN_PINGS": 0,
    "ASSIST_ME_PINGS": 1,
    "BAIT_PINGS": 2,
    "BASIC_PINGS": 3,
    "COMMAND_PINGS": 4,
    "DANGER_PINGS": 5,
    "ENEMY_MISSING_PINGS": 6,
    "ENEMY_VISION_PINGS": 7,
    "GET_BACK_PINGS": 8,
    "NEED_VISION_PINGS": 9,
    "HOLD_PINGS": 10,
    "ON_MY_WAY_PINGS": 11,
    "PUSH_PINGS": 12,
    "PUSH_PINGS": 13,
    "RETREAT_PINGS": 14,
    "VISION_CLEARED_PINGS": 15,
}

class TestPings(TestCase):
    def setUp(self) -> None:
        self.pings: Pings = Pings(pings)

    def test_all_in_pings(self) -> None:
        self.assertEqual(pings.get("ALL_IN_PINGS"), self.pings.all_in)

    def test_assist_me_pings(self) -> None:
        self.assertEqual(pings.get("ASSIST_ME_PINGS"), self.pings.assist_me)

    def test_bait_pings(self) -> None:
        self.assertEqual(pings.get("BAIT_PINGS"), self.pings.bait)

    def test_basic_pings(self) -> None:
        self.assertEqual(pings.get("BASIC_PINGS"), self.pings.basic)

    def test_command_pings(self) -> None:
        self.assertEqual(pings.get("COMMAND_PINGS"), self.pings.command)

    def test_danger_pings(self) -> None:
        self.assertEqual(pings.get("DANGER_PINGS"), self.pings.danger)

    def test_enemy_missing_pings(self) -> None:
        self.assertEqual(pings.get("ENEMY_MISSING_PINGS"), self.pings.enemy_missing)

    def test_enemy_vision_pings(self) -> None:
        self.assertEqual(pings.get("ENEMY_VISION_PINGS"), self.pings.enemy_vision)

    def test_get_back_pings(self) -> None:
        self.assertEqual(pings.get("GET_BACK_PINGS"), self.pings.get_back)

    def test_need_vision_pings(self) -> None:
        self.assertEqual(pings.get("NEED_VISION_PINGS"), self.pings.need_vision)

    def test_hold_pings(self) -> None:
        self.assertEqual(pings.get("HOLD_PINGS"), self.pings.hold)

    def test_on_my_way_pings(self) -> None:
        self.assertEqual(pings.get("ON_MY_WAY_PINGS"), self.pings.on_my_way)
    
    def test_push_pings(self) -> None:
        self.assertEqual(pings.get("PUSH_PINGS"), self.pings.push)

    def test_retreat_pings(self) -> None:
        self.assertEqual(pings.get("RETREAT_PINGS"), self.pings.retreat)

    def test_vision_cleared_pings(self) -> None:
        self.assertEqual(pings.get("VISION_CLEARED_PINGS"), self.pings.vision_cleared)

if __name__ == "__main__":
    main()