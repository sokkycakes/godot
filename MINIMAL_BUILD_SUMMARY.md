# Minimal Godot 4.4 Build - Complete Setup

This directory now contains everything you need to build a custom Godot 4.4 with minimal RAM usage.

## Files Created

### Build Profiles
- **`custom.py`** - Balanced minimal build profile (recommended)
- **`custom_ultra_minimal.py`** - Ultra-minimal build profile (headless only)

### Build Scripts
- **`build_minimal_godot.py`** - Automated script for balanced minimal build
- **`build_ultra_minimal.py`** - Automated script for ultra-minimal build
- **`compare_builds.py`** - Script to compare different builds

### Documentation
- **`README_MINIMAL_BUILD.md`** - Complete build guide and instructions
- **`MINIMAL_BUILD_SUMMARY.md`** - This summary file

## Quick Start

### 1. Balanced Minimal Build (Recommended)
```bash
python3 build_minimal_godot.py
```
This creates a Godot with:
- 2D rendering and physics
- Basic audio and networking
- Essential modules only
- ~40-60% size reduction

### 2. Ultra-Minimal Build (Headless Only)
```bash
python3 build_ultra_minimal.py
```
This creates a Godot with:
- No rendering (headless only)
- GDScript only
- Absolute minimum RAM usage
- ~70-80% size reduction

### 3. Compare Builds
```bash
python3 compare_builds.py
```
Shows size and feature comparison between builds.

## Key Optimizations Applied

### Disabled Features
- 3D rendering and physics (heaviest RAM consumers)
- XR/VR support
- Advanced GUI features
- Heavy third-party libraries
- Unused modules
- Debugging features

### Enabled Optimizations
- `optimize=size_extra` - Maximum size reduction
- `lto=full` - Full link-time optimization
- `production=yes` - Production optimizations
- `disable_exceptions=yes` - Remove exception handling

### Essential Modules Kept
- `gdscript` - Core scripting
- `regex` - Regular expressions
- `jsonrpc` - JSON-RPC communication
- `zip` - ZIP file support
- `png`, `jpg`, `bmp`, `tga` - Image formats
- `freetype` - Font rendering
- `text_server_adv` - Text rendering
- `audio` - Audio system
- `enet` - Networking
- `mbedtls` - SSL/TLS

## Expected Results

### Balanced Minimal Build
- **Binary Size**: ~40-60% smaller than standard
- **RAM Usage**: ~30-50% less than standard
- **Functionality**: Full 2D support, basic networking, audio
- **Use Cases**: 2D games, simple applications, embedded systems

### Ultra-Minimal Build
- **Binary Size**: ~70-80% smaller than standard
- **RAM Usage**: ~60-80% less than standard
- **Functionality**: Headless only, GDScript scripting
- **Use Cases**: Headless servers, command-line tools, testing

## Platform Support

All scripts automatically detect and build for:
- **Linux** (linuxbsd)
- **Windows** (windows)
- **macOS** (macos)

## Troubleshooting

### Build Fails
1. Install dependencies: `sudo apt install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev libgl1-mesa-dev libglu1-mesa-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev`
2. Try without LTO: Edit scripts and change `lto=full` to `lto=none`
3. Reduce parallel jobs: Change `-j4` to `-j2` in scripts

### Runtime Issues
- If audio doesn't work: Enable `xaudio2=yes` (Windows)
- If networking fails: Check `enet` module is enabled
- If rendering fails: Ensure `opengl3=yes`

### Still Too Large
- Use ultra-minimal build instead
- Disable more modules in `essential_modules` list
- Set `disable_physics_2d=yes` and `disable_navigation_2d=yes`

## Customization

### Modify Build Profiles
Edit `custom.py` or `custom_ultra_minimal.py` to adjust features:
```python
# Disable more features
disable_physics_2d = True
disable_navigation_2d = True
opengl3 = False  # Headless only
```

### Modify Module Lists
Edit the `essential_modules` list in build scripts:
```python
essential_modules = [
    "gdscript",  # Keep core scripting
    "regex",     # Keep regular expressions
    # Add/remove modules as needed
]
```

## Output Files

After successful builds, you'll find:
- `bin/godot.linuxbsd.template_release.x86_64` (Linux)
- `bin/godot.windows.template_release.x86_64.exe` (Windows)
- `bin/godot.macos.template_release.x86_64` (macOS)

These are your minimal export templates ready for use in Godot projects.

## Next Steps

1. **Test the builds** with simple Godot projects
2. **Measure actual RAM usage** in your specific use case
3. **Customize further** based on your needs
4. **Use in production** for your RAM-constrained applications

The minimal builds should significantly reduce RAM usage while maintaining the functionality you need for your exports.