# Quadrotor Platform Abstraction for ROS 2

[![Part of: PX4-ROS2 Control Stack](https://img.shields.io/badge/Part_of-PX4--ROS2_Control_Stack-blue)](https://www.evannsmc.com/projects)
![Algorithms](https://img.shields.io/badge/Algorithms-NMPC_%7C_NR_%7C_Geometric-brightgreen)
![Languages](https://img.shields.io/badge/Languages-Python_%7C_C%2B%2B-blue)
[![Docker: PX4-ROS2-Docker](https://img.shields.io/badge/Docker-PX4--ROS2--Docker-2496ED?logo=docker&logoColor=white)](https://github.com/evannsmc/PX4-ROS2-Docker)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A **support library** for the [evannsmc PX4-ROS2 control stack](https://www.evannsmc.com/projects) — an abstract platform interface that lets the same controller code run unchanged on simulation and hardware by hiding platform-specific mass and thrust-throttle conversions behind a common API. It is consumed by the stack's **Python and C++ controllers** (NMPC, Newton-Raphson, geometric); the easiest way to build and integrate the whole stack is the [PX4-ROS2-Docker](https://github.com/evannsmc/PX4-ROS2-Docker) container.

<details>
<summary><b>📖 Table of Contents</b></summary>

- [Supported Platforms](#supported-platforms)
- [Key Features](#key-features)
- [Usage](#usage)
- [API](#api)
- [Package Structure](#package-structure)
- [Installation](#installation)
- [Used by](#used-by)
- [License](#license)

</details>

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

> This is a support package — it is meant to sit alongside one of the controllers in the same workspace `src/`. For a ready-to-build layout of the whole stack, use the [PX4-ROS2-Docker](https://github.com/evannsmc/PX4-ROS2-Docker) container.

## Used by

This is a support package for the controllers in the evannsmc PX4-ROS2 control stack:

- **Python controllers** — [nmpc_acados_px4](https://github.com/evannsmc/nmpc_acados_px4) · [newton_raphson_px4](https://github.com/evannsmc/newton_raphson_px4) · [geometric_px4](https://github.com/evannsmc/geometric_px4)
- **C++ controllers** — [nmpc_acados_px4_cpp](https://github.com/evannsmc/nmpc_acados_px4_cpp) · [newton_raphson_px4_cpp](https://github.com/evannsmc/newton_raphson_px4_cpp) · [geometric_px4_cpp](https://github.com/evannsmc/geometric_px4_cpp)
- **C++ counterpart of this package** — [quad_platforms_cpp](https://github.com/evannsmc/quad_platforms_cpp)
- **Docker integration** — [PX4-ROS2-Docker](https://github.com/evannsmc/PX4-ROS2-Docker)

Part of the [evannsmc open-source portfolio](https://www.evannsmc.com/projects).

## License

MIT
