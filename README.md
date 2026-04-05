# Platform abstraction for throttle-based Quadrotor control in ROS 2 (python)

A ROS 2 Python library providing an abstract platform interface for quadrotor controllers. Enables the same controller code to run seamlessly on simulation and hardware by encapsulating platform-specific mass and thrust-throttle conversions behind a common API.

## Supported Platforms

| Platform | CLI value | Description |
|----------|-----------|-------------|
| Gazebo X500 | `sim` | PX4 SITL simulation platform |
| Holybro X500 V2 | `hw` | Physical Holybro X500 V2 quadrotor |

## Key Features

- **Abstract base class** — `PlatformConfig` defines the interface every platform must implement
- **Registry pattern** — `PLATFORM_REGISTRY` maps `PlatformType` enum values to concrete platform classes
- **Dependency injection** — controllers accept a `PlatformConfig` and never reference concrete platforms directly
- **Thrust-throttle conversion** — each platform implements its own calibrated `get_throttle_from_force()` and `get_force_from_throttle()` methods

## Usage

```python
from quad_platforms import PLATFORM_REGISTRY, PlatformType

platform = PLATFORM_REGISTRY[PlatformType.SIM]()

mass = platform.mass                                # kg
throttle = platform.get_throttle_from_force(9.81)   # N → throttle
force = platform.get_force_from_throttle(0.5)       # throttle → N
```

## API

### `PlatformConfig` (Abstract Base Class)

| Member | Type | Description |
|--------|------|-------------|
| `mass` | `float` (property) | Platform mass in kg |
| `get_throttle_from_force(force)` | `float → float` | Convert thrust in Newtons to a throttle command |
| `get_force_from_throttle(throttle)` | `float → float` | Convert a throttle command to thrust in Newtons |

### `PlatformType` Enum

| Value | String |
|-------|--------|
| `SIM` | `"sim"` |
| `HARDWARE` | `"hw"` |

## Package Structure

```
quad_platforms/
├── __init__.py                          # Public API exports
├── platform_interface.py                # PlatformConfig ABC, PlatformType, PLATFORM_REGISTRY
└── vehicles/
    ├── gz_x500/                         # Gazebo X500 simulation
    │   ├── platform.py
    │   ├── thrust_throttle_conversion.py
    │   └── constants.py
    └── holybro_x500V2/                  # Holybro X500 V2 hardware
        ├── platform.py
        ├── thrust_throttle_conversion.py
        └── constants.py
```

## Installation

```bash
# Inside a ROS 2 workspace src/ directory
git clone git@github.com:evannsmc/quad_platforms.git
cd .. && colcon build --symlink-install
```

## License

MIT
