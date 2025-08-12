from enum import Enum

class Position(Enum):
    """Player positions following Football Manager conventions"""
    # Goalkeeper
    GOALKEEPER = "GK"

    # Defenders
    CENTER_BACK = "CB"
    LEFT_BACK = "LB"
    RIGHT_BACK = "RB"
    WING_BACK_LEFT = "WBL"
    WING_BACK_RIGHT = "WBR"

    # Midfielders
    DEFENSIVE_MIDFIELDER = "DM"
    CENTRAL_MIDFIELDER = "CM"
    ATTACKING_MIDFIELDER = "AM"
    LEFT_MIDFIELDER = "LM"
    RIGHT_MIDFIELDER = "RM"

    # Forwards
    CENTER_FORWARD = "ST"
    LEFT_WINGER = "LW"
    RIGHT_WINGER = "RW"

class PositionCategory(Enum):
    """Broader position categories for tactical analysis"""

    GOALKEEPER = "Goalkeeper"
    DEFENDER = "Defender"
    MIDFIELDER = "Midfielder"
    FORWARD = "Forward"

# Mapping positions to categories
POSITION_CATEGORIES = {
    Position.GOALKEEPER: PositionCategory.GOALKEEPER,
    Position.CENTER_BACK: PositionCategory.DEFENDER,
    Position.LEFT_BACK: PositionCategory.DEFENDER,
    Position.RIGHT_BACK: PositionCategory.DEFENDER,
    Position.WING_BACK_LEFT: PositionCategory.DEFENDER,
    Position.WING_BACK_RIGHT: PositionCategory.DEFENDER,
    Position.DEFENSIVE_MIDFIELDER: PositionCategory.MIDFIELDER,
    Position.CENTRAL_MIDFIELDER: PositionCategory.MIDFIELDER,
    Position.ATTACKING_MIDFIELDER: PositionCategory.MIDFIELDER,
    Position.LEFT_MIDFIELDER: PositionCategory.MIDFIELDER,
    Position.RIGHT_MIDFIELDER: PositionCategory.MIDFIELDER,
    Position.CENTER_FORWARD: PositionCategory.FORWARD,
    Position.LEFT_WINGER: PositionCategory.FORWARD,
    Position.RIGHT_WINGER: PositionCategory.FORWARD,
}

def get_position_category(position: Position) -> PositionCategory:
    """Get the category for a given position."""
    return POSITION_CATEGORIES[position]