#!/usr/bin/env python3
"""
Script to build a minimal Godot 4.4 editor with reduced RAM usage
This script builds the editor (not export templates) with minimal features
"""

import os
import sys
import subprocess
import platform

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n=== {description} ===")
    print(f"Running: {' '.join(cmd)}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    
    print(f"Success: {result.stdout}")
    return True

def main():
    # Detect platform
    system = platform.system().lower()
    if system == "linux":
        target_platform = "linuxbsd"
    elif system == "darwin":
        target_platform = "macos"
    elif system == "windows":
        target_platform = "windows"
    else:
        print(f"Unsupported platform: {system}")
        return 1

    print(f"Building minimal Godot editor for platform: {target_platform}")
    print("Note: The editor will still be large due to development tools")
    
    # Essential modules for editor (more than export templates)
    essential_modules = [
        "gdscript",  # Core scripting
        "regex",     # Regular expressions
        "jsonrpc",   # JSON-RPC (required for editor)
        "zip",       # ZIP support (for project files)
        "png",       # PNG image support
        "jpg",       # JPEG image support
        "bmp",       # BMP image support
        "tga",       # TGA image support
        "dds",       # DDS image support
        "ktx",       # KTX image support
        "hdr",       # HDR image support
        "svg",       # SVG image support
        "freetype",  # Font rendering
        "text_server_adv",  # Advanced text server
        "text_server_fb",   # Fallback text server
        "gltf",      # GLTF support
        "csg",       # CSG nodes
        "gridmap",   # GridMap
        "camera",    # Camera nodes
        "audio",     # Audio system
        "enet",      # Networking
        "mbedtls",   # SSL/TLS
        "zlib",      # Compression
        # Editor-specific modules
        "editor",    # Editor functionality
        "editor_import_export",  # Import/export tools
        "editor_scene",  # Scene editing
        "editor_ui",     # UI editing
        "editor_debugger",  # Debugging tools
        "editor_plugins",   # Plugin system
    ]
    
    # Build command for minimal editor
    build_cmd = [
        "scons",
        f"platform={target_platform}",
        "target=editor",  # Build editor, not export template
        "profile=custom",
        "optimize=size_extra",
        "lto=full",
        "production=yes",
        "disable_3d=yes",
        "disable_physics_3d=yes",
        "disable_navigation_3d=yes",
        "disable_xr=yes",
        "disable_advanced_gui=yes",
        "vulkan=no",
        "opengl3=yes",
        "xaudio2=no",
        "brotli=no",
        "minizip=no",
        "accesskit=no",
        "deprecated=no",
        "modules_enabled_by_default=no",
        "no_editor_splash=yes",
        "engine_update_check=no",
        "steamapi=no",
        "debug_symbols=no",
        "dev_build=no",
        "tests=no",
        "verbose=no",
        "disable_exceptions=yes",
        "strict_checks=no",
        "use_precise_math_checks=no",
        "scu_build=no",
        "redirect_build_objects=no",
        "-j4"  # Use 4 cores
    ]
    
    # Add essential modules
    for module in essential_modules:
        build_cmd.append(f"module_{module}_enabled=yes")
    
    # Disable heavy third-party libraries
    heavy_libs = [
        "builtin_brotli", "builtin_embree", "builtin_msdfgen", "builtin_glslang",
        "builtin_graphite", "builtin_harfbuzz", "builtin_icu4c", "builtin_libtheora",
        "builtin_libvorbis", "builtin_libwebp", "builtin_wslay", "builtin_miniupnpc",
        "builtin_openxr", "builtin_pcre2_with_jit", "builtin_recastnavigation",
        "builtin_rvo2_2d", "builtin_rvo2_3d", "builtin_xatlas", "builtin_zstd"
    ]
    
    for lib in heavy_libs:
        build_cmd.append(f"{lib}=no")
    
    # Keep essential libraries
    essential_libs = [
        "builtin_certs", "builtin_clipper2", "builtin_freetype", "builtin_sdl",
        "builtin_libjpeg_turbo", "builtin_libogg", "builtin_libpng", "builtin_mbedtls",
        "builtin_pcre2", "builtin_zlib"
    ]
    
    for lib in essential_libs:
        build_cmd.append(f"{lib}=yes")
    
    print("Building minimal Godot editor...")
    print(f"Essential modules: {', '.join(essential_modules)}")
    
    if not run_command(build_cmd, "Building minimal Godot editor"):
        return 1
    
    print("\n=== Build completed successfully! ===")
    print("The minimal Godot editor has been built with reduced RAM usage.")
    print("Key optimizations applied:")
    print("- Disabled 3D rendering and physics")
    print("- Disabled XR support")
    print("- Disabled heavy third-party libraries")
    print("- Enabled size optimization and LTO")
    print("- Kept only essential modules")
    print("\nNote: The editor will still be large due to development tools,")
    print("but it will use less RAM than the standard editor.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())