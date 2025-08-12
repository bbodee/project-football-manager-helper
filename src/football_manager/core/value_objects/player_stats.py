from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class PlayerStats:
    """
    Core player attributes for tactical analysis.

    Focusing on 10 key FM attributes for now.  
    Will eventually expand to include more.
    Values typically range from 1 to 20 in Football Manager.
    """

    # Technical attributes
    passing: int
    crossing: int
    dribbling: int
    first_touch: int

    # Defensive attributes
    marking: int
    tackling: int

    # Physical attributes
    pace: int
    acceleration: int
    stamina: int

    # Mental attributes
    vision: int

    def __post_init__(self) -> None:
        """Validate the values are withing the Football Manager Ranges."""
        for field_name, value in self.__dict__.items():
            if not (1 <= value <= 20):
                raise ValueError(f"{field_name} must be between 1 and 20, got {value}")
            
    @property
    def technical_average(self) -> float:
        """Calculate the average of the technical attributes."""
        technical_attrs = [
            self.passing,
            self.crossing,
            self.dribbling,
            self.first_touch
        ]
        return sum(technical_attrs) / len(technical_attrs)
    
    @property
    def defensive_average(self) -> float:
        """Average of defensive attributes."""
        defensive_attrs = [
            self.marking,
            self.tackling
        ]
        return sum(defensive_attrs) / len(defensive_attrs)
    
    @property
    def physical_average(self) -> float:
        """Average of physical attributes."""
        physical_attrs = [
            self.pace,
            self.acceleration,
            self.stamina
        ]
        return sum(physical_attrs) / len(physical_attrs)
    
    @property
    def overall_average(self) -> float:
        """Overall average of all attributes."""
        all_attrs = [
            self.passing,
            self.crossing,
            self.dribbling,
            self.first_touch,
            self.marking,
            self.tackling,
            self.pace,
            self.acceleration,
            self.stamina,
            self.vision
        ]
        return sum(all_attrs) / len(all_attrs)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "passing": self.passing,
            "crossing": self.crossing,
            "dribbling": self.dribbling,
            "first_touch": self.first_touch,
            "marking": self.marking,
            "tackling": self.tackling,
            "pace": self.pace,
            "acceleration": self.acceleration,
            "stamina": self.stamina,
            "vision": self.vision
        }
    
    @classmethod
    def from_dict(cls, data:Dict[str, Any]) -> "PlayerStats":
        """Create PlayerStats from dictionary"""
        return cls(**data)