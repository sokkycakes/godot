# Minimal Godot 4.4 Build - Complete Setup

This directory now contains everything you need to build a custom Godot 4.4 with minimal RAM usage.

## Important: Editor vs Export Templates

**These builds primarily create EXPORT TEMPLATES, not the editor itself.** Here's the difference:

### Export Templates (`target=template_release`)
- Used when you export your game from the Godot editor
- These are the runtime engines that run your exported games
- Much smaller and more optimized than the editor
- This is what reduces RAM usage in your final exported games

### Godot Editor (`target=editor`)
- The development environment you use to create games
- Much larger because it includes all development tools
- You can use the standard Godot editor OR build a minimal editor

## Files Created

### Build Profiles
- **`custom.py`** - Balanced minimal build profile (recommended)
- **`custom_ultra_minimal.py`** - Ultra-minimal build profile (headless only)

### Build Scripts
- **`build_minimal_godot.py`** - Automated script for minimal export templates
- **`build_minimal_editor.py`** - Automated script for minimal editor
- **`build_ultra_minimal.py`** - Automated script for ultra-minimal export templates
- **`compare_builds.py`** - Script to compare different builds

### Documentation
- **`README_MINIMAL_BUILD.md`** - Complete build guide and instructions
- **`DEVELOPMENT_WORKFLOW.md`** - How to use minimal builds in development
- **`MINIMAL_BUILD_SUMMARY.md`** - This summary file

## Development Workflow

### Recommended Approach: Standard Editor + Minimal Exports
1. **Use the standard Godot editor** for development (download from godotengine.org)
2. **Build minimal export templates** using these scripts
3. **Configure your project** to use the minimal export templates
4. **Export your game** - it will use the minimal runtime engine

### Alternative: Minimal Editor + Minimal Exports
1. **Build minimal editor**: `python3 build_minimal_editor.py`
2. **Build minimal export templates**: `python3 build_minimal_godot.py`
3. **Use both minimal builds** for maximum RAM savings

## Quick Start

### 1. Build Minimal Export Templates (Most Important)
```bash
python3 build_minimal_godot.py
```
This creates export templates with:
- 2D rendering and physics
- Basic audio and networking
- Essential modules only
- ~40-60% size reduction

### 2. Build Minimal Editor (Optional)
```bash
python3 build_minimal_editor.py
```
This creates a minimal editor with:
- Reduced development tools
- Same optimizations as export templates
- ~25-40% RAM reduction during development

### 3. Ultra-Minimal Build (Headless Only)
```bash
python3 build_ultra_minimal.py
```
This creates ultra-minimal export templates with:
- No rendering (headless only)
- GDScript only
- Absolute minimum RAM usage
- ~70-80% size reduction

### 4. Compare Builds
```bash
python3 compare_builds.py
```
Shows size and feature comparison between builds.

## Using Minimal Export Templates

### 1. Build the Templates
```bash
python3 build_minimal_godot.py
```

### 2. Configure Godot Editor
1. Open your Godot project in the standard editor
2. Go to **Project → Project Settings → Export**
3. Select your export preset (e.g., "Linux/X11")
4. In **Export Path**, set where you want your game exported
5. **Important**: In **Custom Template**, browse to your minimal export template:
   - Linux: `bin/godot.linuxbsd.template_release.x86_64`
   - Windows: `bin/godot.windows.template_release.x86_64.exe`
   - macOS: `bin/godot.macos.template_release.x86_64`
6. Click **Export Project**

### 3. Result
- Your exported game will use the minimal runtime engine
- Significantly reduced RAM usage compared to standard exports
- Same development experience, smaller final game

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

### Export Templates
- **Binary Size**: ~40-60% smaller than standard
- **RAM Usage**: ~30-50% less than standard
- **Functionality**: Full 2D support, basic networking, audio

### Minimal Editor
- **Binary Size**: ~25-40% smaller than standard
- **RAM Usage**: ~25-40% less during development
- **Functionality**: Reduced development tools

### Ultra-Minimal Export Templates
- **Binary Size**: ~70-80% smaller than standard
- **RAM Usage**: ~60-80% less than standard
- **Functionality**: Headless only, GDScript scripting

## Platform Support

All scripts automatically detect and build for:
- **Linux** (linuxbsd)
- **Windows** (windows)
- **macOS** (macos)

## Output Files

After successful builds, you'll find:

### Export Templates
- `bin/godot.linuxbsd.template_release.x86_64` (Linux)
- `bin/godot.windows.template_release.x86_64.exe` (Windows)
- `bin/godot.macos.template_release.x86_64` (macOS)

### Editor (if built)
- `bin/godot.linuxbsd.editor.x86_64` (Linux)
- `bin/godot.windows.editor.x86_64.exe` (Windows)
- `bin/godot.macos.editor.x86_64` (macOS)

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

## Next Steps

1. **Build export templates**: `python3 build_minimal_godot.py`
2. **Configure your project** to use the minimal templates
3. **Test the exports** with simple Godot projects
4. **Measure actual RAM usage** in your specific use case
5. **Customize further** based on your needs
6. **Use in production** for your RAM-constrained applications

The minimal builds should significantly reduce RAM usage in your exported games while maintaining the functionality you need.