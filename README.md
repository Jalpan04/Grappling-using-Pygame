# Grappling using Pygame

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org) [![Pygame](https://img.shields.io/badge/Pygame-F37626?style=flat&logo=python&logoColor=white)](https://www.pygame.org) ![GitHub repo size](https://img.shields.io/github/repo-size/Jalpan04/Grappling-using-Pygame) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

A 2D physics-based procedurally generated infinite platformer game built in Python using Pygame, featuring dynamic physics, smooth camera tracking, and a mouse-aimed grappling hook mechanic.

## Features

- **Grappling Hook Mechanic**: Shoot a tether hook in any direction using the mouse, attaching to floating platforms and pulling the player towards the hook.
- **Infinite Procedural Generation**: Platforms are dynamically generated ahead of and above the player as they navigate the game world horizontally or vertically, offering infinite progression.
- **Dynamic Physics System**: Simulated gravity, inertia, elastic pull force, and horizontal friction to create a realistic swinging movement.
- **Smooth Camera Tracking**: The view coordinates adjust dynamically to keep the player centered on the screen.
- **Collision Detection**: Real-time bounding-box collisions for landable surfaces.

## Controls

- **Left Mouse Click (Hold)**: Shoot the grappling hook towards the mouse cursor. Keep the button held down to continue pulling yourself towards the attachment point.
- **Release Left Mouse**: Release the grappling hook, enabling the player to launch off or fall under gravity.
- **Aiming**: Aim with the mouse pointer.

## File Structure

```
├── grappling.py          # Core Pygame script including game loop, physics, and rendering
├── .gitignore            # Git ignore patterns
└── LICENSE               # MIT License
```

## Getting Started

### Prerequisites

- Python 3.7 or higher.
- `pygame` library.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jalpan04/Grappling-using-Pygame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Grappling-using-Pygame
   ```
3. Install Pygame:
   ```bash
   pip install pygame
   ```

### Execution

Run the game script:
```bash
python grappling.py
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
