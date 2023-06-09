from enum import Enum

class Items(Enum):
    # Starter items
    DORANS_SHIELD: int = 1054
    DORANS_BLADE: int = 1055
    DORANS_RING: int = 1056
    DARK_SEAL: int = 1082
    CULL: int = 1083
    SCORCHCLAW_PUP: int = 1101
    GUSTWALKER_HATCHLING: int = 1102
    MOSSTOMPER_SEEDLING: int = 1103
    GUARDIANS_HORN: int = 2051
    TEAR_OF_THE_GODDESS: int = 3070
    GUARDIANS_ORB: int = 3112
    GUARDIANS_BLADE: int = 3177
    GUARDIANS_HAMMER: int = 3184
    STEALTH_WARD: int = 3340
    FARSIGHT_ALTERATION: int = 3363
    ORACLE_LENS: int = 3364
    SPEELTHIEFS_EDGE: int = 3850
    STEEL_SHOULDERGUARDS: int = 3854
    RELIC_SHIELD: int = 3858
    SPECTRAL_SICKLE: int = 3862

    # Potions and Consumables
    HEALTH_POTION: int = 2003
    REFILLABLE_POTION: int = 2031
    CORRUPTING_POTION: int = 2033
    CONTROL_WARD: int = 2055
    ELIXIR_OF_IRON: int = 2138
    ELIXIR_OF_SORCERY: int = 2139
    ELIXIR_OF_WRATH: int = 2140

    # Distributed items
    TOTAL_BISCUIT_OF_EVERLASTING_WILL: int = 2010
    PORO_SNAX: int = 2052
    MINION_DEMATERIALIZER: int = 2403
    SLIGHTLY_MAGICAL_BOOTS: int = 2422
    PERFECTLY_TIMED_STOPWATCH: int = 2423
    YOUR_CUT: int = 3400
    EYE_OF_THE_HERALD: int = 3513

    # Boots
    BOOTS: int = 1001
    BERSERKERS_GREAVES: int = 3006
    BOOTS_OF_SWIFTNESS: int = 3009
    SORCERERS_SHOES: int = 3020
    PLATED_STEELCAPS: int = 3047
    MERCURYS_TREADS: int = 3111
    MOBILITY_BOOTS: int = 3117
    IONIAN_BOOTS_OF_LUCIDITY: int = 3158

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()