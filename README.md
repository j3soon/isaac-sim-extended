# ISAAC Sim Extended

> This repo will not be further updated, please refer to <https://github.com/j3soon/isaac-extended> instead.

Provide some Isaac Sim examples and notes not included in the toolkit.

Isaac Sim documentation: https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html

> Note: If you are a developer in the NVIDIA Isaac Sim team and find the examples/notes useful, feel free to include them in the next Isaac Sim release.

## Installation

Download Omniverse Launcher here:
- Linux: https://install.launcher.omniverse.nvidia.com/installers/omniverse-launcher-linux.AppImage
- Windows: https://install.launcher.omniverse.nvidia.com/installers/omniverse-launcher-win.exe

Set up and install Isaac Sim app.

Follow the [Python Environment Guide](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/python_environment.html) to set up a `conda` environment.

```sh
ISAAC_SIM=~/.local/share/ov/pkg/isaac_sim-2021.1.1
cd $ISAAC_SIM
git clone https://github.com/j3soon/isaac-sim-extended.git
```

## Examples

All examples are tested in Isaac Sim 2021.1.1 (`2021.1.1-beta.9+2021.1.141.a62eacb5.teamcity`).

Before running the examples, please `cd` into the `isaac_sim-<VERSION>` directory.

### Dump Commands

```sh
ISAAC_SIM=~/.local/share/ov/pkg/isaac_sim-2021.1.1
conda activate isaac-sim
cd $ISAAC_SIM/python_samples && source setenv.sh
cd $ISAAC_SIM
python dump_commands.py
```

The generated docs are at [isaac-sim-extended/commands.md](commands.md)

## Copyright and License

Copyright (c) 2020-2021, NVIDIA CORPORATION.  All rights reserved.

NVIDIA CORPORATION and its licensors retain all intellectual property
and proprietary rights in and to this software, related documentation
and any modifications thereto.  Any use, reproduction, disclosure or
distribution of this software and related documentation without an express
license agreement from NVIDIA CORPORATION is strictly prohibited.
