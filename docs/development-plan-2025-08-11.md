# Football Manager Helper - Development Plan

## Project Overview
Too often I am guilty of vibe coding where I build these things with AI assistance and just get lost in the sauce.
This project is to force myself to slow down and try to build this project out following SOLID principles. I am 
hoping that this project will help me when it comes from ideation to implementation.

For starters I am going to be using the current assumption that we are using full stats visibility.

## Core Features
- Player management (stats, positions, injuries)
- a Tactics helper where it looks at my players in the context of the league I am playing in to help suggest a tactic.
- Match Simulation and analysis
- Transfer market functionality - to help identify players I can use to upgrade my squad
- Performance Tracking
- Team building - Training scheduling and player progression

## Domain Analysis

### Core Entities
- **Player**: Stats, position, age, injuries, development potential
- **Team**: Squad, formation, tactics, league context
- **Match**: Simulation engine, performance analysis
- **League**: Competition context for tactical anaylsis
- **Training**: Schedules, player development, progression tracking
- **Transfer**: Market analysis, player scouting, upgrade identificaation

### Key Business Rules
- Players have attributes that can suggest specific positions and mentalities this can make or break a tactic
- A Players stats should be measured off of the league average, not based on global ratings
- Training can affect player development over time
- Transfer recommendations based on squad gaps, budget, and tactical evolution

## SOLID Principles Application Strategy

### Single Responsibility Principle (SRP)
- 'Player' handles only player data, not tactics
- 'TacticsAnalyzer' handles only tactical recommendations
- 'TransferAnalyizer' handles only transfer suggestions

### Open/Closed Principle (OCP)
- Extensible tactical systems (4-4-2, 4-3-3, my personal bias 4-1-2-3, etc.)
- Pluggable match simulation algorithms
- Different training methodologies

### Liskov Substitution Principles (LSP)
- Different Player types (Goalkeeper, Outfield) substitutable
- Various tactical formations follow same interface

### Interface Segregation Principle (ISP)
- 'IPlayerStates' vs 'IPlayerDevelopment' vs 'IPlayerInjury'
- 'ITacticalAnalysis' vs 'IFormationBuilder'

### Dependency Inversion Principle (DIP)
- Services depend on repository abstractions
- UI depends on service abstractions

## Development Phases

### Phase 1: Foundation & Player Management
**Goal**: Build solid foundation with player entitites and basic management

**Focus**: Get player modeling right before building complex systems on top

### Phase 2: Tactical Analysis System
**Goal**: Implement the tactics helper that analyzes squad vs league context

### Phase 3: Match Simulation & Analysis
**Goal**: Create match engine that validates tactical decisions

### Phase 4: Transfer Market Intelligence
**Goal**: Build transfer recommendation system

### Phase 5: Training & Development
**Goal**: Add player progression and training systems

## Anti-Vibe Coding Rules
1. **Write tests first** - Forces you to think about interfaces
2. **One feature at a time** - Resist the urge to add "just one more thing"
3. **Refactor before adding** - Clean up before extending
4. **Document decisions** - Why did you choose this approach?
5. **Code review with yourself** - Step away, come back, review your own code

## Success Metrics
- [ ] Can analyze my current squad and suggest optimal formation
- [ ] Can simulate matches and see tactical impact
- [ ] Can identify transfer targets that improve tactical fit
- [ ] Can track player development through training
- [ ] Code follows SOLID principles (measurable through code reviews)

## Architecture Planning

### Project Structure
```
football-manager-helper/
├── src/
│   ├── football_manager/
│   │   ├── core/                      # Domain models, entities, enums
│   │   │   ├── models/                # player.py, team.py, match.py, league.py
│   │   │   ├── enums/                 # position.py, formation.py, tactical_role.py
│   │   │   ├── value_objects/         # player_stats.py, tactical_attributes.py
│   │   │   └── interfaces/            # repository_abc.py, service_abc.py
│   │   ├── application/               # Business logic, use cases
│   │   │   ├── services/              # player_service.py, tactics_analyzer.py
│   │   │   ├── dtos/                  # Data transfer objects
│   │   │   └── interfaces/            # Service contracts (ABC)
│   │   ├── infrastructure/            # Data access, external services
│   │   │   ├── repositories/          # Concrete implementations
│   │   │   └── data/                  # Seed data, JSON storage
│   │   └── console/                   # CLI interface, program entry point
│   │       └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs/
├── requirements.txt
├── pyproject.toml
└── README.md
```

### Decision Log
Keep track of architectural decisions to avoid second-guessing yourself:

| Decision | Reasoning | Trade-offs | Date |
|----------|-----------|------------|------|
| Console UI first | Focus on core logic, not UI complexity | Limited user experience | 2025-08-11 |
| JSON file storage | Simple, no DB setup required | Not scalable, but fine for MVP | 2025-08-11 |
| In-memory league context | Faster development, predictable data | Static data, but realistic for tool | 2025-08-11 |
| Python 3.10+ | Type hints, dataclasses, pattern matching | Requires modern Python | 2025-08-11 |
| Pydantic for DTOs | Built-in validation, serialization | Additional dependency | 2025-08-11 |

### Data Model Strategy
Define your core data relationships upfront:

**Player-League Relationship**:
- How do you measure "league average"? 
- Store league stats separately or calculate dynamically?

**Tactical Complexity**:
- Start simple: Formation + Player Roles
- Avoid mentality/instructions initially (scope creep risk)

**Stats Granularity**:
- Which FM stats actually matter for tactical analysis?
- Focus on 6-8 key attributes max initially

### Technology Constraints
- **Language**: Python 3.10+
- **Storage**: JSON files initially (avoid DB complexity)
- **Testing**: pytest + pytest-mock
- **Validation**: Pydantic for DTOs and data validation
- **Type Checking**: mypy for static type analysis
- **Dependency Injection**: dependency-injector library (lightweight)

### Python-Specific Architecture Patterns
- **Abstract Base Classes (ABC)**: For interfaces/contracts
- **Dataclasses**: For value objects and DTOs
- **Type Hints**: Everywhere for better code documentation
- **Property Decorators**: For computed attributes
- **Context Managers**: For resource management (file operations)

### Scope Boundaries (Anti-Vibe Coding)
**Phase 1 Hard Limits**:
- ✅ Basic player CRUD
- ✅ Simple position assignment
- ❌ No tactical analysis yet
- ❌ No training system
- ❌ No match simulation

**Explicitly Out of Scope (for now)**:
- Real-time data imports
- Multiple save files
- AI opponents
- Complex injury system
- Financial management

## Technical Spikes Needed
Research these before coding:
1. **Formation Representation**: How to model 4-4-2 vs 4-1-2-3 mathematically?
2. **League Context Data**: What constitutes "league average" stats?
3. **Tactical Fit Algorithm**: How to score player suitability for positions?
4. **Python DI Patterns**: How to implement clean dependency injection

## Risk Mitigation
- **Feature Creep**: Stick to phase goals religiously
- **Over-Engineering**: Start with simplest solution that works
- **Analysis Paralysis**: Set 1-week limit per phase planning
- **Perfectionism**: "Good enough" for MVP, refactor in later phases
- **Python Specific**: Avoid "clever" Python tricks, prioritize readability

## Development Setup
```bash
# Virtual environment setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install pytest pytest-mock mypy pydantic dependency-injector

# Project structure creation
mkdir -p src/football_manager/{core,application,infrastructure,console}
mkdir -p tests/{unit,integration}
```