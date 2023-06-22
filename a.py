data: dict[str, int] = {
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
pings: dict[str, str] = {}


for key, value in data.items():
    print(key, value)

    if "PINGS" in key:
        pings.update({key: int(value)})

print(pings)