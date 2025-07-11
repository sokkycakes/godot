# GitHub Actions for Minimal Godot Builds

This repository includes GitHub Actions workflows that automatically build minimal Godot 4.4 with reduced RAM usage.

## Available Workflows

### 1. Simple Build (`build-minimal-godot-simple.yml`)
- **Purpose**: Quick builds for Linux only
- **Builds**: Balanced minimal and ultra-minimal export templates
- **Platform**: Linux only
- **Duration**: ~30-60 minutes
- **Best for**: Testing and quick builds

### 2. Full Build (`build-minimal-godot.yml`)
- **Purpose**: Complete builds for all platforms
- **Builds**: All export templates + minimal editor
- **Platforms**: Linux, Windows, macOS
- **Duration**: ~2-4 hours
- **Best for**: Production releases

## How to Use

### Automatic Builds
The workflows run automatically when you:
- Push to `main` or `master` branch
- Create a pull request

### Manual Builds
To trigger a build manually:

1. Go to your GitHub repository
2. Click **Actions** tab
3. Select the workflow you want to run
4. Click **Run workflow**
5. Choose the branch and click **Run workflow**

### Downloading Builds

#### From Artifacts (Immediate)
1. Go to **Actions** tab
2. Click on a completed workflow run
3. Scroll down to **Artifacts**
4. Download the artifacts you need:
   - `godot-minimal-linux` - Balanced minimal export template
   - `godot-ultra-minimal-linux` - Ultra-minimal export template
   - `godot-minimal-editor-linux` - Minimal editor

#### From Releases (Recommended)
1. Go to **Releases** tab
2. Download the latest release zip file
3. Extract and use the appropriate files

## Workflow Details

### Simple Workflow
```yaml
jobs:
  build-linux-minimal:      # Balanced minimal build
  build-linux-ultra-minimal: # Ultra-minimal build
  create-simple-release:     # Creates GitHub release
```

### Full Workflow
```yaml
jobs:
  build-linux:              # Linux export templates
  build-windows:            # Windows export templates
  build-macos:              # macOS export templates
  build-ultra-minimal:      # Ultra-minimal Linux
  build-minimal-editor:     # Minimal editor
  create-release:           # Creates GitHub release
```

## Build Outputs

### Export Templates
- **Balanced Minimal**: 2D support, audio, networking, ~40-60% size reduction
- **Ultra-Minimal**: Headless only, GDScript only, ~70-80% size reduction

### File Locations
```
bin/
├── godot.linuxbsd.template_release.x86_64    # Linux export template
├── godot.windows.template_release.x86_64.exe # Windows export template
├── godot.macos.template_release.x86_64       # macOS export template
└── godot.linuxbsd.editor.x86_64              # Linux editor (full workflow only)
```

## Using the Built Templates

### 1. Download the Build
- From **Actions** → **Artifacts** (immediate)
- From **Releases** (recommended)

### 2. Configure Your Project
1. Open your Godot project in the editor
2. Go to **Project → Project Settings → Export**
3. Select your export preset (e.g., "Linux/X11")
4. Set **Export Path** (where your game will be exported)
5. **Important**: Set **Custom Template** to the downloaded export template

### 3. Export Your Game
- Click **Export Project**
- Your exported game will use the minimal runtime engine
- Significantly reduced RAM usage compared to standard exports

## Troubleshooting

### Build Fails
1. **Check Actions logs** for specific error messages
2. **Common issues**:
   - Missing dependencies
   - Out of memory (reduce parallel jobs)
   - Platform-specific issues

### Build Takes Too Long
1. **Use simple workflow** for Linux-only builds
2. **Reduce parallel jobs** in workflow files
3. **Disable LTO** by modifying build scripts

### Download Issues
1. **Artifacts expire** after 30 days
2. **Use releases** for long-term storage
3. **Check file sizes** - builds can be 20-100MB

## Customization

### Modify Build Scripts
Edit the build scripts before pushing:
- `build_minimal_godot.py` - Balanced minimal build
- `build_ultra_minimal.py` - Ultra-minimal build
- `build_minimal_editor.py` - Minimal editor build

### Modify Workflows
Edit the workflow files to:
- Add more platforms
- Change build parameters
- Modify artifact retention
- Add custom build steps

### Environment Variables
Set repository secrets for:
- Custom build parameters
- Release tokens
- Build optimization flags

## Cost Considerations

### GitHub Actions Limits
- **Public repos**: 2,000 minutes/month free
- **Private repos**: 500 minutes/month free
- **Build time**: 30 minutes to 4 hours per build

### Optimization Tips
1. **Use simple workflow** for testing
2. **Cache dependencies** to speed up builds
3. **Build only needed platforms**
4. **Use matrix builds** for efficiency

## Security Notes

### Build Security
- Builds run in isolated environments
- No access to your local files
- Dependencies installed from official sources
- Build artifacts are temporary

### Release Security
- Releases are public (for public repos)
- Use private repos for sensitive builds
- Review release contents before publishing

## Next Steps

1. **Push your code** to trigger automatic builds
2. **Monitor the Actions** tab for build progress
3. **Download artifacts** or releases
4. **Test the builds** with your projects
5. **Customize** builds for your specific needs

The GitHub Actions workflows provide a convenient way to build minimal Godot without using your local machine's resources.