#!/usr/bin/env python3
"""
Script to build an ultra-minimal Godot 4.4 with absolute minimum RAM usage
WARNING: This creates a very limited Godot build suitable only for specific use cases
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

    print(f"Building ULTRA-MINIMAL Godot for platform: {target_platform}")
    print("WARNING: This will create a very limited Godot build!")
    
    # Absolute minimum modules (core only)
    core_modules = [
        "gdscript",  # Core scripting (required)
    ]
    
    # Build command for ultra-minimal export templates
    build_cmd = [
        "scons",
        f"platform={target_platform}",
        "target=template_release",
        "profile=custom_ultra_minimal",
        "optimize=size_extra",
        "lto=full",
        "production=yes",
        "disable_3d=yes",
        "disable_physics_2d=yes",
        "disable_physics_3d=yes",
        "disable_navigation_2d=yes",
        "disable_navigation_3d=yes",
        "disable_xr=yes",
        "disable_advanced_gui=yes",
        "vulkan=no",
        "opengl3=no",
        "d3d12=no",
        "metal=no",
        "xaudio2=no",
        "brotli=no",
        "minizip=no",
        "accesskit=no",
        "sdl=no",
        "threads=no",
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
        "-j2"  # Use fewer cores to avoid RAM issues
    ]
    
    # Add only core modules
    for module in core_modules:
        build_cmd.append(f"module_{module}_enabled=yes")
    
    # Disable ALL third-party libraries
    all_libs = [
        "builtin_brotli", "builtin_certs", "builtin_clipper2", "builtin_embree",
        "builtin_enet", "builtin_freetype", "builtin_msdfgen", "builtin_glslang",
        "builtin_graphite", "builtin_harfbuzz", "builtin_sdl", "builtin_icu4c",
        "builtin_libjpeg_turbo", "builtin_libogg", "builtin_libpng", "builtin_libtheora",
        "builtin_libvorbis", "builtin_libwebp", "builtin_wslay", "builtin_mbedtls",
        "builtin_miniupnpc", "builtin_openxr", "builtin_pcre2", "builtin_pcre2_with_jit",
        "builtin_recastnavigation", "builtin_rvo2_2d", "builtin_rvo2_3d", "builtin_xatlas",
        "builtin_zlib", "builtin_zstd"
    ]
    
    for lib in all_libs:
        build_cmd.append(f"{lib}=no")
    
    print("Building ultra-minimal Godot export template...")
    print(f"Core modules only: {', '.join(core_modules)}")
    print("\nThis build will have:")
    print("- NO rendering (headless only)")
    print("- NO audio")
    print("- NO input handling")
    print("- NO networking")
    print("- NO physics")
    print("- NO navigation")
    print("- NO image loading")
    print("- NO font rendering")
    print("- NO compression")
    print("- NO third-party libraries")
    
    confirm = input("\nAre you sure you want to continue? (yes/no): ")
    if confirm.lower() != "yes":
        print("Build cancelled.")
        return 0
    
    if not run_command(build_cmd, "Building ultra-minimal Godot"):
        return 1
    
    print("\n=== Ultra-minimal build completed! ===")
    print("This Godot build has absolute minimum RAM usage but very limited functionality.")
    print("It's suitable only for:")
    print("- Headless servers")
    print("- Command-line tools")
    print("- Simple scripting tasks")
    print("- Testing core engine functionality")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())