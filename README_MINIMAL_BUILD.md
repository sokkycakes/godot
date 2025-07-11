# Minimal Godot 4.4 Build Guide

This guide helps you build a custom Godot 4.4 with minimal RAM usage by disabling unnecessary features and modules.

## Overview

The minimal build removes:
- 3D rendering and physics (heaviest RAM consumers)
- XR/VR support
- Advanced GUI features
- Heavy third-party libraries
- Unused modules
- Debugging features

## Prerequisites

1. **Build Dependencies** (Ubuntu/Debian):
   ```bash
   sudo apt update
   sudo apt install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev libgl1-mesa-dev libglu1-mesa-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev
   ```

2. **Python 3.8+** (required for SCons)

## Quick Build

Run the automated build script:
```bash
python3 build_minimal_godot.py
```

This will:
- Detect your platform automatically
- Build export templates with minimal features
- Apply aggressive size optimizations
- Enable only essential modules

## Manual Build

If you prefer manual control, use the custom profile:

```bash
scons platform=linuxbsd target=template_release profile=custom optimize=size_extra lto=full production=yes -j4
```

## Customization

### Modify `custom.py`
Edit the `custom.py` file to adjust which features are disabled:

```python
# Disable more features for even smaller builds
disable_physics_2d = True  # Remove 2D physics
disable_navigation_2d = True  # Remove 2D navigation
opengl3 = False  # Remove OpenGL rendering (headless only)
```

### Modify `build_minimal_godot.py`
Edit the `essential_modules` list to add/remove modules:

```python
essential_modules = [
    "gdscript",  # Keep core scripting
    "regex",     # Keep regular expressions
    # Add your required modules here
]
```

## Module Reference

### Essential Modules (Recommended)
- `gdscript` - Core scripting language
- `regex` - Regular expressions
- `jsonrpc` - JSON-RPC communication
- `zip` - ZIP file support
- `png`, `jpg`, `bmp`, `tga` - Image formats
- `freetype` - Font rendering
- `text_server_adv` - Text rendering
- `audio` - Audio system
- `enet` - Networking
- `mbedtls` - SSL/TLS

### Heavy Modules (Disabled by Default)
- `webxr` - XR/VR support
- `webrtc` - WebRTC networking
- `vhacd` - 3D mesh decomposition
- `lightmapper_rd` - Lightmapping
- `meshoptimizer` - Mesh optimization
- `jolt_physics` - Advanced physics
- `godot_physics_3d` - 3D physics
- `navigation_3d` - 3D navigation

## Build Targets

- `template_release` - Export templates for release builds
- `template_debug` - Export templates for debug builds
- `editor` - Godot editor (not recommended for minimal builds)

## Platform-Specific Notes

### Linux
- Uses OpenGL3 rendering
- SDL for input handling
- ALSA/PulseAudio for audio

### Windows
- Uses OpenGL3 rendering
- DirectInput for input
- WASAPI for audio

### macOS
- Uses OpenGL3 rendering
- CoreAudio for audio
- Metal rendering disabled for minimal builds

## Expected Results

A minimal build should:
- Reduce binary size by 40-60%
- Reduce RAM usage by 30-50%
- Maintain 2D functionality
- Keep essential networking and audio

## Troubleshooting

### Build Fails
1. Check all dependencies are installed
2. Try building without LTO: `lto=none`
3. Reduce parallel jobs: `-j2` instead of `-j4`

### Runtime Issues
1. If audio doesn't work, enable `xaudio2=yes` (Windows)
2. If networking fails, check `enet` module is enabled
3. If rendering fails, ensure `opengl3=yes`

### Still Too Large
1. Disable more modules in `essential_modules`
2. Set `disable_physics_2d=yes`
3. Set `disable_navigation_2d=yes`
4. Consider headless-only build

## Advanced Optimizations

### Link-Time Optimization (LTO)
- `lto=full` - Maximum optimization (slower build)
- `lto=thin` - Faster build, good optimization
- `lto=none` - No LTO (fastest build)

### Size Optimizations
- `optimize=size_extra` - Maximum size reduction
- `optimize=size` - Standard size optimization
- `optimize=speed` - Speed over size

### Memory Optimizations
- `scu_build=yes` - Single compilation unit (uses more RAM during build)
- `disable_exceptions=yes` - Remove exception handling
- `production=yes` - Production optimizations

## Output Files

After successful build, you'll find:
- `bin/godot.linuxbsd.template_release.x86_64` (Linux)
- `bin/godot.windows.template_release.x86_64.exe` (Windows)
- `bin/godot.macos.template_release.x86_64` (macOS)

These are your minimal export templates ready for use in Godot projects.