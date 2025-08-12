"""Unit tests for the Player model"""

import pytest
from uuid import UUID

from football_manager.core.models.player import Player
from football_manager.core.enums.position import Position
from football_manager.core.value_objects.player_stats import PlayerStats

class TestPlayerCreation:
    """Test Player creation and validation."""

    def test_create_valid_player(self, valid_player_stats):
        """Test creating a valid player"""
        player = Player.create(
            name="Lionel Messi",
            age=35,
            primary_position=Position.RIGHT_WINGER,
            stats=valid_player_stats
        )

        assert player.name == "Lionel Messi"
        assert player.age == 35
        assert player.primary_position == Position.RIGHT_WINGER
        assert player.stats == valid_player_stats
        assert isinstance(player.id, UUID)
        assert not player.is_injured
        assert player.is_available

    def test_player_age_validation_too_young(self, valid_player_stats):
        """Test that players under 16 raise ValueError"""
        with pytest.raises(ValueError, match="Player age must be between 16 and 45, got 15"):
            Player.create(
                name="Too Young",
                age=15,
                primary_position=Position.CENTER_FORWARD,
                stats=valid_player_stats
            )

    def test_player_age_validation_too_old(self, valid_player_stats):
        """Test that players over 45 raise ValueError"""
        with pytest.raises(ValueError, match="Player age must be between 16 and 45, got 46"):
            Player.create(
                name="Too Old",
                age=46,
                primary_position=Position.CENTER_FORWARD,
                stats=valid_player_stats
            )

    def test_empty_name_validation(self, valid_player_stats):
        """Test that empty player names raise ValueError"""
        with pytest.raises(ValueError, match="Player name cannot be empty"):
            Player.create(
                name="",
                age=25,
                primary_position=Position.CENTER_FORWARD,
                stats=valid_player_stats
            )

class TestPlayerInjury:
    """Test Player injury management"""

    def test_injure_player(self, valid_player_stats):
        """Test injuring a player"""
        player = Player.create(
            name="Injured Player",
            age=30,
            primary_position=Position.CENTER_FORWARD,
            stats=valid_player_stats
        )
        player.injure("Hamstring Strain")

        assert player.is_injured
        assert player.injury_description == "Hamstring Strain"
        assert not player.is_available

    def test_heal_player(self, valid_player_stats):
        """Test healing a player from injury"""
        player = Player.create(
            name="Recovering Player",
            age=30,
            primary_position=Position.CENTER_FORWARD,
            stats=valid_player_stats
        )
        player.injure("Ankle Sprain")
        player.heal()

        assert not player.is_injured
        assert player.injury_description is None
        assert player.is_available

class TestPlayerStringRepresentation:
    """Test Player string representation"""

    def test_available_player_str(self, valid_player_stats):
        """Test string representation of available player."""
        player = Player.create(
            name="Cristiano Ronaldo",
            age=38,
            primary_position=Position.CENTER_FORWARD,
            stats=valid_player_stats
        )
        
        expected = "Cristiano Ronaldo (38) - ST [AVAILABLE]"
        assert str(player) == expected
    
    def test_injured_player_str(self, valid_player_stats):
        """Test string representation of injured player."""
        player = Player.create(
            name="Neymar Jr",
            age=31,
            primary_position=Position.LEFT_WINGER,
            stats=valid_player_stats
        )
        
        player.injure("Ankle injury")
        expected = "Neymar Jr (31) - LW [INJURED]"
        assert str(player) == expected