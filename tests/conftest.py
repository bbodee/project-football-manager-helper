"""Test configuration and shared fixtures"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from football_manager.core.value_objects.player_stats import PlayerStats

@pytest.fixture
def valid_player_stats():
    """Create valid player stats for testing."""
    return PlayerStats(
        passing=15,
        crossing=10,
        dribbling=12,
        first_touch=14,
        marking=8,
        tackling=9,
        pace=13,
        acceleration=11,
        stamina=16,
        vision=13
    )

@pytest.fixture
def goalkeeper_stats():
    """Stats typical for a goalkeeper."""
    return PlayerStats(
        passing=10,
        crossing=5,
        dribbling=6,
        first_touch=12,
        marking=15,
        tackling=8,
        pace=8,
        acceleration=7,
        stamina=12,
        vision=16
    )

@pytest.fixture
def test_player(valid_player_stats):
    """Create a test player for testing."""
    from football_manager.core.models.player import Player
    from football_manager.core.enums.position import Position
    
    return Player.create(
        name="Test Player",
        age=25,
        primary_position=Position.CENTRAL_MIDFIELDER,
        stats=valid_player_stats
    )