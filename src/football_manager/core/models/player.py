from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4

from football_manager.core.enums.position import Position
from football_manager.core.value_objects.player_stats import PlayerStats

@dataclass
class Player:
    """Core player entity following SRP- only handles player data"""

    id: UUID
    name: str
    age: int
    primary_position: Position
    stats: PlayerStats
    is_injured: bool = False
    injury_description: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate player data"""
        if self.age < 16 or self.age > 45:
            raise ValueError(f"Player age must be between 16 and 45, got {self.age}")
        
        if not self.name.strip():
            raise ValueError("Player name cannot be empty")
        
        if self.is_injured and not self.injury_description:
            raise ValueError("Injured players must have an injury description")
        
    @classmethod
    def create(
        cls,
        name: str,
        age: int,
        primary_position: Position,
        stats: PlayerStats
    ) -> "Player":
        """Factory method to create a new player"""
        player = cls(
            id=uuid4(),
            name=name,
            age=age,
            primary_position=primary_position,
            stats=stats,
        )
        return player
    
    def injure(self, description: str) -> None:
        """Mark player as injured with a description"""
        self.is_injured = True
        self.injury_description = description.strip()

    def heal(self) -> None:
        """Mark player as healed"""
        self.is_injured = False
        self.injury_description = None

    @property
    def is_available(self) -> bool:
        """Check if player is available for selection"""
        return not self.is_injured
    
    def __str__(self) -> str:
        """String representation for display"""
        status = "INJURED" if self.is_injured else "AVAILABLE"
        return f"{self.name} ({self.age}) - {self.primary_position.value} [{status}]"