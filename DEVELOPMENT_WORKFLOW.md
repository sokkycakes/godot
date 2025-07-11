# Godot Development Workflow with Minimal Builds

This guide explains how to use minimal Godot builds in your development workflow to reduce RAM usage in your exported games.

## Understanding the Components

### 1. Godot Editor (Development Environment)
- **Purpose**: Create and edit your games
- **Size**: Large (100-200MB+) because it includes all development tools
- **RAM Usage**: High during development
- **Source**: Download from godotengine.org OR build minimal editor

### 2. Export Templates (Runtime Engine)
- **Purpose**: Run your exported games
- **Size**: Smaller (20-50MB) because no development tools
- **RAM Usage**: Much lower than editor
- **Source**: Build with these scripts

## Development Workflow Options

### Option 1: Standard Editor + Minimal Export Templates (Recommended)

#### Step 1: Get Standard Editor
```bash
# Download from godotengine.org
# OR build a minimal editor
python3 build_minimal_editor.py
```

#### Step 2: Build Minimal Export Templates
```bash
# Build minimal export templates
python3 build_minimal_godot.py
```

#### Step 3: Configure Project
1. Open your Godot project in the editor
2. Go to **Project → Project Settings → Export**
3. Select your export preset (e.g., "Linux/X11")
4. Set **Export Path** (where your game will be exported)
5. **Important**: Set **Custom Template** to your minimal export template:
   - Linux: `bin/godot.linuxbsd.template_release.x86_64`
   - Windows: `bin/godot.windows.template_release.x86_64.exe`
   - macOS: `bin/godot.macos.template_release.x86_64`

#### Step 4: Export Your Game
- Click **Export Project**
- Your exported game will use the minimal runtime engine
- Significantly reduced RAM usage compared to standard exports

### Option 2: Minimal Editor + Minimal Export Templates

#### Step 1: Build Minimal Editor
```bash
python3 build_minimal_editor.py
```

#### Step 2: Build Minimal Export Templates
```bash
python3 build_minimal_godot.py
```

#### Step 3: Use Both Minimal Builds
- Use the minimal editor for development
- Use minimal export templates for exports
- Maximum RAM savings but limited editor features

## File Locations After Building

### Export Templates
```
bin/
├── godot.linuxbsd.template_release.x86_64    # Linux export template
├── godot.windows.template_release.x86_64.exe # Windows export template
└── godot.macos.template_release.x86_64       # macOS export template
```

### Editor (if built)
```
bin/
└── godot.linuxbsd.editor.x86_64              # Linux editor
```

## RAM Usage Comparison

### During Development
- **Standard Editor**: 200-500MB RAM
- **Minimal Editor**: 150-300MB RAM (25-40% reduction)

### In Exported Games
- **Standard Export**: 50-150MB RAM
- **Minimal Export**: 20-80MB RAM (40-60% reduction)

## When to Use Each Option

### Use Standard Editor + Minimal Exports When:
- You want full editor features
- You're doing complex development
- You need all editor plugins and tools
- You want maximum compatibility

### Use Minimal Editor + Minimal Exports When:
- You're doing simple 2D development
- You have limited development machine RAM
- You don't need advanced editor features
- You want maximum RAM savings everywhere

## Project Configuration Examples

### For 2D Games
```python
# In custom.py - disable 3D features
disable_3d = True
disable_physics_3d = True
disable_navigation_3d = True
disable_xr = True

# Keep 2D features
disable_physics_2d = False
disable_navigation_2d = False
opengl3 = True
```

### For Headless Applications
```python
# In custom_ultra_minimal.py - disable everything
disable_3d = True
disable_physics_2d = True
disable_navigation_2d = True
opengl3 = False
sdl = False
audio = False
```

## Testing Your Minimal Builds

### Test Export Templates
```bash
# Test if your export template works
./bin/godot.linuxbsd.template_release.x86_64 --version

# Test with a simple project
./bin/godot.linuxbsd.template_release.x86_64 --path /path/to/test/project
```

### Test Editor (if built)
```bash
# Test if your minimal editor works
./bin/godot.linuxbsd.editor.x86_64 --version

# Open a project
./bin/godot.linuxbsd.editor.x86_64 --path /path/to/project
```

## Troubleshooting

### Export Template Issues
1. **Game won't start**: Check if required modules are enabled
2. **Missing features**: Add missing modules to `essential_modules` list
3. **Rendering issues**: Ensure `opengl3=yes` for 2D games

### Editor Issues
1. **Editor crashes**: Try standard editor instead
2. **Missing tools**: Add required editor modules
3. **Import errors**: Check if import modules are enabled

### Build Issues
1. **Build fails**: Check dependencies and try `lto=none`
2. **Out of memory**: Reduce parallel jobs with `-j2`
3. **Module errors**: Check module dependencies

## Advanced Configuration

### Custom Module Selection
Edit the `essential_modules` list in build scripts:

```python
essential_modules = [
    "gdscript",      # Always needed
    "regex",         # Regular expressions
    "jsonrpc",       # Editor communication
    "zip",           # Project files
    "png", "jpg",    # Image formats you use
    "freetype",      # Font rendering
    "audio",         # If you need audio
    "enet",          # If you need networking
    # Add your specific modules here
]
```

### Platform-Specific Optimizations
```bash
# Linux - optimize for size
scons platform=linuxbsd target=template_release optimize=size_extra lto=full

# Windows - optimize for compatibility
scons platform=windows target=template_release optimize=size lto=thin

# macOS - optimize for performance
scons platform=macos target=template_release optimize=speed lto=full
```

## Best Practices

1. **Start with balanced minimal build** - it's the safest option
2. **Test thoroughly** - minimal builds may break some features
3. **Profile your game** - measure actual RAM usage
4. **Keep backups** - of both standard and minimal builds
5. **Document your setup** - for team members and future reference

## Summary

- **Export templates** = smaller, faster, less RAM usage in your final games
- **Editor** = development environment (can be minimal or standard)
- **Workflow** = develop with editor, export with minimal templates
- **Result** = same development experience, smaller exported games

The key benefit is that your exported games will use significantly less RAM while maintaining the same development experience.