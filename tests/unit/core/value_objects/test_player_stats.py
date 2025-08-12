"""Unit tests for PlayerStats value object"""

import pytest
from football_manager.core.value_objects.player_stats import PlayerStats

class TestPlayerStatsValidation:
    """Test PlayerStats validation logic"""

    def test_valid_stats_creation(self, valid_player_stats):
        """Test creating valid player stats."""
        assert valid_player_stats.passing == 15
        assert valid_player_stats.vision == 13

    def test_stats_below_minimum_raises_error(self):
        """Test that stats below 1 raise ValueError"""
        with pytest.raises(ValueError, match="passing must be between 1 and 20"):
            PlayerStats(
                passing=0, # Invalid
                crossing=10, dribbling=12, first_touch=14,
                marking=8, tackling=9, pace=13, acceleration=11,
                stamina=16, vision=13
                )
        
class TestPlayerStatsAverages:
    """Test PlayerStats average calculations"""

    def test_technical_average(self, valid_player_stats):
        """Test technical average calculation."""
        # (15 + 10 + 12 + 14)/4 = 12.75
        assert valid_player_stats.technical_average == 12.75

class TestPlayerStatsSerialization:
    """Test PlayerStats serialization methods."""

    def test_to_dict(self, valid_player_stats):
        """Test converting to dictionary."""
        result = valid_player_stats.to_dict()
        
        assert result["passing"] == 15
        assert result["vision"] == 13
        assert len(result) == 10
    
    def test_from_dict(self):
        """Test creating from dictionary."""
        data = {
            "passing": 15, "crossing": 10, "dribbling": 12, "first_touch": 14,
            "marking": 8, "tackling": 9,
            "pace": 13, "acceleration": 11, "stamina": 16, "vision": 13
        }
        
        stats = PlayerStats.from_dict(data)
        assert stats.passing == 15
        assert stats.vision == 13