# Football Manager Helper

A tactical analysis helper for Football Manager built with SOLID principles

## Current Status: Phase 1 Complete ✅

### What's Implemented
- **Core Domain Models**: Player, PlayerStats, Position enums
- **Full Test Coverage**: 13 unit tests, 100% passing
- **Clean Architecture**: Proper separation of concerns
- **SOLID Principles**: Applied throughout the codebase

### Quick Start
```bash
# Clone and setup
git clone <your-repo>
cd project-football-manager-helper
python -m venv venv
venv\Scripts\activate # For Windows users
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

### Example Usage
```python
from football_manager.core.models.player import Player
from football_manager.core.enums.position import Position
from football_manager.core.value_objects.player_stats import PlayerStats

# Create a player
stats = PlayerStats(passing=15, crossing=10, dribbling=12, first_touch=14,
                   marking=8, tackling=9, pace=13, acceleration=11, 
                   stamina=16, vision=13)

player = Player.create("Lionel Messi", 35, Position.RIGHT_WINGER, stats)
print(player)  # "Lionel Messi (35) - RW [AVAILABLE]"
```

## Next: Phase 2 - Application SErvices
Coming next: Repository patterns, Player management services, and business logic foundation.