from dataclasses import dataclass
from BaseClasses import ItemClassification

# Pretty much all of the parameters here are for weapons currently, although that might change in the future, who knows
@dataclass(frozen=True)
class ItemData:
    id: int
    classification: ItemClassification
    level: int | None = None
    player_class: str | None = None
    weapon_type: str | None = None
    dlc_type: str | None = None
    other_type: str | None = None
    difficulty: int | None = None
    unobtainable: bool | None = None