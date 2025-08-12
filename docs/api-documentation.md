# Football Manager Helper - API Documentation

## Core Domain Models

### Position Enum
represents player positions following Football Manager conventions.

```python
from football_manager.core.enums.position import Position, PositionCategory

# Available positions
Position.GOALKEEPER     # "GK"
Position.CENTER_BACK    # "CB"
Position.LEFT_BACK      # "LB"
Position.RIGHT_BACK     # "RB"
# ... etc

# Position Categories for analysis
PositionCategory.GOALKEEPER     # "Goalkeeper"
PositionCategory.DEFENDER       # "Defender"
PositionCategory.MIDFIELDER     # "Midfielder"
PositionCategory.FORWARD        # "Forward
```

### PlayerStats Value Object
Immutable container for player attributes (1-20 scale).

```python
from football_manager.core.value_objects.player_stats import PlayerStats

# Create player stats
stats = PlayerStats(
    passing=15, crossing=10, dribbling=12, first_touch=14,
    marking=8, tackling=9, pace=13, acceleration=11, 
    stamina=16, vision=13
)

# Acesss Computed averages
stats.technical_average     # (passing + crossing + dribbling + first_touch) / 4
stats.defensive_average     # (marking + tackling) / 2
stats.physical_average      # (pace + acceleration + stamina) / 3
stats.overall_average       # All stats / 10
```

### Player Entity
Core player model with injury management.

```python
from football_manager.core.models.player import Player
from football_manager.core.enums.position import Position

# Create a player
player = player.create(
    name="Lionel Messi",
    age=35,
    primary_position=Position.RIGHT_WINGER,
    stats=stats
)

# Injurty Management
player.injure("Hamstring Injury")
player.is_available # False
player.heal()
player.is_available # True

# Display
str(player)     # "Lionel Messi (35) - RW [AVAILABLE]
```

## Validation Rules

### PlayerStats
- All attributes must be integers between 1-20 (Football Manager Scale)
- Raises `ValueError` for invalid values

### Player
- Age must be between 16-45
- Name cannot be empty or whitespace only
- Injured players must have injury description
- Raises `ValueError` for invalid data

## Next Phase Preview
Phase 2 will add:
- Repositotry interfaces for data persistence
- Player management services
- Business logic for tactical analysis foundation